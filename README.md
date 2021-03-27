# Django app 
This is a `Docker` setup for a web application based on Django.

- The `Django` application is served by `Gunicorn` (WSGI application).
- We use `NginX` as reverse proxy and static files server. Static and media files are
  persistently stored in volumes.
- Multiple `Postgres` databases can be used. Data are persistently stored in volumes.
- `Python` dependencies are managed through `pipenv`, with `Pipfile` and `Pipfile.lock`.
- Support for multiple environment settings (variable `DJANGO_SETTINGS_MODULE` is passed
  to the `djangoapp` service).
- Tests are run using `tox`, `pytest`, and other tools such as `safety`.
- Continuous Integration is configured for `GitLab` with `.gitlab-ci.yml`.
  CI follows a Build-Test-Release flow.

Also a `Makefile` is available for convenience. You might need to use `sudo make`
instead of just `make` because `docker` and `docker-compose` commands often needs
admin privilege.

## Requirements
You need to install `Docker` and `Docker-Compose`.

## Build
`docker-compose build` or `make build`.

## Migrate databases
`docker-compose run --rm djangoapp hack/manage.py migrate` or `make migrate`.

## Collect static files
`docker-compose run --rm djangoapp hack/manage.py collectstatic --no-input'` or `make collectstatic`.

## Run
`docker-compose up` or `make run`.

## Tests
- `make checksafety`
- `make checkstyle`
- `make test`
- `make coverage`
