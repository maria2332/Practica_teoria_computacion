# main.py
import os
from parser import parse_html, is_html_balanced

def analizar_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    enlaces, imagenes = parse_html(contenido)
    balanceado = is_html_balanced(contenido)

    print(f"\n🧪 {nombre_archivo}")
    print(f"\nEnlaces (<a href=...>): {len(enlaces)}")
    for enlace in enlaces:
        print(f'\n<a href="{enlace}"> → ✅ Correcto')

    print(f"\nImágenes (<img src=...>): {len(imagenes)}")
    for img in imagenes:
        print(f'\n<img src="{img}"> → ✅ Correcto')

    print(f"\nBalanceado: {'✅ Sí' if balanceado else '❌ No'}")

def main():
    print("🔍 Iniciando análisis de HTMLs...")

    archivos = [
        "prueba1.html",
        "prueba2.html",
        "prueba3.html",
        "prueba4.html",
        "prueba5.html",
        "prueba6.html"
    ]

    for archivo in archivos:
        if os.path.exists(archivo):
            analizar_archivo(archivo)
        else:
            print(f"⚠️ Archivo no encontrado: {archivo}")

if __name__ == "__main__":
    main()
