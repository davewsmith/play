from flask import (
    render_template,
)

from app.main import bp
from app.models import CliMessage


@bp.route('/')
def index():
    messages = CliMessage.query.all()
    return render_template("index.html", messages=messages)
    
