from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
        }

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    return app
