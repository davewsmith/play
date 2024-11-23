from flask import render_template

from app.main import bp


@bp.route('/')
def home():
    bindings = dict()
    return render_template('main/home.html', **bindings)
