import ply.yacc as yacc
from lexer import tokens

stack = []

def p_html(p):
    '''html : elementos'''
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
    tag = p[1].split()[0][1:]  # extrae nombre sin "<"
    stack.append(tag)

def p_elemento_tag_close(p):
    'elemento : TAG_CLOSE'
    tag = p[1][2:-1]
    if not stack or stack[-1] != tag:
        print(f"Error: cerrando {tag} sin corresponder.")
    else:
        stack.pop()

def p_elemento_self_closing(p):
    'elemento : SELF_CLOSING'
    pass  # no necesita balanceo

def p_error(p):
    print("Error de sintaxis")

parser = yacc.yacc()
