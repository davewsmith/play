# https://docs.fastht.ml/

from fasthtml.common import *

app,rt = fast_app(
    hdrs=[Style(':root { --pico-font-size: 120%; }')])

@rt('/')
def get():
    return (
        Title('Demo'),
        Main(
            Div(
                P('Hello World!'),
                P('Good to see you'),
                hx_get="/change",
           ),
           cls='container',
        ),
    )

@rt('/change')
def get():
    return P('Nice to be here!')

serve()
