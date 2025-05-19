import ply.lex as lex

# Tokens
tokens = (
    'TAG_OPEN', 'TAG_CLOSE', 'TAG_SLASH_CLOSE',
    'HREF', 'SRC', 'TEXT'
)

# Estados
states = (
    ('atag', 'exclusive'),
    ('imgtag', 'exclusive')
)

# Reglas para estado INITIAL
def t_TAG_OPEN(t):
    r'<[aA](?=\s|>)'
    t.lexer.begin('atag')
    return t

def t_TAG_OPEN_IMG(t):
    r'<[iI][mM][gG](?=\s|>)'
    t.lexer.begin('imgtag')
    return t

def t_TAG_CLOSE(t):
    r'</[a-zA-Z]+>'
    return t

def t_TAG_SLASH_CLOSE(t):
    r'/?>'
    t.lexer.begin('INITIAL')
    return t

def t_TEXT(t):
    r'[^<>]+'
    return t

t_ignore = ' \t\r\n'

def t_error(t):
    t.lexer.skip(1)

# Reglas para estado atag (extracción de href)
def t_atag_HREF(t):
    r'href\s*=\s*"[^"]+"'
    return t

def t_atag_TAG_CLOSE(t):
    r'>'
    t.lexer.begin('INITIAL')
    return t

def t_atag_TAG_SLASH_CLOSE(t):
    r'/?>'
    t.lexer.begin('INITIAL')
    return t

t_atag_ignore = ' \t\r\n'

def t_atag_error(t):
    t.lexer.skip(1)

# Reglas para estado imgtag (extracción de src)
def t_imgtag_SRC(t):
    r'src\s*=\s*"[^"]+"'
    return t

def t_imgtag_TAG_CLOSE(t):
    r'>'
    t.lexer.begin('INITIAL')
    return t

def t_imgtag_TAG_SLASH_CLOSE(t):
    r'/?>'
    t.lexer.begin('INITIAL')
    return t

t_imgtag_ignore = ' \t\r\n'

def t_imgtag_error(t):
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
