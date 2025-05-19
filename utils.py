import os

def guardar_urls(nombre_archivo, enlaces, imagenes):
    base = os.path.splitext(os.path.basename(nombre_archivo))[0]
    ruta = f"resultados/{base}_urls.txt"
    os.makedirs("resultados", exist_ok=True)
    
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("ENLACES:\n")
        for link in enlaces:
            f.write(f"{link}\n")
        f.write("\nIMÁGENES:\n")
        for img in imagenes:
            f.write(f"{img}\n")
