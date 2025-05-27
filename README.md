# Practica_teoria_computacion

María Arribas Ballesteros, 3ª Ingeniería Matemática


# Proyecto Extracción y Análisis de URLs en HTML

Este proyecto permite extraer URLs de enlaces e imágenes desde documentos HTML y páginas web reales mediante dos métodos distintos:

- **BeautifulSoup:** Análisis flexible y tolerante, ideal para extracción rápida y manejo general de HTML.
- **PLY (Lexer + Parser):** Análisis sintáctico más riguroso, que además verifica el balanceo y la corrección estructural del HTML.

---

## Archivos principales

- bs4_extractor.py  
  Script que utiliza BeautifulSoup para analizar HTML y extraer URLs.  
  **Uso:** Ejecutar para obtener enlaces, imágenes y estadísticas de etiquetas mediante este método.

- main.py  
  Script que utiliza PLY (lexer y parser) para un análisis más exhaustivo que incluye detección de errores estructurales y balanceo.  
  **Uso:** Ejecutar para análisis detallado y validación sintáctica.

---

## Requisitos previos

- Python 3.x instalado.
- Librerías necesarias:

  Para BeautifulSoup: pip install requests beautifulsoup4

  
Para PLY (si no está instalado): pip install ply


- Asegúrate de que los archivos lexer.py y parser.py estén en el mismo directorio que main.py.

---

## Instrucciones de ejecución

### Análisis con BeautifulSoup

1. Ejecuta el script: bs4_extractor.py


2. El programa analizará URLs definidas y archivos HTML locales, mostrando por consola los enlaces, imágenes y estadísticas de etiquetas.

3. Los resultados se guardarán en el archivo `urls_bs4_extraidas.txt`.

---

### Análisis con PLY

1. Ejecuta el script: main.py


2. El programa analizará las mismas URLs y archivos HTML, pero realizará además una comprobación del balanceo y reportará errores estructurales.

3. Los resultados y errores se mostrarán por consola y se guardarán en `urls_extraidas.txt`.

---

## Descripción general

- Ambos métodos permiten evaluar el contenido HTML desde fuentes locales o en línea.
- BeautifulSoup es más tolerante a errores de sintaxis HTML y corrige internamente, por lo que no reporta errores de balanceo.
- PLY ofrece un análisis detallado que detecta inconsistencias en la estructura del HTML.
- Se recomienda usar ambos métodos para un análisis complementario: BeautifulSoup para extracción rápida y PLY para validación estructural.

---

## Estructura de archivos

/proyecto/
├── bs4_extractor.py
├── main.py
├── lexer.py
├── parser.py
├── prueba1.html
├── prueba2.html
├── prueba3.html
├── prueba4.html
├── prueba5.html
├── prueba6.html
└── README.md

---