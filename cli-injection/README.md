# Needs a Good Name

Sourdough starter for projects that do things on some schedule, and present some sort of web UI for the results.

This scratches the itch of needing a starting point for Pi projects that don't need tasks queue (i.e., requiring celery, redis, and maybe RabbitMQ). Instead, do the long-running thing via a separate command-line process that can write into a shared database.

Projects that need to spawn work from web requests need not apply.

## Setup

    virtualenv --python=python3 venv
    venv/bin/pip install --upgrade pip  # optional
    venv/bin/pip install -r requirements.txt

## Before running it

The first time (to create the initial database), or whenever there are pending migrations:

    FLASK_APP=runner.py flask db upgrade

## Running it

    FLASK_APP=runner.py flask run

## Running the tests

    venv/bin/python tests.py

## DONE

* Print "Hi!" from a web page
* Print "Hi!" from the CLI (``FLASK_APP=runner.py flask hi``)
* Test case for "Hi!" from web page
* Test case for "Hi!" from the CLI
* Added basic SQLAlchemy support (using SQLite3)
* Add CliMessage model and a test of it
* CLI persists a CliMessage (with test)
* Display CliMessages through the web (with tests). This one required adding migration support.

## TO DO

* Vagrantfile VM
* provision redis in the VM
* Dockerize

## MAYBE

* Prettier date formatting

