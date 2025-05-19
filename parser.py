import ply.yacc as yacc
from lexer import tokens

# Pila para verificar el balanceo de etiquetas
stack = []

# Reglas de la gramática
def p_document(p):
    """
    document : elements
    """
    pass

def p_elements(p):
    """
    elements : elements element
             | element
    """
    pass

def p_element_open(p):
    """
    element : OPEN_TAG
    """
    tag = p[1][1:-1].split()[0]  # Obtener el nombre de la etiqueta
    stack.append(tag)

def p_element_close(p):
    """
    element : CLOSE_TAG
    """
    tag = p[1][2:-1]
    if stack and stack[-1] == tag:
        stack.pop()
    else:
        # Marca error en el balanceo
        stack.append("#MISMATCH#")

def p_element_selfclosing(p):
    """
    element : SELF_CLOSING_TAG
    """
    # Etiqueta autocontenida, no afecta al balanceo
    pass

def p_element_text(p):
    """
    element : TEXT
    """
    pass

def p_error(p):
    pass

# Crear parser
parser = yacc.yacc()

def is_html_balanced(html):
    global stack
    stack = []  # Reiniciar pila
    parser.parse(html)
    return not stack or all(tag != "#MISMATCH#" for tag in stack) == True
