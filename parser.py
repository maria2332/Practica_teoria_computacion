# parser.py
import ply.yacc as yacc
from lexer import tokens

# Variables para almacenar los resultados
links = []
images = []

# Pila para balanceo de etiquetas
tag_stack = []

def p_document(p):
    '''document : elements'''
    p[0] = True  # Al final sólo importa si está balanceado

def p_elements(p):
    '''elements : element elements
                | empty'''
    # No hace nada especial

def p_element(p):
    '''element : tag_open elements tag_close
               | self_closing_tag
               | TEXT'''
    if len(p) == 4:
        # Control balanceo: comparar etiquetas apertura y cierre
        opening_tag = p[1]
        closing_tag = p[3]
        if opening_tag != closing_tag:
            raise SyntaxError(f"Tag mismatch: {opening_tag} != {closing_tag}")
    elif len(p) == 2:
        # Para self closing tags o texto no se balancea
        pass

def p_tag_open(p):
    '''tag_open : TAG_OPEN'''
    # Extraemos el nombre de la etiqueta para controlar balanceo
    tagname = p[1][1:].split()[0].lower()
    tag_stack.append(tagname)
    # Para <a ...> buscamos href
    if tagname == 'a':
        # Extraer href si está en el string
        import re
        match = re.search(r'href\s*=\s*"([^"]*)"', p[1], re.I)
        if match:
            href = match.group(1)
            links.append(href)
    p[0] = tagname

def p_tag_close(p):
    '''tag_close : TAG_CLOSE'''
    # Extraemos nombre y comparamos con pila
    tagname = p[1][2:-1].lower()
    if not tag_stack or tag_stack[-1] != tagname:
        raise SyntaxError(f"Tag mismatch or stack empty: {tagname}")
    tag_stack.pop()
    p[0] = tagname

def p_self_closing_tag(p):
    '''self_closing_tag : TAG_SELFCLOSE'''
    # Extraer nombre para buscar src solo en img
    tag_str = p[1]
    tagname = tag_str[1:].split()[0].lower()
    if tagname == 'img':
        import re
        match = re.search(r'src\s*=\s*"([^"]*)"', tag_str, re.I)
        if match:
            src = match.group(1)
            images.append(src)

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at {p.value}")
    else:
        raise SyntaxError("Syntax error at EOF")

parser = yacc.yacc()

def parse_html(data):
    global links, images, tag_stack
    links = []
    images = []
    tag_stack = []
    try:
        parser.parse(data)
        balanced = len(tag_stack) == 0
    except SyntaxError:
        balanced = False
    return links, images, balanced
