## TODO

  * A simple form example
    - see https://stackoverflow.com/questions/70043237/how-do-we-make-a-htmx-response-trigger-a-form-reset
  * An example of triggering htmx from JS
  * An example of calling JS from htmx
  * Can htmx be made to play with a web worker?

## Round 0

Get the basic plumbing in place with one working example.

Noting from the outset that there are a few options for Flask
that add server-side htmx affordances. Not going there yet.

It'll be interesting to see how far I can get without the
server side having to know anyting about htmx. I suspect
that won't be far.

## Round 0.1

Well, yes. The Flask I pinned to has a security issue that
hasn't been backported to Python 3.6.9. And yes, that particular
problem goes away once I upgrade one of my laptops of 18.04 LTS.
For the meantime, unpin the dependency.

## Round 1

Show how to wait for something the backend is doing to finish.
