from datetime import datetime

from flask import redirect, render_template, url_for
from lorem import get_word

from app import db
from app.main import bp
from app.main.models import TableData


@bp.route('/')
def index():
    page = TableData.query.order_by(TableData.id.desc()).paginate(per_page=10)
    bindings = {
        'page': page,
    }
    return render_template('index.html', **bindings)


@bp.route('/populate')
def populate():
    for i in range(10):
        db.session.add(TableData(created_at=datetime.now(), data=get_word(count=3)))
    db.session.commit()
    return redirect(url_for('main.index'))
