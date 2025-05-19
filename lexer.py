import ply.lex as lex

# Lista de tokens que reconoce el lexer
tokens = [
    'A_OPEN',            # <a
    'IMG_OPEN',          # <img
    'HREF',              # href
    'SRC',               # src
    'URL',               # "..."
    'TAG_CLOSE',         # >
    'TAG_SLASH_CLOSE'    # />
]

# Reglas léxicas
def t_A_OPEN(t):
    r'<[aA]\b'
    return t

def t_IMG_OPEN(t):
    r'<[iI][mM][gG]\b'
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

def t_TAG_SLASH_CLOSE(t):
    r'/>'  # etiquetas autoconclusivas
    return t

def t_TAG_CLOSE(t):
    r'>'
    return t

# Ignorar espacios, tabulaciones y saltos de línea
t_ignore = ' \t\n'

# Manejador de errores léxicos
def t_error(t):
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()
