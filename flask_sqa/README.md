# Flask SQLAlchemy noodling

Motivated by wanting to have something within reach to
remind myself of how to do a few things, such as getting
foreign keys with cascading deletes working in SQLite3.

## Setup

Assuming `vagrant` and `virtualbox` are installed,

    vagrant up

builds an Ubuntu 20.04 VM

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

