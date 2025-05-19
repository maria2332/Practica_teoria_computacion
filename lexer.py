import ply.lex as lex

# Tokens que nos interesan
tokens = (
    'TAG_OPEN',
    'TAG_CLOSE',
    'SELF_CLOSING',
    'HREF',
    'SRC',
)

# Expresiones regulares
t_TAG_OPEN = r'<[a-zA-Z]+[^>]*?>'
t_TAG_CLOSE = r'</[a-zA-Z]+>'
t_SELF_CLOSING = r'<[a-zA-Z]+[^>]*?/>'
t_ignore = ' \t\n'

def t_HREF(t):
    r'href=["\'](.*?)["\']'
    t.value = t.value.split('=')[1].strip('"\'')
    return t

def t_SRC(t):
    r'src=["\'](.*?)["\']'
    t.value = t.value.split('=')[1].strip('"\'')
    return t

def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
