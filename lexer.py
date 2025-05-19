# lexer.py
import ply.lex as lex

tokens = ['TAG_NAME', 'HREF', 'SRC', 'URL']

def t_TAG_NAME(t):
    r'<(a|img)\b'
    t.value = t.value[1:]  # elimina el símbolo '<'
    return t

def t_HREF(t):
    r'href'
    return t

def t_SRC(t):
    r'src'
    return t

def t_URL(t):
    r'"[^">]+"'
    t.value = t.value.strip('"')
    return t

t_ignore = ' \t\r\n'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()