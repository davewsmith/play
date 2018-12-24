#!/usr/bin/env python

import unittest

from app import (
    cli,
    create_app,
)
from config import Config


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class CliTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)
        cli.register(self.app)
        self.runner = self.app.test_cli_runner()

    def testHi(self):
        result = self.runner.invoke(args=['hi'])
        self.assertTrue('Hi!' in result.output)


class MainTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def testIndex(self):
        result = self.client.get('/')
        self.assertTrue(b'Hi!' in result.data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
