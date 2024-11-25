import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    # Celery configuration
    broker_url = os.getenv('BROKER_URL', None)
    broker_connection_retry_on_startup = True
    result_backend = os.getenv('RESULT_BACKEND', None)
    celery_hijack_root_logger = False
