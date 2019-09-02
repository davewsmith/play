from flask import redirect, url_for
from flask_login import login_user, logout_user

from app.auth import bp
from app.auth.models import User


@bp.route('/login')
def login():
    user = User('Dave')
    user.save()
    login_user(user)
    return redirect(url_for('main.home'))

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
