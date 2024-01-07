#!/usr/bin/env python3

from pathlib import Path
import re


def make():
    for f in Path('.').iterdir():
        if f.suffix == '.css':
            makehtml(f)

def makehtml(css_path):
    # Open the .css file name find the template
    with css_path.open() as f:
        css = f.read()
    m = re.match(r'/\* template: (\S+) \*/', css)
    assert m is not None, f"{str(css_path)} doesn't name a template"
    t = Path(m.group(1))
    assert t.exists(), f"{str(css_path)} names {str(t)}, which doesn't exist"

    with t.open() as f:
        template = f.read()

    m = re.match(r'^(.*)<!-- CSS -->.(.*)$', template, re.M | re.S)
    assert m is not None, f"{str(css_path)} doesn't have a substitution marker"
    substitute = m.group(1) + css + m.group(2)

    with open(css_path.stem + '.html', 'w') as f:
        f.write(substitute)

if __name__ == '__main__':
    make()
