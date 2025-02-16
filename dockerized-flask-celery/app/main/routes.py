import logging

from celery.result import AsyncResult
from flask import current_app, render_template
import redis

from app.main import bp
from app import celery as celery_app
from . import tasks
from .models import Job


logger = logging.getLogger(__name__)
r = redis.Redis(host='redis', port=6379, db=0)


@bp.route('/')
def home():
    logger.info("home")
    bindings = dict(
        msg=redis_keys(),
        config=repr(current_app.config),
    )
    return render_template('main/home.html', **bindings)


@bp.route('/ping')
def ping():
    logger.info("ping")
    return ""


@bp.route('/submit')
def submit():
    result = tasks.testcelery.delay(47, 29)
    bindings = dict(
        result=result,
        keys=redis_keys(),
    )
    return render_template('main/result.html', **bindings)


@bp.route('/submitfailure')
def submitfailure():
    result = tasks.testceleryfailure.delay(47)
    bindings = dict(
        result=result,
        keys=redis_keys(),
    )
    return render_template('main/result.html', **bindings)


@bp.route('/status/<task_id>')
def status(task_id):
    result = AsyncResult(task_id, app=celery_app)
    bindings = dict(
        result=result,
        keys=redis_keys(),
    )
    return render_template('main/result.html', **bindings)


def redis_keys():
    return repr(r.keys('*'))
