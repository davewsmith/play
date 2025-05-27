# Dockerized Flask with Celery

A quick sketch of what the moving parts look like

## Setup

For local (non-docker) development

    python3 -m venv venv
    venv/bin/pip install -r requirements.txt

## Running 

    docker compose build
    docker compose up
    ...
    docker compose down
    ...
    docker system prune

## Running tests

Big TODO

## Making migrations

Use `docker stats` to find the name of the `dev` image, then

    docker exec -it -dev-1 /bin/bash

then, to access mounted source,

    cd /source

From here, the `flask db ...` commands are available.
Since the base of the project is mounted inside the container,
side-effects will be visible outside the container.

TODO fill me in

