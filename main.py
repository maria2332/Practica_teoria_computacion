import os
from lexer import lexer

def extraer_urls(html):
    hrefs = []
    srcs = []
    last_token = ""

    lexer.input(html)

    for tok in lexer:
        if last_token == "HREF" and tok.type == "URL":
            hrefs.append(tok.value)
        elif last_token == "SRC" and tok.type == "URL":
            srcs.append(tok.value)
        last_token = tok.type

    return hrefs, srcs

def main():
    carpeta = "."  # usa "." si tienes los HTML en la misma carpeta

    archivos = sorted(f for f in os.listdir(carpeta) if f.endswith(".html"))

    for archivo in archivos:
        with open(os.path.join(carpeta, archivo), encoding='utf-8') as f:
            html = f.read()

        hrefs, srcs = extraer_urls(html)

        print(f"\n🗂️ Procesando {archivo}")
        print("🔗 Enlaces encontrados:")
        for h in hrefs:
            print(f" - {h}")

        print("🖼️ Imágenes encontradas:")
        for s in srcs:
            print(f" - {s}")

if __name__ == "__main__":
    main()
