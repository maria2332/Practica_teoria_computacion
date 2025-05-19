# main.py
import os
from parser import parse_html

def main():
    files = [
        'prueba1.html', 'prueba2.html', 'prueba3.html',
        'prueba4.html', 'prueba5.html', 'prueba6.html'
    ]

    print("🔍 Iniciando análisis de HTMLs...\n")

    for filename in files:
        if not os.path.isfile(filename):
            print(f"⚠️ Archivo no encontrado: {filename}\n")
            continue

        with open(filename, encoding='utf-8') as f:
            data = f.read()

        links, images, balanced = parse_html(data)

        print(f"🧪 {filename}\n")
        print(f"Enlaces (<a href=...>): {len(links)}")
        for link in links:
            print(f'<a href="{link}"> → ✅ Correcto')
        print()
        print(f"Imágenes (<img src=...>): {len(images)}")
        for img in images:
            print(f'<img src="{img}"> → ✅ Correcto')
        print()
        print(f"Balanceado: {'✅ Sí' if balanced else '❌ No'}\n")

        # Guardar URLs en ficheros
        with open(f'{filename}_links.txt', 'w', encoding='utf-8') as f_links:
            for link in links:
                f_links.write(link + '\n')

        with open(f'{filename}_images.txt', 'w', encoding='utf-8') as f_imgs:
            for img in images:
                f_imgs.write(img + '\n')

if __name__ == "__main__":
    main()
