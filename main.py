import os
from lexer import lexer
from parser import parser, stack

# Lista de archivos
archivos = [f"prueba{i}.html" for i in range(1, 7)]

for archivo in archivos:
    print("=" * 60)
    print(f"Analizando: {archivo}")

    with open(archivo, encoding='utf-8') as f:
        data = f.read()

    # Reset de resultados
    urls = []
    imagenes = []
    stack.clear()

    # Análisis léxico
    lexer.input(data)
    while tok := lexer.token():
        if tok.type == 'HREF':
            urls.append(tok.value)
        elif tok.type == 'SRC':
            imagenes.append(tok.value)

    # Mostrar resultados
    print("\nHipervínculos encontrados:")
    for url in urls:
        print(" -", url)

    print("\nImágenes encontradas:")
    for img in imagenes:
        print(" -", img)

    # Análisis sintáctico (balanceo)
    print("\nChequeando balanceo del HTML...")
    parser.parse(data)
    print("\n")
