import re

def is_html_balanced(html):
    stack = []
    tags = re.findall(r'</?([a-zA-Z0-9]+)[^>]*>', html)
    void_tags = {'br', 'img', 'meta', 'input', 'hr', 'link', 'area'}

    for i, tag in enumerate(tags):
        tag = tag.lower()
        if tag in void_tags:
            continue
        elif i + 1 < len(tags) and tags[i+1].lower() == tag:
            continue
        elif stack and stack[-1] == tag:
            stack.pop()
        else:
            stack.append(tag)
    return len(stack) == 0
