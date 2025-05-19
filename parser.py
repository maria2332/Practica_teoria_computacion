import ply.yacc as yacc
from lexer import tokens

# Datos para almacenar resultados

links = []
images = []
tags_stack = []

# Gramática

def p_document(p):
    '''document : elements'''
    p[0] = p[1]

def p_elements_multiple(p):
    '''elements : elements element'''
    p[0] = p[1] + [p[2]]

def p_elements_single(p):
    '''elements : element'''
    p[0] = [p[1]]

def p_element(p):
    '''element : open_tag elements close_tag
               | self_closing_tag
               | text'''
    if len(p) == 4:
        # Matched a full tag with children
        p[0] = ('element', p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_open_tag(p):
    '''open_tag : TAG_OPEN_A
                | TAG_OPEN_IMG
                | TAG_CLOSE'''
    # Return tag name normalized lowercase without <>
    tag = p[1]
    # Extract tag name between <>
    import re
    m = re.match(r'<\/?([a-zA-Z]+)', tag)
    if m:
        tagname = m.group(1).lower()
    else:
        tagname = None
    p[0] = tagname
    # Push tag to stack only if opening tag (not closing)
    if not tag.startswith('</'):
        tags_stack.append(tagname)
    else:
        # closing tag will pop in close_tag
        pass

def p_close_tag(p):
    '''close_tag : TAG_CLOSE'''
    tag = p[1]
    import re
    m = re.match(r'</([a-zA-Z]+)>', tag)
    tagname = m.group(1).lower() if m else None
    if tags_stack and tags_stack[-1] == tagname:
        tags_stack.pop()
    else:
        # unbalanced or wrong order
        p.parser.error = True
    p[0] = tagname

def p_self_closing_tag(p):
    '''self_closing_tag : TAG_OPEN_IMG SRC TAG_SELF_CLOSE'''
    # Extract src url
    src_token = p[2]
    src_value = src_token[5:-1]  # strip src="..."
    images.append(src_value)
    p[0] = ('img', src_value)

def p_element_a_with_href(p):
    '''element : TAG_OPEN_A HREF TAG_CLOSE elements TAG_CLOSE'''
    href_token = p[2]
    href_value = href_token[6:-1]  # strip href="..."
    links.append(href_value)
    p[0] = ('a', href_value, p[4])

def p_text(p):
    '''text : TEXT'''
    p[0] = p[1]

def p_error(p):
    # print("Parsing error at", p)
    pass

parser = yacc.yacc()

def parse_html(data):
    global tags_stack, links, images
    tags_stack = []
    links = []
    images = []
    parser.error = False
    parser.parse(data)
    balanced = (len(tags_stack) == 0) and (not parser.error)
    return links, images, balanced
