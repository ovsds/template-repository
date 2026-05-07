#!/usr/bin/env bash
set -eo pipefail

TASK_VERSION="v3.33.1"
COOKIECUTTER_VERSION="2.4.0"
ZIZMOR_VERSION="1.0.1"

# Install task (go-task). The Taskfile is the unified entry point.
if ! command -v task >/dev/null; then
  sudo sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin "${TASK_VERSION}"
fi

# Python tools used by tasks: cookiecutter (update-from-template), zizmor (lint).
pipx install "cookiecutter==${COOKIECUTTER_VERSION}"
pipx install "zizmor==${ZIZMOR_VERSION}"

# Install Node deps + wire husky. Node + nvm come from the node devcontainer feature.
task init
