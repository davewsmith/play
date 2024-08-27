# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/api/01_components.ipynb.

# %% auto 0
__all__ = ['named', 'html_attrs', 'hx_attrs', 'show', 'attrmap_x', 'ft_html', 'ft_hx', 'File', 'fill_form', 'fill_dataclass',
           'find_inputs', 'html2ft', 'A', 'Abbr', 'Address', 'Area', 'Article', 'Aside', 'Audio', 'B', 'Base', 'Bdi',
           'Bdo', 'Blockquote', 'Body', 'Br', 'Button', 'Canvas', 'Caption', 'Cite', 'Code', 'Col', 'Colgroup', 'Data',
           'Datalist', 'Dd', 'Del', 'Details', 'Dfn', 'Dialog', 'Div', 'Dl', 'Dt', 'Em', 'Embed', 'Fencedframe',
           'Fieldset', 'Figcaption', 'Figure', 'Footer', 'Form', 'H1', 'Head', 'Header', 'Hgroup', 'Hr', 'Html', 'I',
           'Iframe', 'Img', 'Input', 'Ins', 'Kbd', 'Label', 'Legend', 'Li', 'Link', 'Main', 'Map', 'Mark', 'Menu',
           'Meta', 'Meter', 'Nav', 'Noscript', 'Object', 'Ol', 'Optgroup', 'Option', 'Output', 'P', 'Picture',
           'PortalExperimental', 'Pre', 'Progress', 'Q', 'Rp', 'Rt', 'Ruby', 'S', 'Samp', 'Script', 'Search', 'Section',
           'Select', 'Slot', 'Small', 'Source', 'Span', 'Strong', 'Style', 'Sub', 'Summary', 'Sup', 'Table', 'Tbody',
           'Td', 'Template', 'Textarea', 'Tfoot', 'Th', 'Thead', 'Time', 'Title', 'Tr', 'Track', 'U', 'Ul', 'Var',
           'Video', 'Wbr']

# %% ../nbs/api/01_components.ipynb
from dataclasses import dataclass, asdict, is_dataclass, make_dataclass, replace, astuple, MISSING
from bs4 import BeautifulSoup, Comment

from fastcore.utils import *
from fastcore.xml import *
from fastcore.meta import use_kwargs, delegates
from .core import fh_cfg

import types

try: from IPython import display
except ImportError: display=None

# %% ../nbs/api/01_components.ipynb
def show(ft,*rest):
    "Renders FT Components into HTML within a Jupyter notebook."
    if rest: ft = (ft,)+rest
    return display.HTML(to_xml(ft))

# %% ../nbs/api/01_components.ipynb
named = set('a button form frame iframe img input map meta object param select textarea'.split())
html_attrs = 'id cls title style accesskey contenteditable dir draggable enterkeyhint hidden inert inputmode lang popover spellcheck tabindex translate'.split()
hx_attrs = 'get post put delete patch trigger target swap include select indicator push_url confirm disable replace_url on'
hx_attrs = html_attrs + [f'hx_{o}' for o in hx_attrs.split()]

# %% ../nbs/api/01_components.ipynb
def attrmap_x(o):
    if o.startswith('_at_'): o = '@'+o[4:]
    return attrmap(o)

# %% ../nbs/api/01_components.ipynb
fh_cfg['attrmap']=attrmap_x
fh_cfg['valmap' ]=valmap

# %% ../nbs/api/01_components.ipynb
def ft_html(tag: str, *c, id=None, cls=None, title=None, style=None, attrmap=None, valmap=None, **kwargs):
    if attrmap is None: attrmap=fh_cfg.attrmap
    if valmap  is None: valmap =fh_cfg.valmap
    kwargs['id'],kwargs['cls'],kwargs['title'],kwargs['style'] = id,cls,title,style
    tag,c,kw = ft(tag, *c, attrmap=attrmap, valmap=valmap, **kwargs)
    if tag in named and 'id' in kw and 'name' not in kw: kw['name'] = kw['id']
    return FT(tag,c,kw, void_=tag in voids)

# %% ../nbs/api/01_components.ipynb
@use_kwargs(hx_attrs, keep=True)
def ft_hx(tag: str, *c, target_id=None, **kwargs):
    if target_id: kwargs['hx_target'] = '#'+target_id
    return ft_html(tag, *c, **kwargs)

# %% ../nbs/api/01_components.ipynb
_g = globals()
_all_ = [
    'A', 'Abbr', 'Address', 'Area', 'Article', 'Aside', 'Audio', 'B', 'Base', 'Bdi', 'Bdo', 'Blockquote', 'Body', 'Br',
    'Button', 'Canvas', 'Caption', 'Cite', 'Code', 'Col', 'Colgroup', 'Data', 'Datalist', 'Dd', 'Del', 'Details', 'Dfn',
    'Dialog', 'Div', 'Dl', 'Dt', 'Em', 'Embed', 'Fencedframe', 'Fieldset', 'Figcaption', 'Figure', 'Footer', 'Form',
    'H1', 'Head', 'Header', 'Hgroup', 'Hr', 'Html', 'I', 'Iframe', 'Img', 'Input', 'Ins', 'Kbd', 'Label', 'Legend', 'Li',
    'Link', 'Main', 'Map', 'Mark', 'Menu', 'Meta', 'Meter', 'Nav', 'Noscript', 'Object', 'Ol', 'Optgroup', 'Option', 'Output',
    'P', 'Picture', 'PortalExperimental', 'Pre', 'Progress', 'Q', 'Rp', 'Rt', 'Ruby', 'S', 'Samp', 'Script', 'Search',
    'Section', 'Select', 'Slot', 'Small', 'Source', 'Span', 'Strong', 'Style', 'Sub', 'Summary', 'Sup', 'Table', 'Tbody',
    'Td', 'Template', 'Textarea', 'Tfoot', 'Th', 'Thead', 'Time', 'Title', 'Tr', 'Track', 'U', 'Ul', 'Var', 'Video', 'Wbr']
