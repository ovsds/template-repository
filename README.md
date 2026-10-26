# Cookiecutter Template for GitHub Repository

[![CI](https://github.com/ovsds/template-repository/workflows/Check%20PR/badge.svg)](https://github.com/ovsds/template-repository/actions?query=workflow%3A%22%22Check+PR%22%22)

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template that bootstraps a new GitHub repository with a consistent baseline of CI, commit hygiene, and developer tooling. Used across `@ovsds` personal projects so each new repo starts from the same opinionated scaffold instead of being assembled ad-hoc.

## What you get

Every generated repo includes, regardless of options:

- **MIT `LICENSE`** stamped with the configured owner; standard `.editorconfig`, `.gitignore`, `.npmrc`, `.prettierignore`.
- **`mise.toml`** pinning the whole toolchain (Node from `node_version`, Python from `python_version`, e.g. `3.15.0`, when a flag below needs it - `.scripts` runs on it; keep the services' Python equal to it, or `mise install --monorepo` drops it and Poetry fails to install; and the tools enabled by the flags below), so `mise install` is the only setup step locally and in CI.
- **[mise tasks](https://mise.jdx.dev/tasks/)** in the same `mise.toml` as the unified entry point — `mise run init`, `mise run lint`, `mise run lint-fix`, `mise run test`, `mise run clean`, `mise run dependencies-update`, `mise run dependencies-check`, `mise run update-from-template`.
- **Husky hooks** wiring `pre-commit` through `lint-staged` (Prettier `--check` over `*.{md,yaml,json,js}`) and `commit-msg` through [commitlint](https://commitlint.js.org/) with `@commitlint/config-conventional`.
- **GitHub Actions:**
  - `Check PR` — installs deps, lints, tests on every PR. Toolchain setup factored into a reusable composite action at `.github/actions/setup_environment`, which installs `mise.toml` tools with [`jdx/mise-action`](https://github.com/jdx/mise-action).
  - `Check PR Title` — enforces conventional-commit titles via [`ovsds/commitlint-pr-title-action`](https://github.com/ovsds/commitlint-pr-title-action).

Generated workflows use the `github_workflow_runs_on` Cookiecutter answer, which defaults to `ubuntu-latest`. For a repository that needs a configurable runner, use `"${{ '{{' }} vars.RUNS_ON || 'ubuntu-latest' }}"` as its answer. Cookiecutter renders the `{{ '{{' }}` part into `{{`, leaving `"${{ vars.RUNS_ON || 'ubuntu-latest' }}"` in the workflows. The generated `update-from-template` task preserves the escaped answer for later renders.

Opt-in via flags in [`cookiecutter.json`](cookiecutter.json):

| Flag                     | Adds                                                                                                                                                                                                                                                        |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `with_build=true`        | `Release` + `Release PR` workflows — build & push images to GHCR; PR builds get a Trivy scan whose results are posted as a sticky PR comment.                                                                                                               |
| `with_docker=true`       | `docker/` subfolder with its own mise tasks and a base/dev/CI compose layering for auxiliary containers used in CI.                                                                                                                                         |
| `with_python=true`       | Python + Poetry in `mise.toml`; Pyright wired into devDependencies.                                                                                                                                                                                         |
| `with_zizmor=true`       | [Zizmor](https://woodruffw.github.io/zizmor/) in `mise.toml`, GHA security scan integrated into `mise run lint`.                                                                                                                                            |
| `with_gitleaks=true`     | [Gitleaks](https://github.com/gitleaks/gitleaks) in `mise.toml`, secret scan of git history integrated into `mise run lint`.                                                                                                                                |
| `with_trivy=true`        | Trivy in `mise.toml` (used by the image scan in `Release PR`).                                                                                                                                                                                              |
| `with_cookiecutter=true` | Cookiecutter in `mise.toml` and the project's own `tests/` runner — for when the generated repo is itself a Cookiecutter template.                                                                                                                          |
| `scripts=true`           | `.scripts/` subfolder of shared Python/bash helpers, a [monorepo config root](https://mise.jdx.dev/tasks/monorepo.html) whose tasks the root ones call.                                                                                                     |
| `services="a b c"`       | Multi-service workspace — each service is a monorepo config root whose `mise.toml` implements `init`, `lint`, `lint-fix`, `test`, `clean`, `dependencies-update` and `dependencies-check`; the root tasks fan out to all of them and fail on a missing one. |

A service nested in another one (`services="a a/b"`) is only a config root: the root tasks fan out to `a`, whose own
tasks fan out to `a/b`.

`mise run update-from-template` re-applies the template to an existing repo with the same answers, so scaffold improvements can be pulled in over time.

Project-specific tasks go into `mise-tasks/` as file tasks, which the template never overwrites; with `with_build=true` the release workflows expect `ci-image-push` and `ci-image-scan` there.

`mise run clean` removes the whole `artifacts/` folder, worktrees included, and prunes them: uncommitted work in a worktree there is lost.

Upgrading `.scripts` from its own Python 3.12 pin: run `mise run clean`, `mise run lint-fix` and `mise run init` after the first update, which relocks it for secret-transfer 0.5; later updates relock it themselves.

Upgrading a repository generated with Taskfile: `update-from-template` removes the template's own Taskfiles, but each service's `Taskfile.yaml` has to be ported to its `mise.toml` by hand, in the same change, since `task` is no longer installed.

## Quickstart

Global dependency: [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/installation.html).

```shell
cookiecutter https://github.com/ovsds/template-repository
```

Or, to regenerate scaffold inside an already-cloned repo:

```shell
cookiecutter \
  --overwrite-if-exists \
  --output-dir ../ \
  https://github.com/ovsds/template-repository
```

You'll be prompted for `project_name`, `node_version`, `python_version`, owner identity, and the feature flags above. Defaults live in [`cookiecutter.json`](cookiecutter.json).

## Development

### Global dependencies

- [mise](https://mise.jdx.dev/installing-mise.html), activated in the shell (`eval "$(mise activate zsh)"`)

All other tools are pinned in [mise.toml](mise.toml).

### mise tasks

For all commands see [mise.toml](mise.toml) or `mise tasks ls`.

## License

[MIT](LICENSE)
