import os
from lexer import lexer
from parser import is_html_balanced

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
    archivos = sorted(f for f in os.listdir() if f.endswith(".html"))

    for archivo in archivos:
        with open(archivo, encoding='utf-8') as f:
            html = f.read()

        enlaces, imagenes = extraer_urls(html)
        balanceado = is_html_balanced(html)

        print(f"\n🗂️ Procesando {archivo}")
        print(f"🔗 Enlaces encontrados: {len(enlaces)}")
        for e in enlaces:
            print(f" - {e}")
        print(f"🖼️ Imágenes encontradas: {len(imagenes)}")
        for i in imagenes:
            print(f" - {i}")
        print(f"📐 ¿HTML balanceado?: {balanceado}")

if __name__ == "__main__":
    main()
