from flask_testing import TestCase

from app import db, app



class One(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(128))
    many = db.relationship('ManyOfOne', backref='one', cascade="all, delete")

class ManyOfOne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    one_id = db.Column(db.Integer, db.ForeignKey('one.id'))
    data = db.Column(db.String(128))
    


class OneToManyTests(TestCase):

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def testDatabaseHookup(self):
        # Smoke test the database connection
        self.assertEqual(0, One.query.count())

    def testOneToNone(self):
        self.assertEqual(0, One.query.count())
        one = One(data='one data')
        db.session.add(one)
        db.session.commit()

        self.assertEqual(1, One.query.count())
        one_retrieved = db.session.get(One, 1)
        self.assertIsNotNone(one_retrieved)
        self.assertEqual([], one_retrieved.many)

    def testOneToOne(self):
        one = One(data='one data')
        one.many.append(ManyOfOne(data='many data'))
        db.session.add(one)
        db.session.commit()

        one_retrieved = db.session.get(One, 1)
        self.assertEqual(1, len(one_retrieved.many))
        many = one_retrieved.many[0]
        self.assertEqual('many data', many.data)

    def testOneToMany(self):
        one = One(data='one')
        one.many.append(ManyOfOne(data='first'))
        one.many.append(ManyOfOne(data='second'))
        db.session.add(one)
        db.session.commit()

        self.assertEqual(2, ManyOfOne.query.count())
        one_retrieved = db.session.get(One, 1)
        self.assertEqual(2, len(one_retrieved.many))

    def testOneToManyRemovingOneOfMany(self):
        one = One(data='one')
        one.many.append(ManyOfOne(data='first'))
        one.many.append(ManyOfOne(data='second'))
        db.session.add(one)
        db.session.commit()
        self.assertEqual(2, ManyOfOne.query.count())

        one_retrieved_1 = db.session.get(One, 1)
        victim = one_retrieved_1.many[1]
        one_retrieved_1.many.remove(victim)
        db.session.commit()

        one_retrieved_2 = db.session.get(One, 1)
        self.assertEqual(1, len(one_retrieved_2.many))

        # We removed the association, but left the object
        self.assertEqual(2, ManyOfOne.query.count())
        many = db.session.get(ManyOfOne, 2)
        self.assertIsNone(many.one_id)

    def testOneToManyDeletingOneOfMany(self):
        one = One(data='one')
        one.many.append(ManyOfOne(data='first'))
        one.many.append(ManyOfOne(data='second'))
        db.session.add(one)
        db.session.commit()
        self.assertEqual(2, ManyOfOne.query.count())

        one_of_many = db.session.get(ManyOfOne, 2)
        db.session.delete(one_of_many)
        db.session.commit()
        self.assertEqual(1, ManyOfOne.query.count())

        one_retrieved = db.session.get(One, 1)
        self.assertEqual(1, len(one_retrieved.many)) 
 
    def testDeletingOneCascadesToDeleteOfMany(self):
        one = One(data='one')
        one.many.append(ManyOfOne(data='first'))
        one.many.append(ManyOfOne(data='second'))
        db.session.add(one)
        db.session.commit()
        self.assertEqual(2, ManyOfOne.query.count())

        one_retrieved = db.session.get(One, 1)
        db.session.delete(one)      
        db.session.commit()
        self.assertEqual(0, One.query.count())
        self.assertEqual(0, ManyOfOne.query.count())
