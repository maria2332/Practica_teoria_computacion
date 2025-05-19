# lexer.py
import ply.lex as lex

# Lista de tokens
tokens = (
    'TAG_OPEN', 'TAG_CLOSE', 'TAG_SELFCLOSE',
    'A_HREF', 'IMG_SRC',
)

# Expresiones regulares para los tokens

def t_TAG_OPEN(t):
    r'<[a-zA-Z]+(\s[^<>]*)?>'
    if t.value.lower().startswith('<a'):
        # Buscar href
        import re
        match = re.search(r'href\s*=\s*"([^"]+)"', t.value, re.IGNORECASE)
        if match:
            t.type = 'A_HREF'
            t.value = match.group(1)
            return t
    elif t.value.lower().startswith('<img'):
        # Buscar src
        import re
        match = re.search(r'src\s*=\s*"([^"]+)"', t.value, re.IGNORECASE)
        if match:
            t.type = 'IMG_SRC'
            t.value = match.group(1)
            return t
    t.type = 'TAG_OPEN'
    return t

def t_TAG_SELFCLOSE(t):
    r'<[a-zA-Z]+(\s[^<>]*)?/>'
    return t

def t_TAG_CLOSE(t):
    r'</[a-zA-Z]+>'
    return t

# Ignorar espacios y saltos de línea
t_ignore = ' \t\n'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
