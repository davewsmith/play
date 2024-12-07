from celery.result import AsyncResult
from flask.cli import with_appcontext

from app import create_app, db, tasks
from app import celery  # noqa


app = create_app()


@app.cli.command(short_help="Create database")
@with_appcontext
def create_all():
    app.logger.info(f'calling db.create_all() on {app.config["SQLALCHEMY_DATABASE_URI"]}')
    db.create_all()


@app.cli.command(short_help="Simple celery test")
def testcelery():
    result = tasks.testcelery.delay(47, 42)
    # print(repr(result))
    # print(dir(result))
    print(f'info -> {result.info}, ready -> {result.ready()}, status -> {result.status}')
    print(f'successful -> {result.successful()}, failed -> {result.failed()}')

    task_id = result.task_id
    result = AsyncResult(task_id)
    value = result.get()
    print()

    print(f'info -> {result.info!r}, ready -> {result.ready()}, status -> {result.status}')
    print(f'sucessful -> {result.successful()}, failed -> {result.failed()}')
    print(f'value -> {value}')

    # be a good citizen
    result.forget()


@app.cli.command(short_help="Test failing task behavior")
def testceleryfailure():
    result = tasks.testceleryfailure.delay(42)

    try:
        value = result.get()  # noqa
    except Exception as e:
        print(f'raised -> {e!r}')

    print(f'info -> {result.info!r}, ready -> {result.ready()}, status -> {result.status}')
    print(f'successful -> {result.successful()}, failed -> {result.failed()}')
