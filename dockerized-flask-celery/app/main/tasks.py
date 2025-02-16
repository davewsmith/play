import logging

import requests

from app import celery, db
from .models import Job


logger = logging.getLogger(__name__)


@celery.task(ignore_results=False)
def testcelery(_id):
    logger.info('testcelery')

    job = db.session.get(Job, _id)
    job.output = job.source[::-1]
    db.session.commit()

    return job.output


@celery.task(ignore_results=False)
def testceleryfailure(_):
    logger.info('testceleryfailure')

    raise RuntimeError('oh no!')
