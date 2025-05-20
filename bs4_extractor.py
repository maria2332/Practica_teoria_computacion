import requests
from bs4 import BeautifulSoup
import os

# Etiquetas a analizar
ETIQUETAS_ESTADISTICAS = ['a', 'img', 'br', 'div', 'li', 'ul', 'p', 'span', 'table', 'td', 'tr']

def analizar_html(contenido_html):
    """Analiza el HTML con BeautifulSoup y devuelve enlaces, imágenes y estadísticas de etiquetas."""
    soup = BeautifulSoup(contenido_html, 'html.parser')

    # Extraer URLs de enlaces <a href="">
    enlaces = []
    for a in soup.find_all('a', href=True):
        enlaces.append(a['href'])

    # Extraer URLs de imágenes <img src="">
    imagenes = []
    for img in soup.find_all('img', src=True):
        imagenes.append(img['src'])

    # Estadísticas de etiquetas
    estadisticas = {}
    for etiqueta in ETIQUETAS_ESTADISTICAS:
        estadisticas[etiqueta] = len(soup.find_all(etiqueta))

    return enlaces, imagenes, estadisticas

def analizar_url(url):
    """Descarga el contenido de la URL y lo analiza."""
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        contenido = respuesta.text
        return analizar_html(contenido)
    except Exception as e:
        print(f"Error al obtener {url}: {e}")
        return [], [], {}

def analizar_archivo(ruta_archivo):
    """Lee un archivo HTML local y lo analiza."""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        return analizar_html(contenido)
    except Exception as e:
        print(f"Error al leer {ruta_archivo}: {e}")
        return [], [], {}

def guardar_urls(fuentes_resultados, fichero_salida="urls_bs4_extraidas.txt"):
    """Guarda en un archivo las URLs y estadísticas con conteos."""
    with open(fichero_salida, 'w', encoding='utf-8') as f:
        for nombre, (enlaces, imagenes, estadisticas) in fuentes_resultados.items():
            f.write(f"--- URLs extraídas de {nombre} ---\n")
            f.write(f"Enlaces ({len(enlaces)}):\n")
            for enlace in enlaces:
                f.write(enlace + "\n")
            f.write(f"Imágenes ({len(imagenes)}):\n")
            for img in imagenes:
                f.write(img + "\n")
            f.write("\n")

def imprimir_resultados(fuentes_resultados):
    """Imprime resultados en consola con formato."""
    for nombre, (enlaces, imagenes, estadisticas) in fuentes_resultados.items():
        print(f"🧪 {nombre}")
        print("Enlaces ({}):".format(len(enlaces)))
        for enlace in enlaces:
            print(f"  {enlace}")
        print("Imágenes ({}):".format(len(imagenes)))
        for img in imagenes:
            print(f"  {img}")
        print("Estadísticas de etiquetas:")
        for etiqueta in ETIQUETAS_ESTADISTICAS:
            print(f"  <{etiqueta}>: {estadisticas.get(etiqueta,0)}")
        print()

def main():
    # URLs reales a analizar
    urls = {
        "example.com": "https://www.example.com",
        "python.org": "https://www.python.org",
        "wikipedia.org": "https://www.wikipedia.org"
    }

    # Archivos locales a analizar
    archivos = [f"prueba{i}.html" for i in range(1,7)]

    resultados = {}

    # Analizar URLs reales
    for nombre, url in urls.items():
        print(f"Analizando URL: {url}")
        resultados[nombre] = analizar_url(url)

    # Analizar archivos locales
    for archivo in archivos:
        print(f"Analizando archivo: {archivo}")
        resultados[archivo] = analizar_archivo(archivo)

    # Imprimir resultados
    imprimir_resultados(resultados)

    # Guardar URLs e imágenes en archivo de texto
    guardar_urls(resultados, fichero_salida="urls_bs4_extraidas.txt")
    print("URLs guardadas en 'urls_bs4_extraidas.txt'")

if __name__ == "__main__":
    main()
