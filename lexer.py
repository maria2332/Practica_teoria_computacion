import ply.lex as lex

# Tokens necesarios
tokens = ['HREF', 'SRC', 'URL']

# Reglas léxicas
def t_HREF(t):
    r'href'
    return t

def t_SRC(t):
    r'src'
    return t

# Captura cualquier contenido entre comillas (no solo http)
def t_URL(t):
    r'\"([^"]+)\"'
    t.value = t.value.strip('"')
    return t

# Ignorar espacios, tabulaciones y saltos de línea
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
