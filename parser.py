import re
from lexer import lexer

# Comprueba si el HTML está bien balanceado
def is_html_balanced(html):
    stack = []
    tags = re.findall(r'<(/?)([a-zA-Z0-9]+)', html)
    void_tags = {'br', 'img', 'meta', 'hr', 'input', 'link', 'source', 'track', 'area', 'base', 'col', 'embed', 'wbr'}

    for slash, tag in tags:
        tag = tag.lower()
        if tag in void_tags:
            continue
        if not slash:
            stack.append(tag)
        else:
            if not stack or stack[-1] != tag:
                return False
            stack.pop()
    return len(stack) == 0

# Extrae los enlaces e imágenes con lógica de contexto
def parse_html(html):
    hrefs = []
    srcs = []

    lexer.input(html)
    context = None
    last_token = None

    for tok in lexer:
        if tok.type == 'TAG_OPEN':
            context = tok.value  # 'a' o 'img'

        elif tok.type == 'HREF' and context == 'a':
            last_token = 'HREF'

        elif tok.type == 'SRC' and context == 'img':
            last_token = 'SRC'

        elif tok.type == 'URL':
            if last_token == 'HREF' and context == 'a':
                hrefs.append(tok.value)
                last_token = None
            elif last_token == 'SRC' and context == 'img':
                srcs.append(tok.value)
                last_token = None

        elif tok.type == 'TAG_CLOSE':
            context = None
            last_token = None

    return hrefs, srcs
