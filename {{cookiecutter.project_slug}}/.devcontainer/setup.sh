#!/usr/bin/env bash
set -eo pipefail
{%- if cookiecutter.with_zizmor == 'true' %}

pipx install "zizmor==1.0.1"
{%- endif %}
{%- if cookiecutter.with_trivy == 'true' %}

TRIVY_VERSION="v0.69.3"
if ! command -v trivy >/dev/null; then
  TRIVY_TARBALL="trivy_${TRIVY_VERSION#v}_Linux-64bit.tar.gz"
  curl -fsSL "https://github.com/aquasecurity/trivy/releases/download/${TRIVY_VERSION}/${TRIVY_TARBALL}" \
    | sudo tar -xz -C /usr/local/bin trivy
fi
{%- endif %}

# Install Node deps + wire husky.
task init
