#!/usr/bin/env bash
set -eo pipefail

# zizmor has no devcontainer feature; install via pipx (python feature provides it).
pipx install "zizmor==1.0.1"

# Install Node deps + wire husky.
task init
