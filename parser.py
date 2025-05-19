import ply.yacc as yacc
from lexer import tokens

# Pila para comprobar balanceo
stack = []

def p_html(p):
    'html : elementos'
    if stack:
        print("HTML mal balanceado. Pila final:", stack)
    else:
        print("HTML bien balanceado.")

def p_elementos(p):
    '''elementos : elemento elementos
                 | '''
    pass

def p_elemento_tag_open(p):
    'elemento : TAG_OPEN'
    # extrae el nombre de la etiqueta del TAG_OPEN, e.g., <div id="x"> → div
    tag = p[1][1:].split()[0].lower()
    stack.append(tag)

def p_elemento_tag_close(p):
    'elemento : TAG_CLOSE'
    # extrae el nombre de cierre: </div> → div
    tag = p[1][2:-1].strip().lower()
    if not stack:
        print(f"Error: cerrando {tag} sin corresponder.")
    else:
        open_tag = stack.pop()
        if open_tag != tag:
            print(f"Error: cerrando {tag}, pero se esperaba {open_tag}.")

def p_elemento_self_closing(p):
    'elemento : SELF_CLOSING'
    # se ignoran etiquetas autocontenidas como <img />
    pass

def p_error(p):
    print("Error de sintaxis")
