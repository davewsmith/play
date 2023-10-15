## TODO

  * Read up on what `hx-swap` does and doesn't guarantee
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

Well, nuts. The Flask I pinned to has a security issue that
hasn't been backported to a Flask version that supports Python 3.6.9.
And yes, that particular problem goes away once I upgrade one of my laptops of 18.04 LTS.
For the meantime, unpin the dependency.

## Round 1

A progress spinner, cribbed mostly from https://htmx.org/examples/progress-bar/

The transcription from the example required one minor change:
I'd misunderstood `hx-swap`, and thought that a stable ID on the spinner
meant that it would be left as-is during the swap, but the animation was
restarting at every swap. The fix was to hoist the spinner out
of the swap target.

Already seeing how HTMX with Flask either fills views full of HTMX fragments,
or requires templates holding fragements, which makes it harder to
reason about chains of activities.

## Interregnum 1

An initial side-trip into understanding hx-swap

Key bits:

  * [handleAjaxResponse](https://github.com/bigskysoftware/htmx/blob/htmx-2.0/src/htmx.js#L2983)
  * [getSwapSpecification](https://github.com/bigskysoftware/htmx/blob/htmx-2.0/src/htmx.js#L2307)
  * [selectAndSwap](https://github.com/bigskysoftware/htmx/blob/htmx-2.0/src/htmx.js#L1080)
  * [swap](https://github.com/bigskysoftware/htmx/blob/htmx-2.0/src/htmx.js#L1006)
  * [swapInnerHTML](https://github.com/bigskysoftware/htmx/blob/htmx-2.0/src/htmx.js#L972)

'morph' attempts to merge into the existing DOM rather than replacing bits,
but there's at least one open issue against it.

  * [swapMorph](https://github.com/bigskysoftware/htmx/blob/htmx-2.0/src/htmx.js#L985)

Looking over the open issues... A bit of a log jam on PRs, too.

