import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    # Celery configuration
    broker_url = os.getenv('BROKER_URL', None)
    broker_connection_retry_on_startup = True
    result_backend = os.getenv('RESULT_BACKEND', None)
    celery_hijack_root_logger = False
