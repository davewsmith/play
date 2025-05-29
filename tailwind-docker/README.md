# Tailwind in Docker

Quick proof-of-concept for setting up tailwindcss in a container,
with a (trivial, here) web development environment in another
container.

The tricky bit to find was the `tty: true` bit, which
either keeps tailwincss from exiting right way. (I'll bet
if I look its doing some sort of `isatty` check.)

Found that via https://github.com/rails/rails/issues/44048
