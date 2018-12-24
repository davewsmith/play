import click

def register(app):

    @app.cli.command()
    def hi():
        print("Hi!")
