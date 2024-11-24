import logging

from app import celery

logger = logging.getLogger(__name__)


@celery.task
def testcelery(a, b):
    return a + b


@celery.task
def testceleryfailure(_):
    raise RuntimeError('oh no!')
