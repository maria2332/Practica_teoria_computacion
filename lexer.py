import ply.lex as lex

tokens = (
    'LT',       # <
    'GT',       # >
    'SLASH',    # /
    'EQUALS',   # =
    'NAME',     # nombres (tags, atributos)
    'STRING',   # valores entre comillas
    'TEXT',     # texto simple
)

t_LT = r'<'
t_GT = r'>'
t_SLASH = r'/'
t_EQUALS = r'='

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # eliminar comillas
    return t

def t_NAME(t):
    r'[a-zA-Z_:][a-zA-Z0-9_\-.:]*'
    return t

def t_TEXT(t):
    r'[^<>]+'
    return t

t_ignore = ' \t\n\r'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
