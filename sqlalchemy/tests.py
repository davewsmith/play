# from flask_testing import TestCase
from unittest import TestCase

from app import db, app


class MyTests(TestCase):

    def setUp(self):
        ...

    def tearDown(self):
        ...


    def testStub(self):
        assert True

