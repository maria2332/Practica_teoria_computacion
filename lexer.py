import ply.lex as lex

tokens = (
    'TAG_OPEN',
    'TAG_CLOSE',
    'SELF_CLOSING',
    'HREF',
    'SRC',
)

t_ignore = ' \t\n'

t_TAG_OPEN = r'<[a-zA-Z]+[^>/]*?>'
t_TAG_CLOSE = r'</[a-zA-Z]+>'
t_SELF_CLOSING = r'<[a-zA-Z]+[^>]*?/>'

def t_HREF(t):
    r'href=["\'](.*?)["\']'
    t.value = t.value.split('=', 1)[1].strip('"\'')
    return t

def t_SRC(t):
    r'src=["\'](.*?)["\']'
    t.value = t.value.split('=', 1)[1].strip('"\'')
    return t

def t_TEXT(t):
    r'[^<>\s"\']+'
    pass  # Ignoramos texto plano

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
