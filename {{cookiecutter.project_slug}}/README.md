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

### Global dependencies

- [Taskfile](https://taskfile.dev/installation/)
- [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)
{%- if cookiecutter.with_zizmor == 'true' %}
- [zizmor](https://woodruffw.github.io/zizmor/installation/) - used for GHA security scanning
{%- endif %}

### Taskfile commands

For all commands see [Taskfile](Taskfile.yaml) or `task --list-all`.

## License

[MIT](LICENSE)
