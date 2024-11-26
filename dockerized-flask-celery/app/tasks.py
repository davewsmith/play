import logging

import requests

from app import celery


logger = logging.getLogger(__name__)


@celery.task(ignore_results=False)
def testcelery(a, b):
    logger.info('testcelery')
    _ = requests.get('http://web:5000/ping')
    return a + b


@celery.task(ignore_results=False)
def testceleryfailure(_):
    logger.info('testceleryfailure')
    raise RuntimeError('oh no!')
