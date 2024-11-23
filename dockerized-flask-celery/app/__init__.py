from logging.config import dictConfig

from celery import Celery
from flask import Flask

from config import Config


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

    from app.main import bp as main_bp  # noqa
    app.register_blueprint(main_bp)

    return app
