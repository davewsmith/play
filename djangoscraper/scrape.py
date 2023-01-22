"""
A context manager for logging into a Django site that is protected by
the Django csrf middleware.

Assuming .env is set with correct values

    with logged_in_session() as session:
        ...

will provide a logged-in context that logs out on context exit.
"""

from contextlib import contextmanager
import os

import dotenv
import requests


dotenv.load_dotenv()

base_url = os.getenv('BASE_URL')
login_url = os.getenv('LOGIN_URL')
logout_url = os.getenv('LOGOUT_URL')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


@contextmanager
def logged_in_session():
    session = requests.session()
    _login(session)
    try:
        yield session
    finally:
        _logout(session)


def _login(session):
    resp = session.get(login_url)
    # print(f'GET {login_url} -> {resp.status_code}')
    assert resp.status_code == 200

    resp = session.post(
        login_url, data = {
            'username': username,
            'password': password,
        },
        headers = {
            # N.B., Django's csrf middleware requires a valid referer
            'Referer': base_url,
            # N.B., Django inserts a hidden csrfmiddlewaretoken element into a
            #  form, but will fall back on this header if the form element isn't
            #  present. So pretend it isn't present.
            'X-CSRFToken': resp.cookies['csrftoken'],
        },
    )
    # print(f'POST {login_url} -> {resp.status_code}')
    assert resp.status_code == 200


def _logout(session):
    resp = session.get(logout_url)
    # print(f'GET {logout_url} -> {resp.status_code}')
    assert resp.status_code == 200


if __name__ == '__main__':
    with logged_in_session() as session:
        resp = session.get(base_url)
        print(f'GET {base_url} -> {resp.status_code}')
