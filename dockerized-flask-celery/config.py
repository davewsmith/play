import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    # broker_url = 'redis://localhost:6379'
    # result_backend = 'redis://localhost:6379'
    # CELERY_BROKER_URL = 'redis://localhost:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    broker_url = 'redis://localhost:6379/0'
    result_backend = 'redis://localhost:6379/0'

    celery_hijack_root_logger = False
