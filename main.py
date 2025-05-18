import os
from lexer import lexer
from parser import is_html_balanced

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

def main():
    html_dir = "/mnt/data"
    with open("/mnt/data/urls_extraidas.txt", "w", encoding='utf-8') as out:
        for filename in sorted(f for f in os.listdir(html_dir) if f.endswith(".html")):
            filepath = os.path.join(html_dir, filename)
            with open(filepath, encoding='utf-8') as f:
                html = f.read()

            hrefs, srcs = extraer_urls(html)
            balanceado = is_html_balanced(html)

            print(f"\n🗂️ Procesando {filename}")
            print("🔗 Enlaces encontrados:", hrefs)
            print("🖼️ Imágenes encontradas:", srcs)
            print("✅ ¿HTML balanceado?:", balanceado)

            out.write(f"Archivo: {filename}\n")
            out.write("Enlaces:\n" + "\n".join(hrefs) + "\n")
            out.write("Imágenes:\n" + "\n".join(srcs) + "\n")
            out.write("Balanceado: " + str(balanceado) + "\n\n")

if __name__ == "__main__":
    main()
