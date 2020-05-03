# Zurb Foundation with Flask

Playing around with Foundation, since it doesn't require a build pipeline, and life is short.

Herein is a stock install of Zurb Foundation for Site 6.6.3 (the CSS version).

`templates/base.html` is the standard Foundation wrapper,
extended to pull in the Font Awesome icons, and modified for Flask templating.

## Setup

    virtualenv venv
    venv/bin/pip install -r requirements.txt

## Running Flask

    ./run

will start up a local Flask server, then, in your browser of choice,

    http://127.0.0.1:5001/

## References

* https://foundation.zurb.com/sites/docs/
* https://zurb.com/blog/foundation-building-blocks-over-100-compo
* https://fontawesome.com/v4.7.0/icons/
* https://fontawesome.com/v4.7.0/examples/
