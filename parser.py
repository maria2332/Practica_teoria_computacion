from lexer import lexer
import re

hrefs = []
srcs = []

# Lista de etiquetas que no requieren cierre
VOID_TAGS = { 'br', 'img', 'meta', 'hr', 'input', 'link', 'source', 'track', 'area', 'base', 'col', 'embed', 'wbr' }

def is_html_balanced(html):
    stack = []
    tags = re.findall(r'<(/?)([a-zA-Z0-9]+)', html)
    for slash, tag in tags:
        tag = tag.lower()
        if tag in VOID_TAGS:
            continue
        if not slash:
            stack.append(tag)
        else:
            if not stack or stack[-1] != tag:
                return False
            stack.pop()
    return len(stack) == 0

def parse_html(html):
    global hrefs, srcs
    hrefs, srcs = [], []
    lexer.input(html)

    last_tag = None
    last_token = None

    for tok in lexer:
        if tok.type == 'TAG_OPEN_A':
            last_tag = 'a'
        elif tok.type == 'TAG_OPEN_IMG':
            last_tag = 'img'

        elif last_token == 'HREF' and tok.type == 'URL' and last_tag == 'a':
            hrefs.append(tok.value)
            last_tag = None
        elif last_token == 'SRC' and tok.type == 'URL' and last_tag == 'img':
            srcs.append(tok.value)
            last_tag = None

        elif tok.type in ['TAG_END', 'TAG_SELFCLOSE']:
            last_tag = None

        last_token = tok.type

    return hrefs, srcs
