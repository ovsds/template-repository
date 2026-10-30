import json
import os
import shlex

import tests.utils.replay as replay_utils
import tests.utils.cli as cli_utils

MANIFEST_PATH = "tests/replays.json"
ADDITIONAL_FILES_PATH = "tests/additional_files"
RESULTS_PATH = ".test_results"
NODE_BIN_PATH = "node_modules/.bin"
AGENT_SKILLS_PATHS = [
    "mise.toml",
    ".github/workflows/check-pr.yaml",
    ".gitignore",
    ".prettierignore",
    "package.json",
]


def assert_agent_skills_baseline(cwd: str):
    with open(f"{cwd}/.github/workflows/check-pr.yaml", encoding="utf-8") as file:
        workflow = file.read()
    assert "  push:\n    branches:\n      - main\n" in workflow
    assert "  workflow_dispatch:\n" in workflow
    assert "github.event.number || github.sha" in workflow

    with open(f"{cwd}/mise.toml", encoding="utf-8") as file:
        mise = file.read()
    assert mise.count('GH_TOKEN="${GH_TOKEN:-$(gh auth token)}" zizmor .') == 2

    for ignore_path in [".gitignore", ".prettierignore"]:
        with open(f"{cwd}/{ignore_path}", encoding="utf-8") as file:
            ignore = file.read()
        for pattern in ["/artifacts/", ".venv/", "__pycache__/", ".pytest_cache/", ".ruff_cache/", ".coverage"]:
            assert pattern in ignore, f"{ignore_path} misses {pattern}"

    with open(f"{cwd}/package.json", encoding="utf-8") as file:
        package = json.load(file)
    assert "hooks" not in package


def test_replay(replay: replay_utils.Replay):
    replay_utils.clean_replay(replay, RESULTS_PATH)
    replay_utils.build_replay(replay, RESULTS_PATH)

    cwd = f"{RESULTS_PATH}/{replay.parameters['project_slug']}"
    replay_utils.copy_additional_files(replay, ADDITIONAL_FILES_PATH, cwd)

    cli_utils.run_command("git init", cwd=cwd)
    cli_utils.run_command("git add --all", cwd=cwd)
    cli_utils.run_command("git -c user.name=test -c user.email=test@example.com -c commit.gpgsign=false commit --quiet --no-verify -m init", cwd=cwd)
    if replay.parameters.get("scripts") == "true":
        assert not os.path.exists(f"{cwd}/.scripts/uv.lock"), "template rendered a uv lockfile"
    cli_utils.run_command("mise run init", cwd=cwd)
    if replay.parameters.get("scripts") == "true":
        assert os.path.exists(f"{cwd}/.scripts/uv.lock"), "mise init did not create a uv lockfile"
    cli_utils.run_command("mise run lint", cwd=cwd)
    cli_utils.run_command("mise run lint-fix", cwd=cwd)
    if replay.name == "Agent Skills":
        assert_agent_skills_baseline(cwd)
        replay_paths = [f"{cwd}/{path}" for path in AGENT_SKILLS_PATHS]
        replay_contents = {}
        for path in replay_paths:
            with open(path, encoding="utf-8") as file:
                replay_contents[path] = file.read()
        template_path = shlex.quote(os.path.abspath("."))
        cli_utils.run_command(f"TEMPLATE_PATH={template_path} mise run update-from-template", cwd=cwd)
        for path in replay_paths:
            with open(path, encoding="utf-8") as file:
                assert file.read() == replay_contents[path], f"template update changed {path}"
    cli_utils.run_command("git worktree add --quiet --detach artifacts/worktrees/test", cwd=cwd)
    cli_utils.run_command("mise run clean", cwd=cwd)
    assert not os.path.exists(f"{cwd}/artifacts"), "mise run clean left artifacts/"
    assert not os.path.exists(f"{cwd}/.git/worktrees"), "mise run clean left the worktree registered"

    replay_utils.clean_replay(replay, RESULTS_PATH)


def test_replays():
    # mise refuses [env] and [settings] of an untrusted config; trust the throwaway results only for this run
    trusted_paths = [os.environ.get("MISE_TRUSTED_CONFIG_PATHS"), os.path.abspath(RESULTS_PATH)]
    os.environ["MISE_TRUSTED_CONFIG_PATHS"] = os.pathsep.join(filter(None, trusted_paths))
    for replay in replay_utils.read_replays(MANIFEST_PATH):
        test_replay(replay)


__all__ = [
    "test_replays",
]
