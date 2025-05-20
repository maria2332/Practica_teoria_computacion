import os
import requests
from lexer import lexer
from parser import parse_html, is_html_balanced

def analizar_contenido_html(contenido, nombre):
    enlaces, imagenes, errores = parse_html(contenido)

    print(f"\n🧪 {nombre}")
    print(f"Enlaces ({len(enlaces)}):")
    for e in enlaces:
        print(f"  {e}")
    print(f"Imágenes ({len(imagenes)}):")
    for i in imagenes:
        print(f"  {i}")
    if errores:
        print("Balanceado: ❌ No")
        print("Errores:")
        for err in errores:
            print(f"  - {err}")
    else:
        print("Balanceado: ✅ Sí")

    return enlaces, imagenes

def guardar_urls(nombre_fichero, datos):
    with open(nombre_fichero, "w", encoding="utf-8") as f:
        for nombre, enlaces, imagenes in datos:
            f.write(f"--- URLs extraídas de {nombre} ---\n")
            f.write(f"Enlaces ({len(enlaces)}):\n")
            for e in enlaces:
                f.write(e + "\n")
            f.write(f"Imágenes ({len(imagenes)}):\n")
            for i in imagenes:
                f.write(i + "\n")
            f.write("\n")

def analizar_archivos_locales(ruta_carpeta, archivos):
    resultados = []
    for archivo in archivos:
        ruta = os.path.join(ruta_carpeta, archivo)
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
        enlaces, imagenes = analizar_contenido_html(contenido, archivo)
        resultados.append((archivo, enlaces, imagenes))
    return resultados

def analizar_urls_web(urls):
    resultados = []
    for url in urls:
        print(f"\nDescargando {url} ...")
        try:
            resp = requests.get(url)
            resp.raise_for_status()
            contenido = resp.text
            enlaces, imagenes = analizar_contenido_html(contenido, url)
            resultados.append((url, enlaces, imagenes))
        except Exception as e:
            print(f"Error al descargar {url}: {e}")
            resultados.append((url, [], []))
    return resultados

if __name__ == "__main__":
    # Define archivos locales y URLs
    carpeta_local = "."  # O ajusta al path donde tengas los HTML
    archivos_html = [f"prueba{i}.html" for i in range(1,7)]
    urls_web = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.wikipedia.org"
    ]

    print("🔍 Analizando archivos HTML locales...")
    resultados_locales = analizar_archivos_locales(carpeta_local, archivos_html)

    print("\n🔍 Analizando URLs web reales...")
    resultados_web = analizar_urls_web(urls_web)

    # Combinar resultados para guardar en un archivo único
    todos_resultados = resultados_locales + resultados_web
    guardar_urls("urls_extraidas.txt", todos_resultados)

    print("\n✅ Análisis completado. URLs guardadas en 'urls_extraidas.txt'.")