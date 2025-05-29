# Tailwind in Docker

Proof-of-concept for setting up tailwindcss in a container,
with a (trivial, here) web development environment in another
container, both watching the same mounted source.

The tricky bit to find was the `tty: true` bit, which
either keeps tailwincss `--watch` from exiting right way. (I'll bet
if I look, tailwind is doing some sort of `isatty` check.)

O.K., I looked, and found https://github.com/tailwindlabs/tailwindcss/pull/9966 ,
which adds, but does not document, `=always` as an option to `--watch`.
This eliminates the need for `tty: true` in `compose.yaml`. Yay?
