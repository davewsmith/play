from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class TestConfig:
   SQLALCHEMY_DATABASE_URI = 'sqlite://'


db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(TestConfig)
db.init_app(app)

# Enable foreign key support so that deletes will cascade
from sqlalchemy import event
from sqlalchemy.engine import Engine

@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()

