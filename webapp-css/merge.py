#!/usr/bin/env python3

import re
import sys

def merge(template_path, stylesheet_path):
    with open(template_path, 'r') as f:
        template = f.read()
    with open(stylesheet_path, 'r') as f:
        stylesheet = f.read()

    match = re.match(r'^(.*<style>)(</style>.*)$', template, re.M | re.S)
    assert match is not None, f"Couldn't find <style> in {template_path}"

    return match.group(1) + "\n" + stylesheet + match.group(2)


if __name__ == '__main__':
    assert len(sys.argv) == 3, "Expected two args"
    print(merge(sys.argv[1], sys.argv[2]), end='')
