import markdown

text = """# Heading 1

Some words.

## Heading two

More words, followed by a list.

1. Plan A
2. Plan B

The list *pros:*

* Plans are **good**

This list has _cons:_

* It lacks a Plan C
"""

xhtml = markdown.markdown(text)
print(xhtml)

print("----------")

html5 = markdown.markdown(text, output_format='html5')
if xhtml == html5:
    print("html5 output is the same as xhtml output")
else:
    print(html5)

