# lexer.py
import ply.lex as lex

# Lista de tokens
tokens = ['TAG_OPEN_A', 'TAG_OPEN_IMG', 'HREF', 'SRC', 'URL', 'TAG_END', 'TAG_SELFCLOSE']

def t_TAG_OPEN_A(t):
    r'<a[^>]*'
    return t

def t_TAG_OPEN_IMG(t):
    r'<img[^>]*'
    return t

def t_HREF(t):
    r'href'
    return t

def t_SRC(t):
    r'src'
    return t

def t_URL(t):
    r'"([^">]+)"'
    t.value = t.value.strip('"')
    return t

def t_TAG_SELFCLOSE(t):
    r'/>'
    return t

def t_TAG_END(t):
    r'>'
    return t

t_ignore = ' \t\n'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
