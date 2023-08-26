from flask_testing import TestCase

from app import db, app


class MyTests(TestCase):

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def testStub(self):
        assert True

