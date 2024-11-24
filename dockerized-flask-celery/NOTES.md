# NOTES

## Goals

  * Work up a clean way of dockerizing a Celery worker for a Flask app
  * Test what we can do with Multiprocessing or MultiThreading in the worker
  * (Optional) dockerize the Flask app

## Non-Goals

  * Making it look good (styling)
  * Hooking up a database

## TO DO

  * Dockerize the worker
  * Sort out logging (options for retrieving from a container)

## Round 1

I forget how fiddly it is to add Celery to a minimal Flask app.

Ending round one with round-tripping a request to a celery worker,
demonstrating both success and failure cases.

