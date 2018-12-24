#!/usr/bin/env python

import unittest

from app import create_app
from config import Config


class TestConfig(Config):
    pass


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
