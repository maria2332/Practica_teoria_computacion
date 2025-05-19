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
    tag_context = None   # 'a' o 'img'
    attr_target = None   # 'href' o 'src'
    awaiting_equals = False
    awaiting_value = False

    for tok in lexer:
        if tok.type == 'TAG_OPEN_A':
            tag_context = 'a'
        elif tok.type == 'TAG_OPEN_IMG':
            tag_context = 'img'

        elif tok.type == 'HREF' and tag_context == 'a':
            attr_target = 'href'
            awaiting_equals = True

        elif tok.type == 'SRC' and tag_context == 'img':
            attr_target = 'src'
            awaiting_equals = True

        elif tok.type == 'EQUALS' and awaiting_equals:
            awaiting_equals = False
            awaiting_value = True

        elif tok.type == 'URL' and awaiting_value:
            if attr_target == 'href':
                hrefs.append(tok.value)
            elif attr_target == 'src':
                srcs.append(tok.value)
            # reset after use
            attr_target = None
            awaiting_value = False

        elif tok.type == 'TAG_CLOSE':
            tag_context = None
            attr_target = None
            awaiting_equals = False
            awaiting_value = False

    return hrefs, srcs
