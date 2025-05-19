import os
from parser import parse_html, is_html_balanced

def main():
    print("🔍 Iniciando análisis de HTMLs...\n")
    archivos = sorted([f for f in os.listdir() if f.endswith(".html")])
    if not archivos:
        print("❌ No se encontraron archivos .html en la carpeta.")
        return

    with open("urls_extraidas.txt", "w", encoding="utf-8") as salida:
        for archivo in archivos:
            with open(archivo, encoding="utf-8") as f:
                html = f.read()

            enlaces, imagenes = parse_html(html)
            balanceado = is_html_balanced(html)

            print(f"🗂️ Procesando {archivo}")
            print(f"🔗 Enlaces encontrados: {len(enlaces)}")
            for e in enlaces:
                print(f" - {e}")
            print(f"🖼️ Imágenes encontradas: {len(imagenes)}")
            for i in imagenes:
                print(f" - {i}")
            print(f"📐 ¿HTML balanceado?: {balanceado}\n")

            salida.write(f"{archivo}\n")
            salida.write(f"Enlaces ({len(enlaces)}):\n" + "\n".join(enlaces) + "\n")
            salida.write(f"Imágenes ({len(imagenes)}):\n" + "\n".join(imagenes) + "\n")
            salida.write(f"Balanceado: {balanceado}\n\n")

if __name__ == "__main__":
    main()
