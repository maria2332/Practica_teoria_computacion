import ply.lex as lex

tokens = ('TAG_OPEN', 'TAG_CLOSE', 'TAG_SLASH_CLOSE', 'HREF', 'SRC')

t_TAG_OPEN = r'<[a-zA-Z]+'
t_TAG_CLOSE = r'</[a-zA-Z]+>'
t_TAG_SLASH_CLOSE = r'/>'  # autocierre
t_ignore = ' \t\n'

def t_HREF(t):
    r'href\s*=\s*"[^"]+"'
    return t

def t_SRC(t):
    r'src\s*=\s*"[^"]+"'
    return t

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()