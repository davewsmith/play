# Flask Tutorial

Stepping through 
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
making a few changes as I go, and taking these notes.

The tutorial suggests starting with

    $ python3 -m venv venv

but on Ubuntu 14.04

    The virtual environment was not created successfully because ensurepip is not
    available.  On Debian/Ubuntu systems, you need to install the python3-venv
    package using the following command.

        apt-get install python3-venv

So
    $ virtualenv --python=python3 venv
    $ venv/bin/pip install -r requirements.txt

## Step IV notes

The migration infrastructure is created via

    FLASK_APP=tutorial.py venv/bin/flask db init

The first migration is created via

    FLASK_APP=tutorial.py venv/bin/flask db migrate -m 'users table'

And applied via

    FLASK_APP=tutorial.py venv/bin/flask db upgrade

And the second migration, after adding app.models.Note

    FLASK_APP=tutorial.py venv/bin/flask db migrate
    FLASK_APP=tutorial.py venv/bin/flask db upgrade

Starting up a db- and model-aware shell is done via

    FLASK_APP=tutorial.py venv/bin/flask shell

This lets you do some Django-shell stuff like

    >>> u = User(username='dave', email='dave@example.com')
    >>> db.session.add(u)
    >>> db.session.commit()
    >>> users = User.query.all()
    [<User dave>]
    >>>

The `shell_context_processor` in tutorial.py is what makes `db` and `User` available. Note that this mechanism can surface affordances that aren't reachable via the Web.

## Step V notes

## Step VI notes


    FLASK_APP=tutorial.py venv/bin/flask db migrate -m 'add fields to user'
    FLASK_APP=tutorial.py venv/bin/flask db upgrade

