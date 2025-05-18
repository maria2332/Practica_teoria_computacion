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
    archivo = "prueba1.html"  # cámbialo al nombre del archivo que quieras analizar

    with open(archivo, encoding='utf-8') as f:
        html = f.read()

    enlaces, imagenes = extraer_urls(html)

    print("🔗 Enlaces encontrados:")
    for e in enlaces:
        print(f" - {e}")

    print("\n🖼️ Imágenes encontradas:")
    for i in imagenes:
        print(f" - {i}")

if __name__ == "__main__":
    main()
