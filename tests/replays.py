import os

import tests.utils.replay as replay_utils
import tests.utils.cli as cli_utils

MANIFEST_PATH = "tests/replays.json"
ADDITIONAL_FILES_PATH = "tests/additional_files"
RESULTS_PATH = ".test_results"
NODE_BIN_PATH = "node_modules/.bin"


def test_replay(replay: replay_utils.Replay):
    replay_utils.clean_replay(replay, RESULTS_PATH)
    replay_utils.build_replay(replay, RESULTS_PATH)

    cwd = f"{RESULTS_PATH}/{replay.parameters['project_slug']}"
    replay_utils.copy_additional_files(replay, ADDITIONAL_FILES_PATH, cwd)

    cli_utils.run_command("git init", cwd=cwd)
    cli_utils.run_command("git add --all", cwd=cwd)
    cli_utils.run_command("git -c user.name=test -c user.email=test@example.com -c commit.gpgsign=false commit --quiet --no-verify -m init", cwd=cwd)
    cli_utils.run_command("mise run init", cwd=cwd)
    cli_utils.run_command("mise run lint", cwd=cwd)
    cli_utils.run_command("mise run lint-fix", cwd=cwd)
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
