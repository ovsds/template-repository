#!/usr/bin/env bash
set -eo pipefail

TASK_VERSION="v3.33.1"
{%- if cookiecutter.with_cookiecutter == 'true' %}
COOKIECUTTER_VERSION="2.4.0"
{%- endif %}
{%- if cookiecutter.with_zizmor == 'true' %}
ZIZMOR_VERSION="1.0.1"
{%- endif %}
{%- if cookiecutter.with_trivy == 'true' %}
TRIVY_VERSION="v0.57.1"
{%- endif %}

# Install task (go-task). The Taskfile is the unified entry point.
if ! command -v task >/dev/null; then
  sudo sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin "${TASK_VERSION}"
fi
{%- if cookiecutter.with_cookiecutter == 'true' %}

pipx install "cookiecutter==${COOKIECUTTER_VERSION}"
{%- endif %}
{%- if cookiecutter.with_zizmor == 'true' %}

pipx install "zizmor==${ZIZMOR_VERSION}"
{%- endif %}
{%- if cookiecutter.with_trivy == 'true' %}

# Install trivy via the official install script.
if ! command -v trivy >/dev/null; then
  curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh \
    | sudo sh -s -- -b /usr/local/bin "${TRIVY_VERSION}"
fi
{%- endif %}

# Install Node deps + wire husky. Node + nvm come from the node devcontainer feature.
task init
