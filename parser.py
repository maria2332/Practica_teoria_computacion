import re
from lexer import lexer

def is_html_balanced(html):
    stack = []
    tags = re.findall(r'<(/?)([a-zA-Z0-9]+)', html)
    void_tags = {'br', 'img', 'meta', 'hr', 'input', 'link'}

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
    context = None
    expect_value = None

    for tok in lexer:
        if tok.type == 'TAG_OPEN_A':
            context = 'a'
        elif tok.type == 'TAG_OPEN_IMG':
            context = 'img'
        elif tok.type in ['TAG_CLOSE']:
            context = None
            expect_value = None
        elif tok.type == 'HREF' and context == 'a':
            expect_value = 'href'
        elif tok.type == 'SRC' and context == 'img':
            expect_value = 'src'
        elif tok.type == 'URL' and expect_value == 'href':
            hrefs.append(tok.value)
            expect_value = None
        elif tok.type == 'URL' and expect_value == 'src':
            srcs.append(tok.value)
            expect_value = None

    return hrefs, srcs
