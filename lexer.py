import ply.lex as lex # Lexer

tokens = ('TAG_OPEN', 'TAG_CLOSE', 'TAG_SLASH_CLOSE', 'HREF', 'SRC') # Tokens

t_TAG_OPEN = r'<[a-zA-Z]+' # Etiquetas de apertura
t_TAG_CLOSE = r'</[a-zA-Z]+>' # Etiquetas de cierre
t_TAG_SLASH_CLOSE = r'/>'  # autocierre
t_ignore = ' \t\n' # Ignorar espacios, tabulaciones y saltos de línea

def t_HREF(t): # Enlaces
    r'href\s*=\s*"[^"]+"' # Expresión regular para href
    return t # Devolver el token

def t_SRC(t): # Imágenes
    r'src\s*=\s*"[^"]+"' # Expresión regular para src
    return t # Devolver el token

def t_error(t): # Manejo de errores
    t.lexer.skip(1) # Ignorar el token no reconocido

lexer = lex.lex() # Crear el lexer