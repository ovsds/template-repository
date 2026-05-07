#!/usr/bin/env bash
set -eo pipefail
# nvm.sh references unset vars; cannot use `set -u`.

TASK_VERSION="v3.33.1"
NVM_VERSION="v0.40.1"
COOKIECUTTER_VERSION="2.4.0"
ZIZMOR_VERSION="1.0.1"

# Install task (go-task). The Taskfile is the unified entry point.
if ! command -v task >/dev/null; then
  sudo sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin "${TASK_VERSION}"
fi

# Install nvm at ~/.nvm — Taskfile's _with_nvm sources from this path.
# git clone avoids nvm's install.sh, which exits non-zero under `set -eo pipefail`.
if [ ! -d "${HOME}/.nvm" ]; then
  git clone --depth 1 -b "${NVM_VERSION}" https://github.com/nvm-sh/nvm.git "${HOME}/.nvm"
fi
export NVM_DIR="${HOME}/.nvm"
# shellcheck source=/dev/null
. "${NVM_DIR}/nvm.sh"
nvm install

# Python tools used by tasks: cookiecutter (update-from-template), zizmor (lint).
pipx install "cookiecutter==${COOKIECUTTER_VERSION}"
pipx install "zizmor==${ZIZMOR_VERSION}"

# Install Node deps + wire husky.
task init
