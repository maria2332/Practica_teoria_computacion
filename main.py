from parser import parse_html, is_html_balanced # Importar funciones de parser.py 
import os # Importar os para manejar archivos

def guardar_urls_en_archivo(nombre_archivo, enlaces, imagenes, balanceado): # Guardar URLs en un archivo
    with open(nombre_archivo, 'a', encoding='utf-8') as f: # Abrir archivo en modo append
        f.write(f"{nombre_archivo.replace('_urls.txt', '')}\n") # Nombre del archivo
        f.write(f"Enlaces ({len(enlaces)}):\n") # Enlaces
        for url in enlaces: # Guardar enlaces
            f.write(f"{url}\n") # Escribir enlace
        f.write("\n") # Nueva línea

        f.write(f"Imágenes ({len(imagenes)}):\n") # Imágenes
        for url in imagenes: # Guardar imágenes
            f.write(f"{url}\n") # Escribir imagen
        f.write("\n") # Nueva línea

        f.write(f"Balanceado: {balanceado}\n\n") # Guardar balanceado

def analizar_archivo(filename): # Analizar archivo HTML
    with open(filename, "r", encoding="utf-8") as f: # Abrir archivo
        contenido = f.read() # Leer contenido

    enlaces, imagenes, errores = parse_html(contenido) # Analizar contenido HTML
    balanceado = is_html_balanced() # Verificar si está balanceado

    print(f"\n🧪 {os.path.basename(filename)}\n") 
    print(f"Enlaces (<a href=...>): {len(enlaces)}") # Contar enlaces
    for e in enlaces: # Mostrar enlaces
        print(f'<a href="{e}"> → ✅ Correcto')  # Enlace correcto

    print(f"\nImágenes (<img src=...>): {len(imagenes)}") # Contar imágenes
    for i in imagenes: # Mostrar imágenes
        print(f'<img src="{i}"> → ✅ Correcto') # Imagen correcta

    if balanceado: # Verificar balanceado
        print("\nBalanceado: ✅ Sí") # Si está balanceado
    else:  # Si no está balanceado
        print("\nBalanceado: ❌ No") # Mostrar no balanceado
        print(" - Errores detectados:") # Mostrar errores
        for err in errores: # Mostrar errores
            print(f" - {err}") # Error

    nombre_salida = "urls_extraidas.txt" # Nombre del archivo de salida
    guardar_urls_en_archivo(nombre_salida, enlaces, imagenes, balanceado) # Guardar URLs en archivo

if __name__ == "__main__": # Función principal
    print("🔍 Iniciando análisis de HTMLs...") 
    # Vacía archivo previo para resultados frescos
    open("urls_extraidas.txt", "w", encoding="utf-8").close() # Vaciar archivo de salida
    for i in range(1, 7): # Analizar archivos de prueba
        analizar_archivo(f"prueba{i}.html") # Analizar archivo
