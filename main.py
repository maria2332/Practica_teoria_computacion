from lexer import lexer
from parser import parser, stack
from utils import guardar_urls

archivos = [f"prueba{i}.html" for i in range(1, 7)]

for archivo in archivos:
    print("=" * 60)
    print(f"📄 Analizando: {archivo}")

    try:
        with open(archivo, encoding="utf-8") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"⚠️ No se encontró el archivo: {archivo}")
        continue

    # Reinicio de estado
    enlaces = []
    imagenes = []
    stack.clear()

    # Lexer para extraer href y src
    lexer.input(data)
    while tok := lexer.token():
        if tok.type == 'HREF':
            enlaces.append(tok.value)
        elif tok.type == 'SRC':
            imagenes.append(tok.value)

    # Mostrar resultados
    print("\n🔗 Enlaces encontrados:")
    for link in enlaces:
        print(f" - {link}")

    print("\n🖼️ Imágenes encontradas:")
    for img in imagenes:
        print(f" - {img}")

    # Guardar en disco
    guardar_urls(archivo, enlaces, imagenes)

    # Comprobar balanceo
    print("\n📐 Comprobando balanceo...")
    parser.parse(data)
    print()
