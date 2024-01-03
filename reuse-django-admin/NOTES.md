# Reusing Django Admin

Playing with building stuff using Admin parts

## Round 0

It is so, so nice to have a good set of notes in hand with starting off with something like this.
Thank you, past self, for leaving good notes.

After a bit of futzing, found that giving the VM 2Mb cut build time down.

    source venv/bin/activate
    django-admin startuproject adminpoc
    cd adminpoc
    ./manage.py startapp home
    ./manage.py startapp poc

Edit `adminpoc/settings.py` and add the apps

    ./manage.py migrate
    ./manage.py createsuperuser

then

    ./manage.py runserver 0.0.0.0:8000

and browse to http://localhost:8000/admin to prove that we're set up.
