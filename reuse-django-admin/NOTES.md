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

## Round 1

Here's the general approach:

  * Instead the `poc` app in front of `admin`
  * Copy `admin/index.html` from Django to `poc/templates/admin`
    so that it gets loaded instead of Admin's copy
  * Add `{% include 'poc/command_list.html' %}` to give us a place to
    add links to our commands
  * Style `command_list.html` to match the styling in `admin/app_list.html`
  * PROFIT!!!

For individual `poc` pages can `{% extend 'admin/base_site' %}` to get the
look-and-feel of admin pages.

There's some minor friction around passing some special vars into such pages
so that the full header appears and acts like the Admin index header.

**TBD:**

  * Breadcrumbs
  * Special icons for our custom commands as they appear in the Admin index

