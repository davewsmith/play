## TODO

  * Lots

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
