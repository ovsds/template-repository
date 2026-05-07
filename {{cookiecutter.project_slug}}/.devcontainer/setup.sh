#!/usr/bin/env bash
set -eo pipefail
{%- if cookiecutter.with_zizmor == 'true' %}

pipx install "zizmor==1.0.1"
{%- endif %}

# Install Node deps + wire husky.
task init
