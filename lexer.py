import ply.lex as lex

tokens = (
    'TAG_OPEN_A',
    'TAG_OPEN_IMG',
    'TAG_CLOSE',
    'HREF',
    'SRC',
    'TEXT',
    'TAG_SELF_CLOSE',
)

states = (
    ('atag', 'exclusive'),
    ('imgtag', 'exclusive'),
)

# Estado inicial: detecta etiquetas <a> y <img>

def t_TAG_OPEN_A(t):
    r'<[aA](\s|>)'
    t.lexer.begin('atag')
    return t

def t_TAG_OPEN_IMG(t):
    r'<[iI][mM][gG](\s|>)'
    t.lexer.begin('imgtag')
    return t

def t_TAG_CLOSE(t):
    r'</[a-zA-Z]+>'
    return t

def t_TAG_SELF_CLOSE(t):
    r'/>'  
    return t

def t_TEXT(t):
    r'[^<>]+'
    return t

t_ignore = ' \t\r\n'

def t_error(t):
    t.lexer.skip(1)

# Estado atag para manejar href dentro de <a ...>

def t_atag_HREF(t):
    r'href\s*=\s*"[^"]*"'
    return t

def t_atag_TAG_SELF_CLOSE(t):
    r'/>'  
    t.lexer.begin('INITIAL')
    return t

def t_atag_TAG_CLOSE(t):
    r'>'
    t.lexer.begin('INITIAL')
    return t

t_atag_ignore = ' \t\r\n'

def t_atag_error(t):
    t.lexer.skip(1)

# Estado imgtag para manejar src dentro de <img ...>

def t_imgtag_SRC(t):
    r'src\s*=\s*"[^"]*"'
    return t

def t_imgtag_TAG_SELF_CLOSE(t):
    r'/>'  
    t.lexer.begin('INITIAL')
    return t

def t_imgtag_TAG_CLOSE(t):
    r'>'
    t.lexer.begin('INITIAL')
    return t

t_imgtag_ignore = ' \t\r\n'

def t_imgtag_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
