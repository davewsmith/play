from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.main import bp as main_bp  # noqa
    app.register_blueprint(main_bp)

    return app 
