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

### mise tasks

For all commands see [mise.toml](mise.toml) or `mise tasks ls`.
{%- if cookiecutter.scripts == 'true' or cookiecutter.services != '' or cookiecutter.with_docker == 'true' %}
`mise tasks ls --all` also lists the tasks of the sub-directory config roots, run them from the root as `mise run //<dir>:<task>`.
{%- endif %}

## License

[MIT](LICENSE)
