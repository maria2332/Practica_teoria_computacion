from lexer import lexer
from parser import parser, stack

archivos = [
    "prueba1.html",
    "prueba4.html",
    "prueba6.html"
]

for archivo in archivos:
    print("=" * 60)
    print(f"📄 Analizando: {archivo}")

    with open(archivo, encoding="utf-8") as f:
        data = f.read()

    # Reset para cada archivo
    urls = []
    imagenes = []
    stack.clear()

    # Lexer: Extraer href y src
    lexer.input(data)
    while tok := lexer.token():
        if tok.type == 'HREF':
            urls.append(tok.value)
        elif tok.type == 'SRC':
            imagenes.append(tok.value)

    print("\n🔗 Enlaces encontrados:")
    for u in urls:
        print(f" - {u}")

    print("\n🖼️ Imágenes encontradas:")
    for img in imagenes:
        print(f" - {img}")

    print("\n📐 Comprobando balanceo de etiquetas...")
    parser.parse(data)
    print("\n")
