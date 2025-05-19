from lexer import tokens
import ply.yacc as yacc

# Pila para verificar el balanceo
stack = []

# Contadores y resultados temporales
links = []
images = []

def p_document(p):
    '''document : elements'''
    pass

def p_elements(p):
    '''elements : elements element
                | element'''
    pass

def p_element_open(p):
    '''element : TAG_OPEN
               | TAG_OPEN attributes TAG_SLASH_CLOSE
               | TAG_OPEN attributes TAG_CLOSE'''
    tag = p[1][1:].lower()
    if len(p) == 2 or p[len(p) - 1] == '/>':
        pass  # Autocierre
    else:
        stack.append(tag)

def p_element_close(p):
    'element : TAG_CLOSE'
    tag = p[1][2:-1].lower()
    if stack and stack[-1] == tag:
        stack.pop()

def p_attributes(p):
    '''attributes : attributes attribute
                  | attribute'''
    pass

def p_attribute_href(p):
    'attribute : HREF'
    if 'a' in stack:
        url = p[1].split('=', 1)[1].strip().strip('"')
        links.append(url)

def p_attribute_src(p):
    'attribute : SRC'
    if 'img' in stack:
        url = p[1].split('=', 1)[1].strip().strip('"')
        images.append(url)

def p_error(p):
    pass

parser = yacc.yacc()

def parse_html(content):
    global stack, links, images
    stack = []
    links = []
    images = []
    parser.parse(content)
    return links[:], images[:]

def is_html_balanced():
    return len(stack) == 0
