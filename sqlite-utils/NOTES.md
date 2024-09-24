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

## References

  * https://sqlite-utils.datasette.io/en/stable/
  * https://sqlite-utils.datasette.io/en/stable/python-api.html


