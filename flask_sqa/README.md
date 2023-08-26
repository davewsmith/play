# Flask SQLAlchemy noodling

Motivated by wanting to have something within reach to
remind myself of how to do a few things, such as getting
foreign keys with cascading deletes working in SQLite3.

## Setup

Assuming `vagrant` and `virtualbox` are installed,

    vagrant up

builds an Ubuntu 20.04 VM with a virtual environment (venv)
in `/home/vagrant/venv`

Dependencies aren't pinned; as of my last `vagrant up`, they were

    vagrant@ubuntu-focal:/vagrant$ /home/vagrant/venv/bin/pip freeze -l
    blinker==1.6.2
    click==8.1.7
    Flask==2.3.3
    Flask-SQLAlchemy==3.0.5
    Flask-Testing==0.8.1
    greenlet==2.0.2
    importlib-metadata==6.8.0
    itsdangerous==2.1.2
    Jinja2==3.1.2
    MarkupSafe==2.1.3
    pkg_resources==0.0.0
    SQLAlchemy==2.0.20
    typing_extensions==4.7.1
    Werkzeug==2.3.7
    zipp==3.16.2

## Running the code

The tests are where it's at here.

    vagrant ssh
    cd /vagrant
    ./runtests

## Notes

It looks like SQLAlchemy is enforcing ON DELETE CASCADE. With

    pragma foreign_keys=off;

the cascade still happens from code.

But when interacting directly with SQLite3, the pragma has effect.

	vagrant@ubuntu-focal:/vagrant$ sqlite3
	SQLite version 3.31.1 2020-01-27 19:55:54
	Enter ".help" for usage hints.
	Connected to a transient in-memory database.
	Use ".open FILENAME" to reopen on a persistent database.

	sqlite> .read cascade.sql
	pragma foreign_keys
	0
	many before delete of one|2
	many after delete of one|2
 
	sqlite> pragma foreign_keys=on;
	sqlite> .read cascade.sql
	pragma foreign_keys
	1
	many before delete of one|2
	many after delete of one|0
	sqlite> 

## References

  * https://docs.sqlalchemy.org/en/20/orm/cascades.html which notes deprecations and intents to
    change behavior in the future.
