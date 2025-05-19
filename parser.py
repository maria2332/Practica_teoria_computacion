import ply.yacc as yacc
from lexer import tokens

links = []
images = []
stack = []
parser_error = False

def p_document(p):
    '''document : elements'''
    pass

def p_elements_multiple(p):
    '''elements : elements element'''
    pass

def p_elements_single(p):
    '''elements : element'''
    pass

def p_element_text(p):
    '''element : TEXT'''
    pass

def p_element_open_close(p):
    '''element : open_tag elements close_tag'''
    pass

def p_element_selfclosing(p):
    '''element : self_closing_tag'''
    pass

def p_open_tag(p):
    '''open_tag : LT NAME attrs GT'''
    global stack
    tag = p[2].lower()
    attrs = p[3]
    stack.append(tag)

    # Solo contar href dentro <a>
    if tag == 'a' and 'href' in attrs:
        links.append(attrs['href'])

    # Solo contar src dentro <img>
    if tag == 'img' and 'src' in attrs:
        images.append(attrs['src'])

def p_close_tag(p):
    '''close_tag : LT SLASH NAME GT'''
    global stack, parser_error
    tag = p[3].lower()
    if stack and stack[-1] == tag:
        stack.pop()
    else:
        parser_error = True  # cierre inesperado o mal orden

def p_self_closing_tag(p):
    '''self_closing_tag : LT NAME attrs SLASH GT'''
    tag = p[2].lower()
    attrs = p[3]
    # Los self-closing no se apilan ni desapilan
    if tag == 'img' and 'src' in attrs:
        images.append(attrs['src'])

def p_attrs(p):
    '''attrs : attrs attr
             | empty'''
    if len(p) == 3:
        p[0] = p[1]
        p[0].update(p[2])
    else:
        p[0] = {}

def p_attr(p):
    '''attr : NAME EQUALS STRING'''
    p[0] = {p[1].lower(): p[3]}

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global parser_error
    parser_error = True

parser = yacc.yacc()

def parse_html(data):
    global links, images, stack, parser_error
    links = []
    images = []
    stack = []
    parser_error = False

    parser.parse(data)
    balanced = (len(stack) == 0) and (not parser_error)
    return links, images, balanced
