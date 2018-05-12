# Flask Tutorial

Based on select bits of https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

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

