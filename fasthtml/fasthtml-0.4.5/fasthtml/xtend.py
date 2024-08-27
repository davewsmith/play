# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/api/02_xtend.ipynb.

# %% auto 0
__all__ = ['A', 'Form', 'AX', 'Hidden', 'CheckboxX', 'Script', 'Style', 'double_braces', 'undouble_braces', 'loose_format',
           'ScriptX', 'replace_css_vars', 'StyleX', 'On', 'Any', 'Prev', 'Now', 'AnyNow', 'run_js', 'Titled', 'Socials',
           'Favicon', 'jsd', 'clear']

# %% ../nbs/api/02_xtend.ipynb
from dataclasses import dataclass, asdict
from typing import Any

from fastcore.utils import *
from fastcore.xtras import partial_format
from fastcore.xml import *
from fastcore.meta import use_kwargs, delegates
from .components import *

try: from IPython import display
except ImportError: display=None

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def A(*c, hx_get=None, target_id=None, hx_swap=None, href='#', **kwargs)->FT:
    "An A tag; `href` defaults to '#' for more concise use with HTMX"
    return ft_hx('a', *c, href=href, hx_get=hx_get, target_id=target_id, hx_swap=hx_swap, **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Form(*c, enctype="multipart/form-data", **kwargs)->FT:
    "A Form tag; identical to plain `ft_hx` version except default `enctype='multipart/form-data'`"
    return ft_hx('form', *c, enctype=enctype, **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def AX(txt, hx_get=None, target_id=None, hx_swap=None, href='#', **kwargs)->FT:
    "An A tag with just one text child, allowing hx_get, target_id, and hx_swap to be positional params"
    return ft_hx('a', txt, href=href, hx_get=hx_get, target_id=target_id, hx_swap=hx_swap, **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Hidden(value:Any="", id:Any=None, **kwargs)->FT:
    "An Input of type 'hidden'"
    return Input(type="hidden", value=value, id=id, **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def CheckboxX(checked:bool=False, label=None, value="1", id=None, name=None, **kwargs)->FT:
    "A Checkbox optionally inside a Label, preceded by a `Hidden` with matching name"
    if id and not name: name=id
    if not checked: checked=None
    res = Input(type="checkbox", id=id, name=name, checked=checked, value=value, **kwargs)
    if label: res = Label(res, label)
    return Hidden(name=name, skip=True, value=""), res

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_html, keep=True)
def Script(code:str="", **kwargs)->FT:
    "A Script tag that doesn't escape its code"
    return ft_html('script', NotStr(code), **kwargs)

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_html, keep=True)
def Style(*c, **kwargs)->FT:
    "A Style tag that doesn't escape its code"
    return ft_html('style', map(NotStr,c), **kwargs)

# %% ../nbs/api/02_xtend.ipynb
def double_braces(s):
    "Convert single braces to double braces if next to special chars or newline"
    s = re.sub(r'{(?=[\s:;\'"]|$)', '{{', s)
    return re.sub(r'(^|[\s:;\'"])}', r'\1}}', s)

# %% ../nbs/api/02_xtend.ipynb
def undouble_braces(s):
    "Convert double braces to single braces if next to special chars or newline"
    s = re.sub(r'\{\{(?=[\s:;\'"]|$)', '{', s)
    return re.sub(r'(^|[\s:;\'"])\}\}', r'\1}', s)

# %% ../nbs/api/02_xtend.ipynb
def loose_format(s, **kw):
    "String format `s` using `kw`, without being strict about braces outside of template params"
    if not kw: return s
    return undouble_braces(partial_format(double_braces(s), **kw)[0])

# %% ../nbs/api/02_xtend.ipynb
def ScriptX(fname, src=None, nomodule=None, type=None, _async=None, defer=None,
            charset=None, crossorigin=None, integrity=None, **kw):
    "A `script` element with contents read from `fname`"
    s = loose_format(Path(fname).read_text(), **kw)
    return Script(s, src=src, nomodule=nomodule, type=type, _async=_async, defer=defer,
                  charset=charset, crossorigin=crossorigin, integrity=integrity)

# %% ../nbs/api/02_xtend.ipynb
def replace_css_vars(css, pre='tpl', **kwargs):
    "Replace `var(--)` CSS variables with `kwargs` if name prefix matches `pre`"
    if not kwargs: return css
    def replace_var(m):
        var_name = m.group(1).replace('-', '_')
        return kwargs.get(var_name, m.group(0))
    return re.sub(fr'var\(--{pre}-([\w-]+)\)', replace_var, css)

# %% ../nbs/api/02_xtend.ipynb
def StyleX(fname, **kw):
    "A `style` element with contents read from `fname` and variables replaced from `kw`"
    s = Path(fname).read_text()
    attrs = ['type', 'media', 'scoped', 'title', 'nonce', 'integrity', 'crossorigin']
    sty_kw = {k:kw.pop(k) for k in attrs if k in kw}
    return Style(replace_css_vars(s, **kw), **sty_kw)

# %% ../nbs/api/02_xtend.ipynb
def On(code:str, event:str='click', sel:str='', me=True):
    "An async surreal.js script block event handler for `event` on selector `sel`"
    func = 'me' if me else 'any'
    if sel: sel=f'"{sel}"'
    return Script(f'{func}({sel}).on("{event}", async ev=>{{\nlet e = me(ev);\n{code}\n}});\n')

# %% ../nbs/api/02_xtend.ipynb
def Any(sel:str, code:str, event:str='click'):
    "An `any` async surreal.js script block event handler for `event` on selector `sel`"
    return On(code, event, sel=sel, me=False)

# %% ../nbs/api/02_xtend.ipynb
def Prev(code:str, event:str='click'):
    "An async surreal.js script block event handler for `event` on previous sibling"
    return On(code, event=event, sel='-')

# %% ../nbs/api/02_xtend.ipynb
def Now(code:str, sel:str=''):
    "An async surreal.js script block on selector `me(sel)`"
    if sel: sel=f'"{sel}"'
    return Script(f'(async (ee = me({sel})) => {{\nlet e = me(ee);\n{code}\n}})()\n')

# %% ../nbs/api/02_xtend.ipynb
def AnyNow(sel:str, code:str):
    "An async surreal.js script block on selector `any(sel)`"
    return Script(f'(async (e = any("{sel}")) => {{\n{code}\n}})()\n')

# %% ../nbs/api/02_xtend.ipynb
def run_js(js, id=None, **kw):
    "Run `js` script, auto-generating `id` based on name of caller if needed, and js-escaping any `kw` params"
    if not id: id = sys._getframe(1).f_code.co_name
    kw = {k:dumps(v) for k,v in kw.items()}
    return Script(js.format(**kw), id=id, hx_swap_oob='true')

# %% ../nbs/api/02_xtend.ipynb
@delegates(ft_hx, keep=True)
def Titled(title:str="FastHTML app", *args, cls="container", **kwargs)->FT:
    "An HTML partial containing a `Title`, and `H1`, and any provided children"
    return Title(title), Main(H1(title), *args, cls=cls, **kwargs)

# %% ../nbs/api/02_xtend.ipynb
def Socials(title, site_name, description, image, url=None, w=1200, h=630, twitter_site=None, creator=None, card='summary'):
    "OG and Twitter social card headers"
    if not url: url=site_name
    if not url.startswith('http'): url = f'https://{url}'
    if not image.startswith('http'): image = f'{url}{image}'
    res = [Meta(property='og:image', content=image),
        Meta(property='og:site_name', content=site_name),
        Meta(property='og:image:type', content='image/png'),
        Meta(property='og:image:width', content=w),
        Meta(property='og:image:height', content=h),
        Meta(property='og:type', content='website'),
        Meta(property='og:url', content=url),
        Meta(property='og:title', content=title),
        Meta(property='og:description', content=description),
        Meta(name='twitter:image', content=image),
        Meta(name='twitter:card', content=card),
        Meta(name='twitter:title', content=title),
        Meta(name='twitter:description', content=description)]
    if twitter_site is not None: res.append(Meta(name='twitter:site',    content=twitter_site))
    if creator      is not None: res.append(Meta(name='twitter:creator', content=creator))
    return tuple(res)

# %% ../nbs/api/02_xtend.ipynb
def Favicon(light_icon, dark_icon):
    "Light and dark favicon headers"
    return (Link(rel='icon', type='image/x-ico', href=light_icon, media='(prefers-color-scheme: light)'),
            Link(rel='icon', type='image/x-ico', href=dark_icon, media='(prefers-color-scheme: dark)'))

# %% ../nbs/api/02_xtend.ipynb
def jsd(org, repo, root, path, prov='gh', typ='script', ver=None, esm=False, **kwargs)->FT:
    "jsdelivr `Script` or CSS `Link` tag, or URL"
    ver = '@'+ver if ver else ''
    s = f'https://cdn.jsdelivr.net/{prov}/{org}/{repo}{ver}/{root}/{path}'
    if esm: s += '/+esm'
    return Script(src=s, **kwargs) if typ=='script' else Link(rel='stylesheet', href=s, **kwargs) if typ=='css' else s

# %% ../nbs/api/02_xtend.ipynb
def clear(id): return Div(hx_swap_oob='innerHTML', id=id)