from flask import current_app, render_template

from app.main import bp


@bp.route('/')
def home():
    return render_template("index.html")

@bp.route('/debug')
def debug():
    bindings = dict(
        rules=url_map_rules(),
    )
    return render_template("debug.html", **bindings)

def url_map_rules():
    return ["Rule('{}', endpoint='{}')".format(rule, rule.endpoint) for rule in current_app.url_map.iter_rules()]
