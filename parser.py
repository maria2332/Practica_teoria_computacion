from lexer import lexer, tokens
import ply.yacc as yacc

# -------------------------
# Parsing para balanceo
# -------------------------

stack = []

# Reglas gramaticales simplificadas para chequear el balanceo de etiquetas

def p_document(p):
    '''document : elements'''
    p[0] = p[1]

def p_elements_multiple(p):
    '''elements : elements element'''
    p[0] = p[1] + p[2]

def p_elements_single(p):
    '''elements : element'''
    p[0] = p[1]

def p_element_tag(p):
    '''element : TAG_OPEN elements TAG_CLOSE'''
    opening_tag = p[1][1:-1].strip().lower()
    closing_tag = p[3][2:-1].strip().lower()
    p[0] = [opening_tag == closing_tag]

def p_element_selfclosing(p):
    '''element : TAG_SLASH_CLOSE'''
    p[0] = [True]

def p_element_text(p):
    '''element : TEXT'''
    p[0] = [True]

def p_error(p):
    pass

parser = yacc.yacc()

def is_html_balanced(data):
    try:
        result = parser.parse(data, lexer=lexer)
        return all(result)
    except:
        return False

# -------------------------
# Extracción de enlaces e imágenes
# -------------------------

def parse_html(data):
    lexer.input(data)
    links = []
    images = []

    current_tag = None

    for tok in lexer:
        if tok.type == 'TAG_OPEN':
            current_tag = 'a'
        elif tok.type == 'TAG_OPEN_IMG':
            current_tag = 'img'
        elif tok.type == 'HREF' and current_tag == 'a':
            url = tok.value.split('=', 1)[1].strip().strip('"')
            links.append(url)
        elif tok.type == 'SRC' and current_tag == 'img':
            url = tok.value.split('=', 1)[1].strip().strip('"')
            images.append(url)
        elif tok.type in ('TAG_CLOSE', 'TAG_SLASH_CLOSE'):
            current_tag = None

    return links, images
