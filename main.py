from parser import parse_html
import os

def main():
    folder = '.'  # ajusta si tus HTML están en otra carpeta
    files = sorted([f for f in os.listdir(folder) if f.endswith('.html')])

    print("🔍 Iniciando análisis de HTMLs...\n")

    for filename in files:
        with open(os.path.join(folder, filename), encoding='utf-8') as f:
            data = f.read()

        links, images, balanced = parse_html(data)

        print(f"🧪 {filename}\n")

        print(f"Enlaces (<a href=...>): {len(links)}")
        for link in links:
            print(f'<a href="{link}"> → ✅ Correcto')

        print(f"\nImágenes (<img src=...>): {len(images)}")
        for img in images:
            print(f'<img src="{img}"> → ✅ Correcto')

        print(f"\nBalanceado: {'✅ Sí' if balanced else '❌ No'}\n")

if __name__ == "__main__":
    main()
