import click

from app import create_app, celery
from app import tasks


app = create_app()


@app.cli.command(short_help="Simple celery test")
def testcelery():
    task = tasks.testcelery.delay(47, 42)
    print(repr(task))
    result = task.get()
    print(f'task -> {result}')
