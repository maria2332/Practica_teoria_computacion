from lexer import lexer
from parser import parser

# Carga HTML de prueba
with open("test_page.html", encoding='utf-8') as f:
    data = f.read()

# Lexer: extraer URLs
lexer.input(data)
urls = []
images = []

while tok := lexer.token():
    if tok.type == 'HREF':
        urls.append(tok.value)
    elif tok.type == 'SRC':
        images.append(tok.value)

print("Hipervínculos encontrados:")
for url in urls:
    print(" -", url)

print("\nImágenes encontradas:")
for img in images:
    print(" -", img)

# Parser: balanceo
print("\nChequeando balanceo del HTML...")
parser.parse(data)
