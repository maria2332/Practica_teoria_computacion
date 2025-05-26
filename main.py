import os # Importar os para manejar rutas de archivos
import requests  # Importar requests para hacer solicitudes HTTP
from lexer import lexer # Importar el lexer
from parser import parse_html, is_html_balanced # Importar el parser y la función para verificar balanceo

def analizar_contenido_html(contenido, nombre): 
    enlaces, imagenes, errores = parse_html(contenido) # Analizar el contenido HTML

    print(f"\n🧪 {nombre}") 
    print(f"Enlaces ({len(enlaces)}):") # Imprimir la cantidad de enlaces encontrados
    for e in enlaces: # Imprimir cada enlace encontrado
        print(f"  {e}") # Añadir un salto de línea para mejor legibilidad
    print(f"Imágenes ({len(imagenes)}):") # Imprimir la cantidad de imágenes encontradas
    for i in imagenes: # Imprimir cada imagen encontrada
        print(f"  {i}") # Añadir un salto de línea para mejor legibilidad
    if errores: # Si hay errores, imprimirlos
        print("Balanceado: ❌ No")  # Indicar que no está balanceado
        print("Errores:") # Imprimir errores encontrados
        for err in errores: # Iterar sobre los errores
            print(f"  - {err}") # Imprimir cada error encontrado
    else:   # Si no hay errores, indicar que está balanceado
        print("Balanceado: ✅ Sí")  # Indicar que está balanceado

    return enlaces, imagenes  # Devolver listas de enlaces e imágenes

def guardar_urls(nombre_fichero, datos):    
    with open(nombre_fichero, "w", encoding="utf-8") as f:  # Abrir el archivo para escribir
        for nombre, enlaces, imagenes in datos:     # Iterar sobre los datos de cada fuente
            f.write(f"--- URLs extraídas de {nombre} ---\n")    # Escribir el nombre de la fuente
            f.write(f"Enlaces ({len(enlaces)}):\n") # Escribir la cantidad de enlaces encontrados
            for e in enlaces:   # Iterar sobre los enlaces encontrados
                f.write(e + "\n")   # Escribir cada enlace en una nueva línea
            f.write(f"Imágenes ({len(imagenes)}):\n")   # Escribir la cantidad de imágenes encontradas
            for i in imagenes:  # Iterar sobre las imágenes encontradas
                f.write(i + "\n")   # Escribir cada imagen en una nueva línea
            f.write("\n")   # Añadir una línea en blanco entre fuentes

def analizar_archivos_locales(ruta_carpeta, archivos):
    resultados = [] # Lista para almacenar los resultados de análisis
    for archivo in archivos:    # Iterar sobre los archivos HTML locales
        ruta = os.path.join(ruta_carpeta, archivo)  # Construir la ruta completa del archivo
        with open(ruta, "r", encoding="utf-8") as f:    # Abrir el archivo para leer
            contenido = f.read()    # Leer el contenido del archivo
        enlaces, imagenes = analizar_contenido_html(contenido, archivo) # Analizar el contenido HTML del archivo
        resultados.append((archivo, enlaces, imagenes)) # Añadir los resultados a la lista
    return resultados   # Devolver la lista de resultados

def analizar_urls_web(urls):
    resultados = [] # Lista para almacenar los resultados de análisis
    for url in urls:    # Iterar sobre las URLs web a analizar
        print(f"\nDescargando {url} ...")   # Imprimir mensaje de inicio de descarga
        try:    # Intentar descargar el contenido de la URL
            resp = requests.get(url)    # Hacer la solicitud HTTP GET
            resp.raise_for_status() # Verificar si la solicitud fue exitosa
            contenido = resp.text   # Obtener el contenido HTML de la respuesta
            enlaces, imagenes = analizar_contenido_html(contenido, url) # Analizar el contenido HTML de la URL
            resultados.append((url, enlaces, imagenes)) # Añadir los resultados a la lista
        except Exception as e:  # Manejar excepciones durante la solicitud
            print(f"Error al descargar {url}: {e}") # Imprimir mensaje de error
            resultados.append((url, [], []))    # Añadir la URL con listas vacías en caso de error
    return resultados   # Devolver la lista de resultados

if __name__ == "__main__":  # Punto de entrada del script
    # Define archivos locales y URLs
    carpeta_local = "."  # O ajusta al path donde tengas los HTML
    archivos_html = [f"prueba{i}.html" for i in range(1,7)] # Lista de archivos HTML locales a analizar
    urls_web = [    # Lista de URLs web a analizar
        "https://www.example.com",
        "https://www.python.org",
        "https://www.wikipedia.org"
    ]

    print("🔍 Analizando archivos HTML locales...") 
    resultados_locales = analizar_archivos_locales(carpeta_local, archivos_html)    # Analizar archivos HTML locales

    print("\n🔍 Analizando URLs web reales...")
    resultados_web = analizar_urls_web(urls_web) # Analizar URLs web reales

    # Combinar resultados para guardar en un archivo único  
    todos_resultados = resultados_locales + resultados_web  # Combinar resultados de archivos locales y URLs web
    guardar_urls("urls_extraidas.txt", todos_resultados)    # Guardar los resultados en un archivo

    print("\n✅ Análisis completado. URLs guardadas en 'urls_extraidas.txt'.")