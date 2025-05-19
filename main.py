import os
from parser import parse_html, is_html_balanced

HTML_DIR = "."  # Directorio donde están los archivos .html
OUTPUT_FILE = "urls_extraidas.txt"

def main():
    print("🔍 Iniciando análisis de HTMLs...\n")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
        for filename in sorted(os.listdir(HTML_DIR)):
            if filename.endswith(".html"):
                path = os.path.join(HTML_DIR, filename)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Analizar HTML
                links, images = parse_html(content)
                balanced = is_html_balanced(content)

                # Imprimir resultados por pantalla
                print(f"🧪 {filename}")
                print(f"Enlaces (<a href=...>): {len(links)}")
                for l in links:
                    print(f"\n<a href=\"{l}\"> → ✅ Correcto")

                print(f"\nImágenes (<img src=...>): {len(images)}")
                for i in images:
                    print(f"\n<img src=\"{i}\"> → ✅ Correcto")

                print(f"\nBalanceado: {'✅ Sí' if balanced else '❌ No'}\n")

                # Guardar en archivo
                f_out.write(f"{filename}\n")
                f_out.write("Links:\n" + "\n".join(links) + "\n")
                f_out.write("Images:\n" + "\n".join(images) + "\n\n")

if __name__ == "__main__":
    main()
