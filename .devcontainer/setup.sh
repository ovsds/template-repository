#!/usr/bin/env bash
set -eo pipefail

# This devcontainer is built to run the template's full replay test matrix
# (tests/replays.py renders cookiecutter for each flag combo and runs task
# init / lint / lint-fix / clean inside this container), so it bundles the
# union of every optional flag's tooling: poetry, trivy, etc.

TASK_VERSION="v3.33.1"
COOKIECUTTER_VERSION="2.4.0"
ZIZMOR_VERSION="1.0.1"
POETRY_VERSION="1.7.1"
TRIVY_VERSION="v0.57.1"

# Install task (go-task). The Taskfile is the unified entry point.
if ! command -v task >/dev/null; then
  sudo sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin "${TASK_VERSION}"
fi

# Python tools used by tasks across replay variants.
pipx install "cookiecutter==${COOKIECUTTER_VERSION}"
pipx install "zizmor==${ZIZMOR_VERSION}"
pipx install "poetry==${POETRY_VERSION}"

# Trivy (used by the with_trivy replay variant).
if ! command -v trivy >/dev/null; then
  curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh \
    | sudo sh -s -- -b /usr/local/bin "${TRIVY_VERSION}"
fi

# Install Node deps + wire husky. Node + nvm come from the node devcontainer feature.
task init
