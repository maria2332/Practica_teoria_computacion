from lexer import tokens
import ply.yacc as yacc

tags_stack = []
links = []
images = []
current_tag = None

def p_document(p):
    'document : elements'
    pass

def p_elements(p):
    '''elements : elements element
                | element'''
    pass

def p_element_tag_open(p):
    'element : TAG_OPEN'
    global current_tag
    tag = p[1][1:].lower()
    current_tag = tag
    if tag not in ['img', 'br', 'meta', 'input']:  # autocerradas
        tags_stack.append(tag)

def p_element_tag_close(p):
    'element : TAG_CLOSE'
    tag = p[1][2:-1].lower()
    if tags_stack and tags_stack[-1] == tag:
        tags_stack.pop()

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
    pass

parser = yacc.yacc()

def parse_html(content):
    global tags_stack, links, images, current_tag
    tags_stack = []
    links = []
    images = []
    current_tag = None
    parser.parse(content)
    return links[:], images[:]

def is_html_balanced():
    return len(tags_stack) == 0
