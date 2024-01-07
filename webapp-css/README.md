# WebApp CSS experiments

Trying out combinations of templates and stylesheets.

To reduce the need to make duplicate changes across multiple templates or multiple stylesheets, we merge the two before viewing.

    ./merge.py template stylesheet > result.html

merges a stylesheet into a template by locating `<style></style>` in the template and inserting the contents of the stylesheet into it.

    ./mergeall

runs preconfigured merged.

