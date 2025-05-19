import ply.lex as lex

# Lista de tokens
tokens = ['A_OPEN', 'IMG_OPEN', 'HREF', 'SRC', 'URL', 'TAG_CLOSE', 'TAG_SLASH_CLOSE']

# Reglas léxicas
def t_A_OPEN(t):
    r'<[aA]'
    return t

def t_IMG_OPEN(t):
    r'<[iI][mM][gG]'
    return t

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

def t_TAG_CLOSE(t):
    r'>'
    return t

def t_TAG_SLASH_CLOSE(t):
    r'/>'  # Para <img ... />
    return t

# Ignorar espacios, tabs y saltos de línea
t_ignore = ' \t\n'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
