import ply.lex as lex

# Lista de tokens que vamos a usar
tokens = ['HREF', 'SRC', 'URL']

# Reglas simples
def t_HREF(t):
    r'href'
    return t

def t_SRC(t):
    r'src'
    return t

def t_URL(t):
    r'\"(http[s]?://[^"]+)\"'
    t.value = t.value.strip('"')
    return t

# Ignorar espacios, tabs y saltos de línea
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
