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
