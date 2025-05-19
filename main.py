from parser import parse_html, is_html_balanced 
import os # Importar el módulo os para manejar rutas de archivos

def analizar_archivo(filename): # Función para analizar un archivo HTML
    with open(filename, "r", encoding="utf-8") as f: # Abrir el archivo en modo lectura
        contenido = f.read() # Leer el contenido del archivo

    enlaces, imagenes, errores = parse_html(contenido) # Analizar el contenido HTML

    print(f"\n🧪 {os.path.basename(filename)}\n") 

    print(f"Enlaces (<a href=...>): {len(enlaces)}") # Contar enlaces
    for e in enlaces:
        print(f'<a href="{e}"> → ✅ Correcto') # Mostrar enlaces

    print(f"\nImágenes (<img src=...>): {len(imagenes)}") # Contar imágenes
    for i in imagenes:
        print(f'<img src="{i}"> → ✅ Correcto') # Mostrar imágenes

    if is_html_balanced(): # Verificar si el HTML está balanceado
        print("\nBalanceado: ✅ Sí") 
    else:
        print("\nBalanceado: ❌ No")
        print(" - Errores detectados:") # Mostrar errores
        for err in errores: 
            print(f" - {err}") 

if __name__ == "__main__": # Punto de entrada del script
    print("🔍 Iniciando análisis de HTMLs...") 
    for i in range(1, 7):
        analizar_archivo(f"prueba{i}.html") # Analizar archivos de prueba
