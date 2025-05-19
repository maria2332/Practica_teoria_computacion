import os
from parser import parse_html, is_html_balanced

def analizar_archivo(filename):
    with open(filename, "r", encoding="utf-8") as f:
        contenido = f.read()

    enlaces, imagenes = parse_html(contenido)
    balanceado = is_html_balanced()

    print(f"\n🧪 {os.path.basename(filename)}")

    print(f"\nEnlaces (<a href=...>): {len(enlaces)}")
    for e in enlaces:
        print(f'\n<a href="{e}"> → ✅ Correcto')

    print(f"\nImágenes (<img src=...>): {len(imagenes)}")
    for i in imagenes:
        print(f'\n<img src="{i}"> → ✅ Correcto')

    print(f"\nBalanceado: {'✅ Sí' if balanceado else '❌ No'}")

if _name_ == "_main_":
    print("🔍 Iniciando análisis de HTMLs...")
    for i in range(1, 7):
        analizar_archivo(f"prueba{i}.html")