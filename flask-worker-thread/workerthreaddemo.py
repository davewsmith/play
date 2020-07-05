"""
Demonstrate a simple, in process work queue for Flask apps.
"""

import queue
import threading
from time import sleep

from flask import Flask, redirect, render_template

app = Flask(__name__)
app.config['WORK_TIME'] = 3  # seconds


def worker(queue):
    while True:
        # get the next task, blocking until one is available.
        task = queue.get()

        # The app is available to the worker, but be wary of
        # using app services without locking.
        duration = app.config.get('WORK_TIME', 3)

        sleep(duration)  # simulate doing work
        print("did task {!r}".format(task))


# Give the worker thread a Queue that's shared with the app, and start
# the worker. The worker will block immediately until a route puts
# a task into the queue.
wq = queue.Queue()
worker_thread = threading.Thread(target=worker, args=(wq,))
worker_thread.start()


@app.route('/')
def index():
    return render_template('index.html', size=wq.qsize())


# Because this is a cheesy demo, a task is just a number.
# Because we're only the develoment server, there's no issue
# with muliple processes handing out identical numbers.
task = 0

@app.route('/add_task')
def add_task():
    global task
    task += 1
    print("add task {!r}".format(task))
    wq.put(task)
    return redirect('/')
