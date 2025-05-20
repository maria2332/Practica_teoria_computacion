from bs4 import BeautifulSoup
import os

def analizar_archivo_bs4(filename, archivo_salida):
    with open(filename, "r", encoding="utf-8") as f:
        contenido = f.read()
    soup = BeautifulSoup(contenido, "html.parser")

    # Extraer URLs
    enlaces = [a.get('href') for a in soup.find_all('a', href=True)]
    imagenes = [img.get('src') for img in soup.find_all('img', src=True)]

    # Etiquetas para estadísticas
    etiquetas = ['a', 'img', 'br', 'div', 'li', 'ul', 'p', 'span', 'table', 'td', 'tr']

    # Contar cada etiqueta
    stats = {tag: len(soup.find_all(tag)) for tag in etiquetas}

    # Mostrar resultados por consola
    print(f"\n🧪 {os.path.basename(filename)}")
    print(f"Enlaces ({len(enlaces)}):")
    for url in enlaces:
        print(f"  {url}")
    print(f"Imágenes ({len(imagenes)}):")
    for url in imagenes:
        print(f"  {url}")

    print("Estadísticas de etiquetas:")
    for tag in etiquetas:
        print(f"  <{tag}>: {stats[tag]}")

    # Guardar URLs en archivo común
    with open(archivo_salida, "a", encoding="utf-8") as f_out:
        f_out.write(f"\n--- URLs extraídas de {os.path.basename(filename)} ---\n")
        f_out.write("Enlaces:\n")
        for url in enlaces:
            f_out.write(f"{url}\n")
        f_out.write("Imágenes:\n")
        for url in imagenes:
            f_out.write(f"{url}\n")

if __name__ == "__main__":
    archivo_comun = "urls_bs4.txt"
    # Limpiar contenido previo
    open(archivo_comun, "w").close()

    archivos_html = [f"prueba{i}.html" for i in range(1, 7)]
    for archivo in archivos_html:
        analizar_archivo_bs4(archivo, archivo_comun)
