"""
Demonstrate a simple, in process work queue for Flask apps.

This works in the development server, but not that as soon as you
go multi-process (by using gunicorn or uwsgi), you'll have a worker
thread per-process. That may or may not be what you want.
"""

import queue
import threading
from time import sleep

from flask import Flask, redirect, render_template

def worker(queue):
    # Note that we don't, in this example, have access to the Flask app.
    while True:
        task = queue.get()
        sleep(3)  # simulate doing work
        print("did task {!r}".format(task))

wq = queue.Queue()
worker_thread = threading.Thread(target=worker, args=(wq,))
worker_thread.start()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', size=wq.qsize())

task = 0

@app.route('/enqueue')
def enqueue():
    global task
    task += 1
    print("enqueue task {!r}".format(task))
    wq.put(task)
    return redirect('/')
