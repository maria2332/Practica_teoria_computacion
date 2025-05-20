from bs4 import BeautifulSoup

# Etiquetas a contar para estadísticas
ETIQUETAS = ['a', 'img', 'br', 'div', 'li', 'ul', 'p', 'span', 'table', 'td', 'tr']

def extraer_datos_html(contenido):
    soup = BeautifulSoup(contenido, 'html.parser')

    # Extraer enlaces y urls de imágenes
    enlaces = [a.get('href') for a in soup.find_all('a') if a.get('href')]
    imagenes = [img.get('src') for img in soup.find_all('img') if img.get('src')]

    # Contar etiquetas
    estadisticas = {tag: len(soup.find_all(tag)) for tag in ETIQUETAS}

    return enlaces, imagenes, estadisticas

def guardar_urls_en_archivo(nombre_archivo, nombre_html, enlaces, imagenes):
    with open(nombre_archivo, 'a', encoding='utf-8') as f:
        f.write(f"--- URLs extraídas de {nombre_html} ---\n")
        f.write(f"Enlaces ({len(enlaces)}):\n")
        for url in enlaces:
            f.write(url + "\n")
        f.write(f"Imágenes ({len(imagenes)}):\n")
        for url in imagenes:
            f.write(url + "\n")
        f.write("\n")

def analizar_archivo(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        contenido = f.read()

    enlaces, imagenes, estadisticas = extraer_datos_html(contenido)

    print(f"\n🧪 {filename}")
    print("Enlaces ({}):".format(len(enlaces)))
    for url in enlaces:
        print(f"  {url}")
    print("Imágenes ({}):".format(len(imagenes)))
    for url in imagenes:
        print(f"  {url}")
    print("Estadísticas de etiquetas:")
    for tag in ETIQUETAS:
        print(f"  <{tag}>: {estadisticas.get(tag,0)}")

    return enlaces, imagenes

if __name__ == "__main__":
    archivos = [f"prueba{i}.html" for i in range(1, 7)]
    archivo_salida = "urls_bs4.txt"

    # Sobrescribir fichero al iniciar
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write("")

    for archivo in archivos:
        enlaces, imagenes = analizar_archivo(archivo)
        guardar_urls_en_archivo(archivo_salida, archivo, enlaces, imagenes)
