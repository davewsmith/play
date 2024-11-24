# Dockerized Flask with Celery

A quick sketch of what the moving parts look like

## Setup

For local (non-docker) development

    python3 -m venv venv
    venv/bin/pip install -r requirements.txt

## Running 

Build the worker image

    sudo docker buildx build --tag worker .

Create the docker network if it isn't already there

    sudo docker network create demo

Then separate terminals

    sudo docker run --name redis --network demo -p 6379:6379 redis:7-alpine

    sudo docker run --name worker --network demo worker

Then in another terminal

    FLASK_APP=server.py venv/bin/flask testcelery

    FLASK_APP=server.py venv/bin/flask testceleryfailure