for o in _all_: _g[o] = partial(ft_hx, o.lower())

# %% ../nbs/api/01_components.ipynb
def File(fname):
    "Use the unescaped text in file `fname` directly"
    return NotStr(Path(fname).read_text())

# %% ../nbs/api/01_components.ipynb
def _fill_item(item, obj):
    if not isinstance(item,list): return item
    tag,cs,attr = item
    if isinstance(cs,tuple): cs = tuple(_fill_item(o, obj) for o in cs)
    name = attr.get('name', None)
    val = None if name is None else obj.get(name, None)
    if val is not None:
        if tag=='input':
            if attr.get('type', '') in ('checkbox','radio'):
                if val: attr['checked'] = '1'
                else: attr.pop('checked', '')
            else: attr['value'] = val
        if tag=='textarea': cs=(val,)
        if tag == 'select':
            option = next((o for o in cs if o.tag=='option' and o.get('value')==val), None)
            if option: option.selected = '1'
    return FT(tag,cs,attr,void_=item.void_)

# %% ../nbs/api/01_components.ipynb
def fill_form(form:FT, obj)->FT:
    "Fills named items in `form` using attributes in `obj`"
    if is_dataclass(obj): obj = asdict(obj)
    elif not isinstance(obj,dict): obj = obj.__dict__
    return _fill_item(form, obj)

# %% ../nbs/api/01_components.ipynb
def fill_dataclass(src, dest):
    "Modifies dataclass in-place and returns it"
    for nm,val in asdict(src).items(): setattr(dest, nm, val)
    return dest

# %% ../nbs/api/01_components.ipynb
def find_inputs(e, tags='input', **kw):
    "Recursively find all elements in `e` with `tags` and attrs matching `kw`"
    if not isinstance(e, (list,tuple)): return []
    inputs = []
    if isinstance(tags,str): tags = [tags]
    elif tags is None: tags = []
    cs = e
    if isinstance(e, list):
        tag,cs,attr = e
        if e[0] in tags and kw.items()<=e[2].items(): inputs.append(e)
    for o in cs: inputs += find_inputs(o, tags, **kw)
    return inputs

# %% ../nbs/api/01_components.ipynb
def __getattr__(tag):
    if tag.startswith('_') or tag[0].islower(): raise AttributeError
    tag = tag.replace("_", "-")
    def _f(*c, target_id=None, **kwargs): return ft_hx(tag, *c, target_id=target_id, **kwargs)
    return _f

# %% ../nbs/api/01_components.ipynb
_re_h2x_attr_key = re.compile(r'^[A-Za-z_-][\w-]*$')
def html2ft(html, attr1st=False):
    """Convert HTML to an `ft` expression"""
    rev_map = {'class': 'cls', 'for': 'fr'}
    
    def _parse(elm, lvl=0, indent=4):
        if isinstance(elm, str): return repr(elm.strip()) if elm.strip() else ''
        if isinstance(elm, list): return '\n'.join(_parse(o, lvl) for o in elm)
        tag_name = elm.name.capitalize()
        if tag_name=='[document]': return _parse(list(elm.children), lvl)
        cts = elm.contents
        cs = [repr(c.strip()) if isinstance(c, str) else _parse(c, lvl+1)
              for c in cts if str(c).strip()]
        attrs = []
        for key, value in sorted(elm.attrs.items(), key=lambda x: x[0]=='class'):
            if isinstance(value,(tuple,list)): value = " ".join(value)
            key = rev_map.get(key, key)
            attrs.append(f'{key.replace("-", "_")}={value!r}'
                         if _re_h2x_attr_key.match(key) else f'**{{{key!r}:{value!r}}}')
        spc = " "*lvl*indent
        onlychild = not cts or (len(cts)==1 and isinstance(cts[0],str))
        j = ', ' if onlychild else f',\n{spc}'
        inner = j.join(filter(None, cs+attrs))
        if onlychild: return f'{tag_name}({inner})'
        if not attr1st or not attrs: return f'{tag_name}(\n{spc}{inner}\n{" "*(lvl-1)*indent})' 
        inner_cs = j.join(filter(None, cs))
        inner_attrs = ', '.join(filter(None, attrs))
        return f'{tag_name}({inner_attrs})(\n{spc}{inner_cs}\n{" "*(lvl-1)*indent})'

    soup = BeautifulSoup(html.strip(), 'html.parser')
    for c in soup.find_all(string=risinstance(Comment)): c.extract()
    return _parse(soup, 1)
