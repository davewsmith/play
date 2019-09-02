from flask import current_app, redirect

def handle_authorize(remote, token, user_info):
    current_app.logger.info("remote: {}".format(remote))
    current_app.logger.info("token: {!r}".format(token))
    current_app.logger.info("user_info: {!r}".format(user_info))
    return redirect('/')
