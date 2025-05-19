import ply.lex as lex

tokens = (
    'TAG_OPEN_A', 'TAG_CLOSE_A',
    'TAG_OPEN_IMG', 'TAG_SELF_CLOSE_IMG',
    'OTHER',
)

states = (
    ('atag', 'exclusive'),
    ('imgtag', 'exclusive'),
)

t_ignore = ' \t\n'

def t_TAG_OPEN_A(t):
    r'<[aA](\s|>)'
    t.lexer.begin('atag')
    t.href = None
    return t

def t_TAG_OPEN_IMG(t):
    r'<[iI][mM][gG](\s|>)'
    t.lexer.begin('imgtag')
    t.src = None
    return t

def t_TAG_CLOSE_A(t):
    r'</[aA]>'
    return t

def t_OTHER(t):
    r'<[^>]+>|[^<>]+'
    return t

# Estado atag para <a ...>

def t_atag_HREF(t):
    r'href\s*=\s*"[^"]+"'
    # Extraemos href
    href_val = t.value.split('=',1)[1].strip().strip('"')
    t.lexer.token_href = href_val
    return None  # No se devuelve token, solo guardamos href

def t_atag_TAG_CLOSE(t):
    r'>'
    # Emitimos token TAG_OPEN_A con href si lo tenemos
    t.type = 'TAG_OPEN_A'
    if hasattr(t.lexer, 'token_href'):
        t.href = t.lexer.token_href
        del t.lexer.token_href
    else:
        t.href = None
    t.lexer.begin('INITIAL')
    return t

def t_atag_ignore(t):
    r'[^>]+'
    pass

# Estado imgtag para <img ...>

def t_imgtag_SRC(t):
    r'src\s*=\s*"[^"]+"'
    src_val = t.value.split('=',1)[1].strip().strip('"')
    t.lexer.token_src = src_val
    return None

def t_imgtag_TAG_SELF_CLOSE(t):
    r'/?>'
    # Emitimos token de imagen con src si lo hay
    t.type = 'TAG_SELF_CLOSE_IMG'
    if hasattr(t.lexer, 'token_src'):
        t.src = t.lexer.token_src
        del t.lexer.token_src
    else:
        t.src = None
    t.lexer.begin('INITIAL')
    return t

def t_imgtag_ignore(t):
    r'[^>]+'
    pass

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
