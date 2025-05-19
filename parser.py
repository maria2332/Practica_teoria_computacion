import ply.yacc as yacc
from lexer import tokens

stack = []

def p_html(p):
    'html : elementos'
    if stack:
        print("❌ HTML mal balanceado. Pila final:", stack)
    else:
        print("✅ HTML bien balanceado.")

def p_elementos(p):
    '''elementos : elemento elementos
                 | '''
    pass

def p_elemento_open(p):
    'elemento : TAG_OPEN'
    tag = p[1][1:].split()[0].lower()
    stack.append(tag)

def p_elemento_close(p):
    'elemento : TAG_CLOSE'
    tag = p[1][2:-1].strip().lower()
    if not stack:
        print(f"❌ Error: cerrando {tag} sin etiqueta abierta.")
    else:
        open_tag = stack.pop()
        if open_tag != tag:
            print(f"❌ Error: cerrando {tag}, se esperaba {open_tag}.")

def p_elemento_self(p):
    'elemento : SELF_CLOSING'
    pass  # No se apilan

def p_error(p):
    print("❌ Error de sintaxis")

parser = yacc.yacc()
