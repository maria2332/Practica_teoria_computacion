import ply.lex as lex

tokens = [
    'TAG_OPEN', 'TAG_CLOSE', 'TAG_SLASH_CLOSE',
    'A_OPEN', 'IMG_OPEN',
    'HREF_ATTR', 'SRC_ATTR',
    'URL'
]

t_TAG_OPEN = r'<'
t_TAG_CLOSE = r'>'
t_TAG_SLASH_CLOSE = r'/>'  # Para tags autoconclusivos como <img/>

def t_A_OPEN(t):
    r'[aA]'
    return t

def t_IMG_OPEN(t):
    r'[iI][mM][gG]'
    return t

def t_HREF_ATTR(t):
    r'href'
    return t

def t_SRC_ATTR(t):
    r'src'
    return t

def t_URL(t):
    r'"(http[s]?://[^"]+)"'
    t.value = t.value.strip('"')
    return t

t_ignore = ' \t\n'

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
