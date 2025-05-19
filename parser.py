from lexer import tokens
import ply.yacc as yacc

tags_stack = []
links = []
images = []
errors = []
current_tag = None

# Etiquetas autocerradas comunes en HTML (no requieren cierre)
self_closing_tags = {'br', 'img', 'input', 'meta', 'area', 'base', 'col', 'embed', 'hr', 'link', 'param', 'source', 'track', 'wbr'}

def p_document(p):
    'document : elements'
    # Si al final queda algo en el stack, son etiquetas abiertas sin cerrar
    if tags_stack:
        for tag in reversed(tags_stack):
            errors.append(f"Etiqueta abierta sin cerrar: <{tag}>")

def p_elements(p):
    '''elements : elements element
                | element'''
    pass

def p_element_tag_open(p):
    'element : TAG_OPEN'
    global current_tag
    tag = p[1][1:].lower()
    current_tag = tag
    if tag not in self_closing_tags:
        tags_stack.append(tag)

def p_element_tag_close(p):
    'element : TAG_CLOSE'
    tag = p[1][2:-1].lower()
    if tags_stack:
        last_tag = tags_stack[-1]
        if last_tag == tag:
            tags_stack.pop()
        else:
            errors.append(f"Cierre inesperado o incorrecto de etiqueta </{tag}> (se esperaba </{last_tag}>)")
            # Opcional: intentar sincronizar stack si quieres, aquí no lo hacemos para ser estrictos
    else:
        errors.append(f"Cierre inesperado o incorrecto de etiqueta </{tag}> (no había etiqueta abierta)")

def p_element_tag_slash_close(p):
    'element : TAG_SLASH_CLOSE'
    global current_tag
    current_tag = None

def p_element_href(p):
    'element : HREF'
    global current_tag
    if current_tag == 'a':
        url = p[1].split('=', 1)[1].strip('" ')
        links.append(url)

def p_element_src(p):
    'element : SRC'
    global current_tag
    if current_tag == 'img':
        url = p[1].split('=', 1)[1].strip('" ')
        images.append(url)

def p_error(p):
    # Aquí puedes añadir más manejo de errores si quieres
    pass

parser = yacc.yacc()

def parse_html(content):
    global tags_stack, links, images, errors, current_tag
    tags_stack = []
    links = []
    images = []
    errors = []
    current_tag = None
    parser.parse(content)
    return links[:], images[:], errors[:]

def is_html_balanced():
    return len(errors) == 0
