import click

from app import db
from app.models import CliMessage


def register(app):

    @app.cli.command()
    def hi():
        message = CliMessage(message="Hi!")
        db.session.add(message)
        db.session.commit()
        print("Hi!")
