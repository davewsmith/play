# WebApp CSS experiments

Each `*.css` file is expected to include a comment naming an HTML template.
E.g.,

    /* simple.template */
    .body { color: salmonl }

Each such template is expected to include

    <style>
    <!-- CSS -->
    </style>

Running

    ./build.py

opens each `.css` file, extracts the template name and reads the corresponding file, replaces the comment in the template with the contents of the `.css` file, then writes the result to file named by replaceing `.css` with `.html`.

This lets us try out a large number of styles against a small number of templates, without having to duplicate changes across files.
