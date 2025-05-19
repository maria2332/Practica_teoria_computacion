import ply.lex as lex

# Solo declaramos los tokens que realmente usamos en parser.py
tokens = (
    'TAG_OPEN',
    'TAG_CLOSE',
    'SELF_CLOSING',
    # HREF y SRC se usan en main.py, no en parser, pero no los quitamos si los necesitas
    'HREF',
    'SRC',
)

# Ignorar espacios, tabs y saltos de línea
t_ignore = ' \t\n'

# Detectar etiquetas de apertura: <tag ...>
t_TAG_OPEN = r'<[a-zA-Z]+[^>/]*?>'

# Detectar etiquetas de cierre: </tag>
t_TAG_CLOSE = r'</[a-zA-Z]+>'

# Detectar etiquetas autocontenidas: <img ... />
t_SELF_CLOSING = r'<[a-zA-Z]+[^>]*?/>'

# Detectar atributos href=""
def t_HREF(t):
    r'href=["\'](.*?)["\']'
    t.value = t.value.split('=', 1)[1].strip('"\'')
    return t

# Detectar atributos src=""
def t_SRC(t):
    r'src=["\'](.*?)["\']'
    t.value = t.value.split('=', 1)[1].strip('"\'')
    return t

# Ignorar contenido textual no HTML (opcional)
def t_TEXT(t):
    r'[^<>\s"\']+'
    pass

# Manejo de errores léxicos
def t_error(t):
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()
