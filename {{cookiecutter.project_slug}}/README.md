# {{cookiecutter.project_name}}

[![CI](https://github.com/{{cookiecutter.owner_github_login}}/{{cookiecutter.project_slug}}/workflows/Check%20PR/badge.svg)](https://github.com/{{cookiecutter.owner_github_login}}/{{cookiecutter.project_slug}}/actions?query=workflow%3A%22%22Check+PR%22%22)

{{ cookiecutter.project_name }}

## Usage
{%- if cookiecutter.with_cookiecutter == 'true' %}

### Global dependencies

- [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)

### Basic usage

```shell
cookiecutter https://github.com/{{ cookiecutter.owner_github_login }}/{{ cookiecutter.project_slug }}
```
{%- endif %}

## Development

### Devcontainer (recommended)

The repo ships with a [devcontainer](.devcontainer/devcontainer.json) that bundles `task`, the pinned Node version (via nvm){%- if cookiecutter.with_python == 'true' %}, Python{%- endif %}{%- if cookiecutter.with_cookiecutter == 'true' %}, `cookiecutter`{%- endif %}{%- if cookiecutter.with_zizmor == 'true' %}, `zizmor`{%- endif %}{%- if cookiecutter.with_trivy == 'true' %}, `trivy`{%- endif %}. Both human IDEs and headless agents share the same definition.

- **VSCode / Cursor / JetBrains:** open the folder; "Reopen in Container" / "Open Dev Container".
- **CLI / headless:** with the [`devcontainer` CLI](https://github.com/devcontainers/cli):
  ```shell
  devcontainer up --workspace-folder .
  devcontainer exec --workspace-folder . task --list-all
  ```

All `task` targets work inside the container — no host toolchain required. First boot runs [`setup.sh`](.devcontainer/setup.sh) which installs the toolchain and runs `task init`.

### Without devcontainer

Global dependencies:

- [Taskfile](https://taskfile.dev/installation/)
- [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)
{%- if cookiecutter.with_zizmor == 'true' %}
- [zizmor](https://woodruffw.github.io/zizmor/installation/) - used for GHA security scanning
{%- endif %}

### Taskfile commands

For all commands see [Taskfile](Taskfile.yaml) or `task --list-all`.

## License

[MIT](LICENSE)
