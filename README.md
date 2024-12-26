# Cookiecutter Template for GitHub Repository

[![CI](https://github.com/ovsds/template-repository/workflows/Check%20PR/badge.svg)](https://github.com/ovsds/template-repository/actions?query=workflow%3A%22%22Check+PR%22%22)

Cookiecutter Template for GitHub Repository

## Usage

### Global dependencies

- [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)

### Basic usage

```shell
cookiecutter https://github.com/ovsds/template-repository
```

### Usage from inside already cloned repository

```shell
cookiecutter \
  --overwrite-if-exists \
  --output-dir ../ \
  https://github.com/ovsds/template-repository
```

## Development

### Global dependencies

- [Taskfile](https://taskfile.dev/installation/)
- [nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script)

### Taskfile commands

For all commands see [Taskfile](Taskfile.yaml) or `task --list-all`.

## License

[MIT](LICENSE)
