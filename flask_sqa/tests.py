from flask_testing import TestCase

from app import db, app


class FlaskSQLAlchemyTestCase(TestCase):
    """A Flask-SQLAlchemy-aware base class for tests"""

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
