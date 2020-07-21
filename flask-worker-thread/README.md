# Flask Worker Thread Demo

## The Problem

You have a Flask app, and need to start some work while handling
a request, leaving that work running after issuing a response.

The 'right' way to do is to use a task manager like
[celery](https://docs.celeryproject.org/en/stable/) or
[rq](http://python-rq.org/), which run tasks in separate
processes. But those seem heavyweight when the need is simple.
Can't it all be done in the Flask app? Yes.

A tempting approach is to spawn off a thread while handling
the request, leaving that thread running. This is a trail
that ends in tears.

But what about starting a worker thread before starting
Flask, and have the worker thread share a queue that
request handlers can add work to? That can work.
That's what this demo does.

## Caveats

There are many. This is not a general solution.

It does work when running an app under Flask development runner,
but not with DEBUG=True. Since there's a single process, there'll
be a single queue instance. This makes examinging the queue
(say, to show how many tasks are waiting) simple.

You still take on responsibility for using approaching locking
if you're going to share resources between the worker thread
and Flask threads.
It pays here to read and reflect on the Python
[threading](https://docs.python.org/3/library/threading.html) documentation.

This will *not* run under `uwsgi`, for as-yet unknown reasons.

It does appear to work with `gunicorn`.

## Setup

On Linux (or maybe MacOS)

    virtualenv --python=python3 venv
    venv/bin/pip install -r requirements.txt

sets things up. Then

    ./rundemo

starts the flask development server.

Using the browser of your choise, visit `http://127.0.0.1:5000/`

Clicking the 'add work' link queues up a trivial task.
(Click quickly at least twice; the first tasks gets picked up from the queue right away.)
Click the link several more times, and watch the work queue size grow.
Then refresh the page every few seconds and watch the work queue size burn down
as the worker thread pretends to do work.

