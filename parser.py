import re

# Lista de etiquetas que no necesitan cierre
VOID_TAGS = {
    'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img',
    'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'
}

def is_html_balanced(html):
    # Encuentra etiquetas de apertura y cierre
    tags = re.findall(r'<(/?)([a-zA-Z0-9]+)', html)
    
    stack = []

    for slash, tag in tags:
        tag = tag.lower()

        if tag in VOID_TAGS:
            continue  # ignorar autoconclusivas

        if not slash:  # etiqueta de apertura
            stack.append(tag)
        else:  # etiqueta de cierre
            if not stack or stack[-1] != tag:
                return False
            stack.pop()

    return len(stack) == 0
