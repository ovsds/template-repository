# Docker

Configs and commands for auxiliary services.

## Usage

### Global dependencies

- [docker](https://docs.docker.com/engine/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

### mise tasks

For all commands see [mise.toml](mise.toml) and [mise-tasks](mise-tasks) or `mise tasks ls`.

`mise run compose <args>` passes the arguments to `docker compose` over every `base-compose.yaml`;
`ENVIRONMENT=DEV` or `ENVIRONMENT=CI` adds the `dev-compose.yaml` or `ci-compose.yaml` layers.
