from datetime import datetime

from app import db


class CliMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    message = db.Column(db.String(128))
