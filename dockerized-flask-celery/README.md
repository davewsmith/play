# Dockerized Flask with Celery

A quick sketch of what the moving parts look like

## Setup

For local (non-docker) development

    python3 -m venv venv
    venv/bin/pip install -r requirements.txt

## Running a local test

In separate terminals

    sudo docker run -p 6379:6379 redis:7-alpine

    ./runworkers

then in another terminal

    FLASK_APP=server.py venv/bin/flask testcelery

    FLASK_APP=server.py venv/bin/flask testceleryfailure

