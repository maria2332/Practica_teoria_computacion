import ply.yacc as yacc
from lexer import tokens

hrefs = []
srcs = []

def p_document(p):
    'document : elements'
    pass

def p_elements(p):
    '''elements : element elements
                | element'''
    pass

def p_element_a(p):
    'element : A_OPEN HREF URL TAG_CLOSE'
    hrefs.append(p[3])

def p_element_img(p):
    'element : IMG_OPEN SRC URL TAG_SLASH_CLOSE'
    srcs.append(p[3])

def p_error(p):
    pass

parser = yacc.yacc()

def parse_html(html):
    global hrefs, srcs
    hrefs, srcs = [], []
    parser.parse(html)
    return hrefs, srcs
