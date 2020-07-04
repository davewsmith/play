# Flask Worker Thread Demo

This demonstrates how to do long-running tasks in process in a Flask app,
using a worker thread.

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

Clicking the 'enqueue work' link queues up a fake task.
Click the link several times, and watch the queue size grow.
Then refresh the page every few seconds and watch the queue size burn down.

## Caveats

The typical use of out-of-request tasks is to do something that will
take longer than a web user will want to wait on a page refresh for,
but which will eventually produce side-effects that are visible to the user,
say when they visit a later page. By doing work in a separate thread,
rather than a separate process, you take on responsibility for using
appropriate locking if you're accessing data structures that are shared
with the Flask app. It pays here to read and reflect on the Python
[threading](https://docs.python.org/3/library/threading.html) documentation.


