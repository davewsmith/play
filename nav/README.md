# A Navigation Experiment

Scratching an itch. What does it take to build a web app that lets me
plant a marker at my current location, then navigate back to that location
later? I.e., "Dude, where's my car?"

## Serving it up

Someplace running `tailscale`, do

    python3 -m http.server 5000

Then

    http://tailscale-node:5000/index.html

