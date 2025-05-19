import os
from parser import parse_html

def main():
    print("🔍 Iniciando análisis de HTMLs...\n")
    files = [f"prueba{i}.html" for i in range(1,7)]

    for filename in files:
        print(f"🧪 {filename}\n")
        if not os.path.exists(filename):
            print(f"Archivo {filename} no encontrado.\n")
            continue

        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()

        links, images, balanced = parse_html(data)

        print(f"Enlaces (<a href=...>): {len(links)}")
        for l in links:
            print(f'<a href="{l}"> → ✅ Correcto')

        print(f"\nImágenes (<img src=...>): {len(images)}")
        for i in images:
            print(f'<img src="{i}"> → ✅ Correcto')

        print(f"\nBalanceado: {'✅ Sí' if balanced else '❌ No'}\n")

if __name__ == "__main__":
    main()
