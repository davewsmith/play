# NOTES

## Round 1

Surprise. Using the `db.table('name', ...)` form, tables are specified, but only reified by the first insert.

The m2m example in the docs results in:

    CREATE TABLE [dogs] (
       [id] INTEGER PRIMARY KEY,
       [name] TEXT
    );
    CREATE TABLE [humans] (
       [id] INTEGER PRIMARY KEY,
       [name] TEXT
    );
    CREATE TABLE [dogs_humans] (
       [humans_id] INTEGER REFERENCES [humans]([id]),
       [dogs_id] INTEGER REFERENCES [dogs]([id]),
       PRIMARY KEY ([dogs_id], [humans_id])
    );

Creating the above eagerly is pretty straightforward.

Depending on access patterns, this might need additional indexes in the linking table.

Running the eager creation twice results in

    sqlite3.OperationalError: table [dogs] already exists

Checking `db.schema == ""` is a possibly overkill way of avoiding that.  `db.table["dogs"].exists()` may be cleaner.

The initial insert into `dogs_humans` produced a `last_pk` of `1`. Bug? No sign of an issue.

A duplicate insert yielded

    sqlite3.IntegrityError: UNIQUE constraint failed: dogs_humans.dogs_id, dogs_humans.humans_id

## Round 2

A bit of research later, not a bug, but perhaps a documentation issue.
The docs seem not make it clear earlier that

    >>> id(db["foo"]) == id(db["foo"])
    False

That is, each time you reach into db with the same key, you get back a _new_ value,
which retains nothing from older values other than what can be derived by introspection
on the underlying database.


## References

  * https://sqlite-utils.datasette.io/en/stable/
  * https://sqlite-utils.datasette.io/en/stable/python-api.html


