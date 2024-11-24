import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    # Celery configuration
    broker_url = 'redis://localhost:6379/0'
    broker_connection_retry_on_startup = True
    result_backend = 'redis://localhost:6379/0'
    celery_hijack_root_logger = False
