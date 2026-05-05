# Cookiecutter Template for GitHub Repository

[![CI](https://github.com/ovsds/template-repository/workflows/Check%20PR/badge.svg)](https://github.com/ovsds/template-repository/actions?query=workflow%3A%22%22Check+PR%22%22)

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template that bootstraps a new GitHub repository with a consistent baseline of CI, commit hygiene, and developer tooling. Used across `@ovsds` personal projects so each new repo starts from the same opinionated scaffold instead of being assembled ad-hoc.

## What you get

Every generated repo includes, regardless of options:

- **MIT `LICENSE`** stamped with the configured owner; standard `.editorconfig`, `.gitignore`, `.nvmrc`, `.npmrc`, `.prettierignore`.
- **`Taskfile.yaml`** as the unified entry point — `task init`, `task lint`, `task lint-fix`, `task test`, `task clean`, `task dependencies-update`, `task dependencies-check`, `task update-from-template`.
- **Husky hooks** wiring `pre-commit` through `lint-staged` (Prettier `--check` over `*.{md,yaml,json,js}`) and `commit-msg` through [commitlint](https://commitlint.js.org/) with `@commitlint/config-conventional`.
- **GitHub Actions:**
  - `Check PR` — installs deps, lints, tests on every PR. Toolchain setup factored into a reusable composite action at `.github/actions/setup_environment`.
  - `Check PR Title` — enforces conventional-commit titles via [`ovsds/commitlint-pr-title-action`](https://github.com/ovsds/commitlint-pr-title-action).

Opt-in via flags in [`cookiecutter.json`](cookiecutter.json):

| Flag                     | Adds                                                                                                                                          |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `with_build=true`        | `Release` + `Release PR` workflows — build & push images to GHCR; PR builds get a Trivy scan whose results are posted as a sticky PR comment. |
| `with_docker=true`       | `docker/` subfolder with its own Taskfile and a base/dev/CI compose layering for auxiliary containers used in CI.                             |
| `with_python=true`       | Python + Poetry support in the setup action; Pyright wired into devDependencies.                                                              |
| `with_zizmor=true`       | [Zizmor](https://woodruffw.github.io/zizmor/) GHA security scan integrated into `task lint`.                                                  |
| `with_trivy=true`        | Trivy installed by the setup action (used by the image scan in `Release PR`).                                                                 |
| `with_cookiecutter=true` | Wires the project's own `tests/` runner — for when the generated repo is itself a Cookiecutter template.                                      |
| `scripts=true`           | `.scripts/` subfolder of shared Python/bash helpers, included into the root Taskfile.                                                         |
| `services="a b c"`       | Multi-service workspace — each service gets its own Taskfile; `init` / `lint` / `test` / `clean` are fanned out across all of them.           |

`task update-from-template` re-applies the template to an existing repo with the same answers, so scaffold improvements can be pulled in over time.

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

You'll be prompted for `project_name`, `node_version`, owner identity, and the feature flags above. Defaults live in [`cookiecutter.json`](cookiecutter.json).

## Development

### Global dependencies

- [Taskfile](https://taskfile.dev/installation/)
- [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)
- [zizmor](https://woodruffw.github.io/zizmor/installation/) — used for GHA security scanning

### Taskfile commands

For all commands see [Taskfile](Taskfile.yaml) or `task --list-all`.

## License

[MIT](LICENSE)
