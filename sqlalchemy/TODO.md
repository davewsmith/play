# TODO

  * Actually instantiate SQLAlchemy and Flask.
    * use an in-memory SQLite3 database
    * configure the DB to honor foreign keys
    * N.B. This may require switching to `flask_testing.TestCase`.

  * one db.Model
    * create one row
    * prove in a test that we can query it
    * delete the row
    * prove the count is 0

  * Many-to-one
    * prove that deletes cascade

  * Many-to-many
    * Set up a 1-to-1 with deletes cascading one way
    * prove this works
