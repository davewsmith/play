# Tailwind in Docker

Set up a `compose up` to run tailwindcss with --watch

The tricky bit to find was the `stdin_open: true` bit, which
either keeps tailwincss from exiting right way, or the
compose mechanism from thinking that it has.

Found that via https://github.com/rails/rails/issues/44048
