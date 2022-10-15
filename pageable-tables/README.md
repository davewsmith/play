# Pageable Tables

Working through the details of getting pagination to behave the way I want for a project elsewhere.

Overkill, but hey.

## TO DO

  * Search that persists across page navigation, and 'reset' when the search term changes
  * Sortable fields that persist

## Setup

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

## One-time DB setup

    # FLASK_APP=tables flask db init
    # FLASK_APP=tables flask db migrate -m 'initial tables'
    FLASK_APP=tables flask db upgrade

## Running the app

    FLASK_APP=tables flask run

then hit `http://localhost:5000/populate` to populate the database.

## Notes

With Python 3.6.9, I got Flask\_SQLAlchemy 2.5.1.
The latest is 3.0.x, and the pagination API has some backward-compatible changes
(e.g., the pagination is iterable, and supports `.first` and `.last`).
