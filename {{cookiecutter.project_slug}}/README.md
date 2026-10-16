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

- [mise](https://mise.jdx.dev/installing-mise.html), activated in the shell (`eval "$(mise activate zsh)"`)

All other tools are pinned in [mise.toml](mise.toml).

### Taskfile commands

For all commands see [Taskfile](Taskfile.yaml) or `task --list-all`.

## License

[MIT](LICENSE)
