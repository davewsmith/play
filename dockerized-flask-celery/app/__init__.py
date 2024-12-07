from logging.config import dictConfig

from celery import Celery
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config


db = SQLAlchemy()
migrate = Migrate()
celery = Celery(__name__)


def create_app(config_class=Config):
    dictConfig({
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'default': {
                'format': '[%(asctime)s]'
                          ' %(levelname)s'
                          ' in %(module)s.%(funcName)s:'
                          ' %(message)s',
            }
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'formatter': 'default'
            }
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['wsgi'],
            },
        }
    })

    app = Flask(__name__)
    app.config.from_object(config_class)

    celery.config_from_object(config_class)

    # Arrange for tasks to have access to the Flask app
    TaskBase = celery.Task

    class FlaskTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = FlaskTask

    db.init_app(app)

    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        from sqlalchemy import event  # noqa
        from sqlalchemy.engine import Engine  #noqa

        @event.listens_for(Engine, "connect")
        def _set_sqlite_pragma(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON;")
            cursor.close()

    migrate.init_app(app, db, render_as_batch=True)

    from app.main import bp as main_bp  # noqa
    app.register_blueprint(main_bp)

    return app
