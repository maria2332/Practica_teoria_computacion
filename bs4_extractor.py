import requests # Importar requests para realizar solicitudes HTTP
from bs4 import BeautifulSoup # Importar BeautifulSoup para analizar HTML
import os # Importar os para manejar rutas de archivos

# Etiquetas a analizar
ETIQUETAS_ESTADISTICAS = ['a', 'img', 'br', 'div', 'li', 'ul', 'p', 'span', 'table', 'td', 'tr'] # Lista de etiquetas para estadísticas

def analizar_html(contenido_html): 
    """Analiza el HTML con BeautifulSoup y devuelve enlaces, imágenes y estadísticas de etiquetas."""
    soup = BeautifulSoup(contenido_html, 'html.parser') # Crear objeto BeautifulSoup

    # Extraer URLs de enlaces <a href="">
    enlaces = [] # Lista para almacenar enlaces
    for a in soup.find_all('a', href=True): # Buscar todas las etiquetas <a> con atributo href
        enlaces.append(a['href']) # Añadir el enlace a la lista

    # Extraer URLs de imágenes <img src="">
    imagenes = [] # Lista para almacenar imágenes
    for img in soup.find_all('img', src=True): # Buscar todas las etiquetas <img> con atributo src
        imagenes.append(img['src']) # Añadir la imagen a la lista

    # Estadísticas de etiquetas
    estadisticas = {} # Diccionario para almacenar estadísticas de etiquetas
    for etiqueta in ETIQUETAS_ESTADISTICAS: # Iterar sobre las etiquetas definidas
        estadisticas[etiqueta] = len(soup.find_all(etiqueta)) # Contar cuántas veces aparece cada etiqueta

    return enlaces, imagenes, estadisticas # Lista de enlaces, lista de imágenes y diccionario de estadísticas

def analizar_url(url): 
    """Descarga el contenido de la URL y lo analiza."""
    try: # Realizar una solicitud GET a la URL
        respuesta = requests.get(url) # Verificar si la solicitud fue exitosa
        respuesta.raise_for_status() # Lanzar un error si la solicitud falló
        contenido = respuesta.text # Obtener el contenido HTML de la respuesta
        return analizar_html(contenido) # Analizar el contenido HTML
    except Exception as e: # Manejar excepciones durante la solicitud
        print(f"Error al obtener {url}: {e}") # Imprimir mensaje de error
        return [], [], {} # Devolver listas vacías y diccionario vacío en caso de error

def analizar_archivo(ruta_archivo): 
    """Lee un archivo HTML local y lo analiza."""
    try: # Abrir el archivo HTML local
        with open(ruta_archivo, 'r', encoding='utf-8') as f: # Leer el contenido del archivo
            contenido = f.read() # Obtener el contenido del archivo
        return analizar_html(contenido) # Analizar el contenido HTML del archivo
    except Exception as e: # Manejar excepciones al leer el archivo
        print(f"Error al leer {ruta_archivo}: {e}") # Imprimir mensaje de error
        return [], [], {} # Devolver listas vacías y diccionario vacío en caso de error

def guardar_urls(fuentes_resultados, fichero_salida="urls_bs4_extraidas.txt"): 
    """Guarda en un archivo las URLs y estadísticas con conteos."""
    with open(fichero_salida, 'w', encoding='utf-8') as f: # Abrir el archivo de salida
        for nombre, (enlaces, imagenes, estadisticas) in fuentes_resultados.items(): # Iterar sobre los resultados de cada fuente
            f.write(f"--- URLs extraídas de {nombre} ---\n") # Escribir el nombre de la fuente
            f.write(f"Enlaces ({len(enlaces)}):\n") # Escribir la cantidad de enlaces encontrados
            for enlace in enlaces: # Escribir cada enlace encontrado
                f.write(enlace + "\n") # Añadir un salto de línea
            f.write(f"Imágenes ({len(imagenes)}):\n") # Escribir la cantidad de imágenes encontradas
            for img in imagenes: # Escribir cada imagen encontrada
                f.write(img + "\n") # Añadir un salto de línea
            f.write("\n") # Añadir una línea en blanco entre fuentes

def imprimir_resultados(fuentes_resultados): 
    """Imprime resultados en consola con formato."""
    for nombre, (enlaces, imagenes, estadisticas) in fuentes_resultados.items(): # Iterar sobre los resultados de cada fuente
        print(f"🧪 {nombre}")  
        print("Enlaces ({}):".format(len(enlaces))) # Imprimir la cantidad de enlaces encontrados
        for enlace in enlaces: # Imprimir cada enlace encontrado
            print(f"  {enlace}") # Añadir un espacio para mejor legibilidad
        print("Imágenes ({}):".format(len(imagenes))) # Imprimir la cantidad de imágenes encontradas
        for img in imagenes: # Imprimir cada imagen encontrada
            print(f"  {img}") # Añadir un espacio para mejor legibilidad
        print("Estadísticas de etiquetas:") # Imprimir estadísticas de etiquetas
        for etiqueta in ETIQUETAS_ESTADISTICAS: # Iterar sobre las etiquetas definidas
            print(f"  <{etiqueta}>: {estadisticas.get(etiqueta,0)}") # Imprimir la cantidad de veces que aparece cada etiqueta
        print() # Añadir una línea en blanco entre fuentes

def main(): 
    # URLs reales a analizar
    urls = { # Diccionario de URLs a analizar
        "example.com": "https://www.example.com",
        "python.org": "https://www.python.org",
        "wikipedia.org": "https://www.wikipedia.org"
    }

    # Archivos locales a analizar
    archivos = [f"prueba{i}.html" for i in range(1,7)] # Lista de archivos HTML locales a analizar

    resultados = {} # Diccionario para almacenar los resultados de análisis

    # Analizar URLs reales
    for nombre, url in urls.items(): # Iterar sobre las URLs a analizar
        print(f"Analizando URL: {url}") # Imprimir mensaje de inicio de análisis
        resultados[nombre] = analizar_url(url) # Analizar la URL y almacenar los resultados

    # Analizar archivos locales
    for archivo in archivos: # Iterar sobre los archivos locales a analizar
        print(f"Analizando archivo: {archivo}") # Imprimir mensaje de inicio de análisis
        resultados[archivo] = analizar_archivo(archivo) # Analizar el archivo y almacenar los resultados

    # Imprimir resultados
    imprimir_resultados(resultados) # Imprimir los resultados en consola

    # Guardar URLs e imágenes en archivo de texto
    guardar_urls(resultados, fichero_salida="urls_bs4_extraidas.txt") # Guardar los resultados en un archivo de texto
    print("URLs guardadas en 'urls_bs4_extraidas.txt'") # Imprimir mensaje de confirmación

if __name__ == "__main__": # Punto de entrada del script
    main() # Ejecutar la función principal
