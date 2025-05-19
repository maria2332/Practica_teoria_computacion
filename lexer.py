import ply.lex as lex

tokens = ['A_OPEN', 'IMG_OPEN', 'HREF', 'SRC', 'URL']

def t_HREF(t):
    r'href'
    return t

def t_SRC(t):
    r'src'
    return t

def t_URL(t):
    r'\"([^"]+)\"'
    t.value = t.value.strip('"')
    return t

def t_A_OPEN(t):
    r'<a'
    return t

def t_IMG_OPEN(t):
    r'<img'
    return t

t_ignore = ' \t\n'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
