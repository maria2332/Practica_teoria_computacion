from parser import parse_html, is_html_balanced
import os

def analizar_archivo(filename):
    with open(filename, "r", encoding="utf-8") as f:
        contenido = f.read()

    enlaces, imagenes, errores = parse_html(contenido)

    print(f"\n🧪 {os.path.basename(filename)}\n")

    print(f"Enlaces (<a href=...>): {len(enlaces)}")
    for e in enlaces:
        print(f'<a href="{e}"> → ✅ Correcto')

    print(f"\nImágenes (<img src=...>): {len(imagenes)}")
    for i in imagenes:
        print(f'<img src="{i}"> → ✅ Correcto')

    if is_html_balanced():
        print("\nBalanceado: ✅ Sí")
    else:
        print("\nBalanceado: ❌ No")
        print(" - Errores detectados:")
        for err in errores:
            print(f" - {err}")

if __name__ == "__main__":
    print("🔍 Iniciando análisis de HTMLs...")
    for i in range(1, 7):
        analizar_archivo(f"prueba{i}.html")
