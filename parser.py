import re

VOID_TAGS = {
    'area', 'base', 'br', 'col', 'embed', 'hr',
    'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'
}

def is_html_balanced(html):
    tags = re.findall(r'<(/?)([a-zA-Z0-9]+)', html)
    stack = []
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
