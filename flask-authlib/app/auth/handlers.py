from flask import current_app, redirect
from flask_login import login_user

from app.auth.models import User


def handle_authorize(remote, token, user_info):
    current_app.logger.info("remote: {}".format(remote))
    current_app.logger.info("token: {!r}".format(token))
    current_app.logger.info("user_info: {!r}".format(user_info))

    # Note: Here's where to do team membership or whitelist/blacklist tests

    user = User.find_by_email(user_info['email'])
    if user is None:
        user = User(user_info['preferred_username'])
        user.email = user_info['email']
        # Note: in real life we wouldn't discard the rest
        user.save()
    login_user(user)

    return redirect('/')
