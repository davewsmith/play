from app import db


class TableData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    data = db.Column(db.String(255))
