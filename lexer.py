import ply.lex as lex

tokens = [
    'TAG_OPEN_A', 'TAG_OPEN_IMG', 'TAG_CLOSE',
    'HREF', 'SRC', 'EQUALS', 'URL', 'IDENTIFIER'
]

def t_TAG_OPEN_A(t):
    r'<\s*a\b'
    return t

def t_TAG_OPEN_IMG(t):
    r'<\s*img\b'
    return t

def t_TAG_CLOSE(t):
    r'/?>'
    return t

def t_HREF(t):
    r'href'
    return t

def t_SRC(t):
    r'src'
    return t

def t_EQUALS(t):
    r'='
    return t

def t_URL(t):
    r'"[^"]*"'
    t.value = t.value.strip('"')
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_:][a-zA-Z0-9_\-:.]*'
    return t

t_ignore = ' \t\r\n'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
