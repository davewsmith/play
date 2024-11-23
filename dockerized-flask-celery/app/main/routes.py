import logging

from flask import render_template

from app.main import bp


logger = logging.getLogger(__name__)


@bp.route('/')
def home():
    logger.info("home")
    bindings = dict()
    return render_template('main/home.html', **bindings)
