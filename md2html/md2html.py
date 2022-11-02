#! venv/bin/python

from pathlib import Path
import sys

from jinja2 import Environment, FileSystemLoader
from markdown import Markdown


MARKDOWN_EXTENSIONS = [
    'tables',
    'fenced_code',
    'smarty',
]

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=False,
    keep_trailing_newline=True,
)


def convert(source, target):
    body = source.read_text(encoding='utf-8')

    md = Markdown(extensions=MARKDOWN_EXTENSIONS)
    html_fragment = md.convert(body)

    template = env.get_template('template.html')
    html = template.render(title=source.stem, body=html_fragment)

    target.write_text(html, encoding='utf-8')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: md2html input.md output.html")
        sys.exit(1)

    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    convert(source, target)
