# Flask Worker Thread Demo

This demonstrates how to use a worker thread to handle long-running
tasks in a Flask app.

The question of how to do something like this keeps coming up on
StackOverflow. The 'right' answer is to use a task queue like
[celery](https://docs.celeryproject.org/en/stable/) or
[rq](http://python-rq.org/), but those require, at minumum, setting
up Redis. Could there be a simpler approach for apps that will only
be run on an intranet using the Flask development server?

Yes.

## Setup

On Linux (or maybe MacOS)

    virtualenv --python=python3 venv
    venv/bin/pip install -r requirements.txt

sets things up. Then

    ./run

starts the flask development server.

Using the browser of your choise, visit `http://127.0.0.1:5000/`

Clicking the 'enqueue work' link queues up a trivial task.
Click the link several times, and watch the queue size grow.
Then refresh the page every few seconds and watch the queue size burn down
as the worker thread pretends to do work.

## Caveats

The typical use of out-of-request tasks is to do something that will
take longer than a web user will want to wait on a page refresh for,
but which will eventually produce side-effects that are visible to the user,
say when they visit a later page. By doing work in a separate thread,
rather than a separate process, you take on responsibility for using
appropriate locking if you're accessing data structures that are shared
with the Flask app. It pays here to read and reflect on the Python
[threading](https://docs.python.org/3/library/threading.html) documentation.

As soon as you deploy multiple instances of a Flask app (e.g., behind
gunicorn or uwsgi), this approach will continue to work, but tasks will
be distributed among processes, and will no longer run sequentially.
This poses two problems: First, getting a summary of queued tasks is
more difficult. Second, tasks risk colliding on shared resources,
such as temporary files, unless you're careful to keep resources separate.
