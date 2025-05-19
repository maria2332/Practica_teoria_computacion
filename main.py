import os
from parser import parse_html

# Verificador de balanceo básico
def is_html_balanced(html):
    import re
    VOID_TAGS = {'br', 'img', 'meta', 'hr', 'input', 'link'}
    stack = []
    tags = re.findall(r'<(/?)([a-zA-Z0-9]+)', html)
    for slash, tag in tags:
        tag = tag.lower()
        if tag in VOID_TAGS:
            continue
        if not slash:
            stack.append(tag)
        else:
            if not stack or stack[-1] != tag:
                return False
            stack.pop()
    return len(stack) == 0

def main():
    html_dir = "."  # Usa la carpeta actual
    archivos = sorted(f for f in os.listdir(html_dir) if f.endswith(".html"))

    for archivo in archivos:
        with open(os.path.join(html_dir, archivo), encoding='utf-8') as f:
            html = f.read()

        enlaces, imagenes = parse_html(html)
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
