from lexer import tokens # Importar los tokens del lexer
import ply.yacc as yacc # Importar el parser

tags_stack = [] # Pila para manejar etiquetas abiertas
links = [] # Lista para almacenar enlaces
images = [] # Lista para almacenar imágenes
errors = [] # Lista para almacenar errores
current_tag = None # Variable para almacenar la etiqueta actual

# Etiquetas autocerradas comunes en HTML (no requieren cierre)
self_closing_tags = {'br', 'img', 'input', 'meta', 'area', 'base', 'col', 'embed', 'hr', 'link', 'param', 'source', 'track', 'wbr'}

def p_document(p): # Función para manejar el documento HTML
    'document : elements' 
    # Si al final queda algo en el stack, son etiquetas abiertas sin cerrar
    if tags_stack:
        for tag in reversed(tags_stack):
            errors.append(f"Etiqueta abierta sin cerrar: <{tag}>") # Error de etiqueta abierta

def p_elements(p): # Función para manejar los elementos HTML
    '''elements : elements element
                | element'''
    pass

def p_element_tag_open(p): # Función para manejar etiquetas de apertura
    'element : TAG_OPEN' 
    global current_tag  # Variable global para la etiqueta actual
    tag = p[1][1:].lower() # Convertir a minúsculas
    current_tag = tag # Actualizar la etiqueta actual
    if tag not in self_closing_tags: # Si no es una etiqueta autocerrada
        tags_stack.append(tag) # Añadir etiqueta a la pila

def p_element_tag_close(p): # Función para manejar etiquetas de cierre
    'element : TAG_CLOSE' 
    tag = p[1][2:-1].lower() # Convertir a minúsculas
    if tags_stack: # Si hay etiquetas abiertas
        last_tag = tags_stack[-1] # Obtener la última etiqueta abierta
        if last_tag == tag: # Si coincide con la etiqueta cerrada
            tags_stack.pop() # Cerrar etiqueta
        else: # Si no coincide
            errors.append(f"Cierre inesperado o incorrecto de etiqueta </{tag}> (se esperaba </{last_tag}>)") # Error de cierre inesperado
            # Opcional: intentar sincronizar stack si quieres, aquí no lo hacemos para ser estrictos
    else: # Si no hay etiquetas abiertas
        errors.append(f"Cierre inesperado o incorrecto de etiqueta </{tag}> (no había etiqueta abierta)") # Error de cierre inesperado

def p_element_tag_slash_close(p): # Función para manejar etiquetas autocerradas
    'element : TAG_SLASH_CLOSE'
    global current_tag # Variable global para la etiqueta actual
    current_tag = None # No se añade a la pila porque es autocerrada

def p_element_href(p): # Función para manejar enlaces
    'element : HREF'
    global current_tag # Variable global para la etiqueta actual
    if current_tag == 'a': # Si la etiqueta actual es un enlace
        url = p[1].split('=', 1)[1].strip('" ') # Obtener la URL
        links.append(url) # Añadir a la lista de enlaces

def p_element_src(p): # Función para manejar imágenes
    'element : SRC'
    global current_tag # Variable global para la etiqueta actual
    if current_tag == 'img': # Si la etiqueta actual es una imagen
        url = p[1].split('=', 1)[1].strip('" ') # Obtener la URL
        images.append(url) # Añadir a la lista de imágenes

def p_error(p): # Manejo de errores
    # Aquí puedes añadir más manejo de errores si quieres
    pass

parser = yacc.yacc() # Crear el parser

def parse_html(content): # Función para analizar el contenido HTML
    global tags_stack, links, images, errors, current_tag # Reiniciar variables globales
    tags_stack = [] # Pila para manejar etiquetas abiertas
    links = [] # Lista para almacenar enlaces
    images = [] # Lista para almacenar imágenes
    errors = [] # Lista para almacenar errores
    current_tag = None # Variable para almacenar la etiqueta actual
    parser.parse(content) # Analizar el contenido HTML
    return links[:], images[:], errors[:] # Devolver listas de enlaces, imágenes y errores

def is_html_balanced(): # Función para verificar si el HTML está balanceado
    return len(errors) == 0 # Si no hay errores, está balanceado