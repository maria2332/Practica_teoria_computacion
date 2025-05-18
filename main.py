from lexer import lexer
from parser import HTMLBalanceChecker

def extraer_urls(html):
    hrefs, srcs = [], []
    lexer.input(html)
    last_token = ""

    for tok in lexer:
        if last_token == "HREF_ATTR" and tok.type == "URL":
            hrefs.append(tok.value)
        elif last_token == "SRC_ATTR" and tok.type == "URL":
            srcs.append(tok.value)
        last_token = tok.type
    return hrefs, srcs

def verificar_balanceo(html):
    parser = HTMLBalanceChecker()
    parser.feed(html)
    return parser.is_balanced()

def main():
    for i in range(1, 7):
        filename = f"prueba{i}.html"
        print(f"\n🗂️ Procesando {filename}")
        with open(filename, encoding='utf-8') as f:
            html = f.read()

        hrefs, srcs = extraer_urls(html)
        print("🔗 Enlaces encontrados:", hrefs)
        print("🖼️ Imágenes encontradas:", srcs)
        print("✅ ¿HTML balanceado?:", verificar_balanceo(html))

if __name__ == "__main__":
    main()
