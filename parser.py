import re
from lexer import lexer

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

def parse_html(html):
    hrefs = []
    srcs = []

    lexer.input(html)
    last_tag = None
    last_token = None

    for tok in lexer:
        if tok.type == 'TAG_NAME':
            last_tag = tok.value

        elif last_token == 'HREF' and tok.type == 'URL' and last_tag == 'a':
            hrefs.append(tok.value)
            last_tag = None
        elif last_token == 'SRC' and tok.type == 'URL' and last_tag == 'img':
            srcs.append(tok.value)
            last_tag = None

        last_token = tok.type

    return hrefs, srcs
