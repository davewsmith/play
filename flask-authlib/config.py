import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'top sekret')
    # Let Authlib use  http: for localhost work
    AUTHLIB_INSECURE_TRANSPORT = 1
    GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET')
    # TODO: Sort out why using this causes github to refuse to Authenticate
    # GITHUB_AUTHORIZE_URL = os.environ.get('GITHUB_AUTHORIZE_URL')
