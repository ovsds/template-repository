#!/usr/bin/env bash
set -eo pipefail

# zizmor + trivy have no community devcontainer features.

pipx install "zizmor==1.0.1"

TRIVY_VERSION="v0.69.3"
if ! command -v trivy >/dev/null; then
  TRIVY_TARBALL="trivy_${TRIVY_VERSION#v}_Linux-64bit.tar.gz"
  curl -fsSL "https://github.com/aquasecurity/trivy/releases/download/${TRIVY_VERSION}/${TRIVY_TARBALL}" \
    | sudo tar -xz -C /usr/local/bin trivy
fi

# Install Node deps + wire husky.
task init
