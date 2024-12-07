from app import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(128))
    output = db.Column(db.String(128))
