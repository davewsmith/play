# Needs a Good Name

Sourdough starter for Pi projects that do things on some schedule, and present some sort of web UI for the results.

## Setup

    virtualenv --python=python3 venv
    venv/bin/pip install --upgrade pip
    venv/bin/pip install -r requirements.txt

## Run

    FLASK_APP=runner.py flask run

## Run tests

    venv/bin/python tests.py

## DONE

* Print "Hi!" from a web page
* Print "Hi!" from the CLI (``FLASK_APP=runner.py flask hi``)
* Test case for "Hi!" from web page

## TO DO

* Add somethings to a persistent store through the CLI
* Prove the same in a test
* Display the thing through the Web, with a test

