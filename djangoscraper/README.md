# DjangoScraper


This provides a context manager, `logged_in_session` that on
entry will log in to a Django site that is protected by the csrf
middleware, then log out on exit. It provides a `requests.session()`.

    from djangoscraper import logged_in_session

    with logged_in_session() as session:
        ... go wild with session

## Setup

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

Then

    cp env.template .env

and fill out `.env`
