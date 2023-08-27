"""
Test a way of hooking up the before_delete event
"""

from app import db
from tests import FlaskSQLAlchemyTestCase


class Thing(db.Model):
    """A thing that might hold an external resource"""
    id = db.Column(db.Integer, primary_key=True)

capture = {}

from sqlalchemy import event
@event.listens_for(Thing, 'before_delete')
def thing_before_delete(mapper, connection, target):
    capture['deleted'].append(target.id)
    # In real life we might fire of an async task to do cleanup


class EventTest(FlaskSQLAlchemyTestCase):

    def setUp(this):
        capture['deleted'] = []
        super().setUp()

    def testBeforeDeleteEvent(self):
        self.assertEqual([], capture['deleted'])

        thing = Thing()
        db.session.add(thing)
        db.session.commit()

        thing_id = thing.id

        db.session.delete(thing)
        db.session.commit()
        self.assertEqual([thing_id], capture['deleted'])
