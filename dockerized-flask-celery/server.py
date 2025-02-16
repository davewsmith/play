from celery.result import AsyncResult
from flask.cli import with_appcontext

from app import create_app, db
from app import celery  # noqa
from app.main import tasks


app = create_app()


@app.cli.command(short_help="Create database")
@with_appcontext
def create_all():
    app.logger.info(f'calling db.create_all() on {app.config["SQLALCHEMY_DATABASE_URI"]}')
    db.create_all()
