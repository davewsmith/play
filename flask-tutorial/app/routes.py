from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    bindings = dict(
        title='Home',
        user=dict(
            username='Dave',
        ),
    )
    return render_template('index.html', **bindings)
