#!/usr/bin/env python
from datetime import datetime
import unittest

from app import (
    cli,
    create_app,
    db,
)
from app.models import CliMessage
from config import Config


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class DatabaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        cli.register(self.app)
        self.runner = self.app.test_cli_runner()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


class CliTestCase(DatabaseTestCase):

    def test_hi(self):
        result = self.runner.invoke(args=['hi'])
        self.assertTrue('Hi!' in result.output)
        cli_message = CliMessage.query.get(1)
        self.assertEqual('Hi!', cli_message.message)


class DbTestCases(DatabaseTestCase):

    def test_climessage(self):
        test_started_at = datetime.utcnow()
        message = 'Eels? In my hovercraft?'
        cli_message = CliMessage(message=message)
        db.session.add(cli_message)
        db.session.commit()

        self.assertEqual(1, cli_message.id)
        recovered_message = CliMessage.query.get(cli_message.id)
        self.assertEqual(message, recovered_message.message)
        self.assertTrue(recovered_message.created_at >= test_started_at)
        self.assertTrue(recovered_message.created_at <= datetime.utcnow())


class MainRoutesTestCase(DatabaseTestCase):

    def setUp(self):
       super(MainRoutesTestCase, self).setUp()
       self.client = self.app.test_client()

    def test_index(self):
        result = self.client.get('/')
        self.assertTrue(b'Hi!' in result.data)

    def test_index_with_message(self):
        db.session.add(CliMessage(message='Woot!'))
        db.session.commit()
        result = self.client.get('/')
        self.assertTrue(b'Woot!' in result.data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
