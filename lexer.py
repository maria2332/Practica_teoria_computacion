# lexer.py
import ply.lex as lex

tokens = (
    'TAG_OPEN',         # <tag>
    'TAG_CLOSE',        # </tag>
    'TAG_SELFCLOSE',    # <tag />
    'A_HREF',           # href="..."
    'IMG_SRC',          # src="..."
    'TEXT',             # texto fuera de etiquetas
)

# Expresiones regulares para tokens

t_TAG_SELFCLOSE = r'<[a-zA-Z]+(\s+[a-zA-Z]+\s*=\s*"[^"]*")*\s*/>'
t_TAG_OPEN = r'<[a-zA-Z]+(\s+[a-zA-Z]+\s*=\s*"[^"]*")*\s*>'
t_TAG_CLOSE = r'</[a-zA-Z]+>'

def t_A_HREF(t):
    r'href\s*=\s*"[^"]*"'
    return t

def t_IMG_SRC(t):
    r'src\s*=\s*"[^"]*"'
    return t

def t_TEXT(t):
    r'[^<>]+'
    return t

t_ignore = " \t\n\r"

def t_error(t):
    # Ignorar cualquier carácter ilegítimo
    t.lexer.skip(1)

lexer = lex.lex()
