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
    docker compose prune
