# NOTES

## Goals

  * Work up a clean way of dockerizing a Celery worker for a Flask app
  * Test what we can do with Multiprocessing or MultiThreading in the worker
  * (Optional) dockerize the Flask app

## Non-Goals

  * Making it look good (styling)
  * Hooking up a database

## TO DO

  * Sort out logging (options for retrieving from a container)
  * Why am I not getting app-level logging from celery workers?
  * Configure to use a non-root user

## Round 1

I forget how fiddly it is to add Celery to a minimal Flask app.

Ending round one with round-tripping a request to a celery worker,
demonstrating both success and failure cases.

## Round 2

Got the celery worker to start up in a container, but it couldn't
connect to Redis. Aha! First time I've needed to confiure
docker networking by hand! (`docker compose` would be an option,
except I want to see the logs from the worker in real time.
I guess `docker logs --follow` will do that, but it's an extra
step.) I'll manual up. It'll build character.

## Round 3

Based on reading the docs, what _should_ work is something like

    docker buildx build --tag worker .

After arranging for the `.env` to reflect `redis` as the redis host.
Then

    docker network create demo-net
    docker run --name redis --network demo-net -p 6379:6379 redis:7-alpine
    docker run --network demo-net worker

This should let me inject work in from outside of `demo-net`.
Or, work out the switch that lets me use the same image for
both app and worker. Choices.

After a bit of futzing, that worked. Yay! I can delay a task to celery
from outside of the docker world, then get a response from a worker
inside the docker world. The desired path is paved.

## Round 4

So, `docker compose`, which has changed sligtly since `docker-compose` days.

Got `docker compuse up` minimally working (the flask app presents on localhost:5000).
There's a complaint from the worker that it shouldn't be run as root. Fixing that later.

Fought with celery for a few hours sorting out why it thought there was no backend
configured when I went to retreive the status for a task. A bit of searching turned
up others having the problem, then eventualy the hint that when reconsituting a
`celery.result.AsyncResult` from a `task_id`, one has to also set `app`. Not sure
why I didn't get bit by this earlier.
