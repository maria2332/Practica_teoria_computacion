import ply.lex as lex

tokens = ['HREF', 'SRC', 'URL']

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

t_ignore = ' \t\n'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
