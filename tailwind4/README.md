# Playing with Tailwind CSS 4

## Setup (YMMV)

    curl -L https://github.com/tailwindlabs/tailwindcss/releases/download/v4.0.14/tailwindcss-linux-x64 -o ~/bin/tailwindcss
    chmod +x ~/bin/tailwindcss

## To run an experiment

    mkdir experiment
    cd experiment
    cp ../index.html .
    cp ../tailwind.css .
    tailwindcss -i tailwind.css -o style.css --watch

(Ignore any `watchman` error. See https://github.com/tailwindlabs/tailwindcss/discussions/16011)

Then edit away. style.css will be generated on save.
