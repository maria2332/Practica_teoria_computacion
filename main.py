import os
from parser import parse_html, is_html_balanced

def main():
    print("🔍 Iniciando análisis de HTMLs...\n")
    archivos = sorted([f for f in os.listdir() if f.endswith(".html")])

    for archivo in archivos:
        with open(archivo, encoding='utf-8') as f:
            html = f.read()

        enlaces, imagenes = parse_html(html)
        balanceado = is_html_balanced(html)

        print(f"🧪 {archivo}")
        print(f"Enlaces (<a href=...>): {len(enlaces)}")
        for e in enlaces:
            print(f'\n<a href="{e}"> → ✅ Correcto')

        print(f"\nImágenes (<img src=...>): {len(imagenes)}")
        for i in imagenes:
            print(f'\n<img src="{i}"> → ✅ Correcto')

        print(f"\nBalanceado: {'✅ Sí' if balanceado else '❌ No'}\n")

if __name__ == "__main__":
    main()
