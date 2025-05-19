import ply.yacc as yacc
from lexer import tokens

links = []
images = []
stack = []
error = False

def p_document(p):
    '''document : elements'''
    pass

def p_elements(p):
    '''elements : element elements
                | empty'''
    pass

def p_element(p):
    '''element : TAG_OPEN_A elements TAG_CLOSE_A
               | TAG_SELF_CLOSE_IMG
               | OTHER'''
    global links, images, stack, error

    tok = p.slice[1]  # Objeto token para acceder a atributos

    if tok.type == 'TAG_OPEN_A':
        stack.append('a')
        if tok.href:
            links.append(tok.href)
    elif tok.type == 'TAG_CLOSE_A':
        if stack and stack[-1] == 'a':
            stack.pop()
        else:
            global error
            error = True
    elif tok.type == 'TAG_SELF_CLOSE_IMG':
        if tok.src:
            images.append(tok.src)
    else:
        # Otros tokens ignorados
        pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    global error
    error = True

parser = yacc.yacc()

def parse_html(data):
    global links, images, stack, error
    links = []
    images = []
    stack = []
    error = False
    parser.parse(data)
    balanced = (len(stack) == 0 and error == False)
    return links, images, balanced
