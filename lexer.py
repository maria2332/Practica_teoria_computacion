import ply.lex as lex

# Definimos los tokens que nos interesan
tokens = (
    'TAG_OPEN',
    'TAG_CLOSE',
    'SELF_CLOSING',
    'HREF',
    'SRC',
    'TEXT',  # texto plano entre etiquetas, que ahora ignoramos
)

# Ignoramos espacios, tabs y saltos de línea
t_ignore = ' \t\n'

# Tokens para etiquetas
t_TAG_OPEN = r'<[a-zA-Z]+[^>/]*?>'
t_TAG_CLOSE = r'</[a-zA-Z]+>'
t_SELF_CLOSING = r'<[a-zA-Z]+[^>]*?/>'

# Token para href
def t_HREF(t):
    r'href=["\'](.*?)["\']'
    t.value = t.value.split('=', 1)[1].strip('"\'')
    return t

# Token para src
def t_SRC(t):
    r'src=["\'](.*?)["\']'
    t.value = t.value.split('=', 1)[1].strip('"\'')
    return t

# Ignorar texto entre etiquetas
def t_TEXT(t):
    r'[^<>\s"\']+'
    pass

# Manejo de errores léxicos
def t_error(t):
    # En lugar de imprimir, simplemente ignoramos cualquier carácter inesperado
    t.lexer.skip(1)

# Construimos el analizador léxico
lexer = lex.lex()
