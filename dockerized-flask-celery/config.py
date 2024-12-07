import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

sqlite_fallback = 'sqlite:///' + os.path.join(basedir, 'app.db')


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', sqlite_fallback)
    # Celery configuration
    broker_url = os.getenv('BROKER_URL', None)
    broker_connection_retry_on_startup = True
    result_backend = os.getenv('RESULT_BACKEND', None)
    celery_hijack_root_logger = False
