from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class TestConfig:
   SQLALCHEMY_DATABASE_URI = 'sqlite://'


db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(TestConfig)
db.init_app(app)

if False:  # not needed for this example
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'): 
        # Enable SQLite3 foreign key support so that deletes will cascade.
        #
        # This only impacts SQL executed against the connection.
        #
        # The need for this is SQLite version dependent! See
        # https://www.sqlite.org/pragma.html#pragma_foreign_keys

        from sqlalchemy import event
        from sqlalchemy.engine import Engine

        @event.listens_for(Engine, "connect")
        def _set_sqlite_pragma(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON;")
            cursor.close()
