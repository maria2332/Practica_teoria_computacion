import os
from lexer import lexer
from parser import is_html_balanced  # solo para verificación de etiquetas

def extraer_urls(html):
    hrefs = []
    srcs = []

    lexer.input(html)

    last_token = ""
    context_tag = None  # para saber si estamos dentro de <a> o <img>

    for tok in lexer:
        if tok.type == "A_OPEN":
            context_tag = "a"
        elif tok.type == "IMG_OPEN":
            context_tag = "img"

        if last_token == "HREF" and tok.type == "URL" and context_tag == "a":
            hrefs.append(tok.value)
            context_tag = None  # reset después de detectar
        elif last_token == "SRC" and tok.type == "URL" and context_tag == "img":
            srcs.append(tok.value)
            context_tag = None

        if tok.type in ["TAG_CLOSE", "TAG_SLASH_CLOSE"]:
            context_tag = None  # cerrar el contexto tras > o />

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
