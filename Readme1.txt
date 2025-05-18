Práctica: Analizador léxico y verificador de HTML con PLY

Autor/a:María Arribas Ballesteros
Asignatura: Teoría de la Computación
Curso: 2024-2025

-------------------------------------------
 DESCRIPCIÓN DEL PROYECTO
-------------------------------------------

Este proyecto implementa un analizador de páginas HTML que permite:

- Extraer todas las URLs de los enlaces (<a href="...">)
- Extraer todas las URLs de las imágenes (<img src="...">)
- Verificar si el documento HTML está bien balanceado
  (es decir, si todas las etiquetas que se abren también se cierran correctamente)

-------------------------------------------
 TECNOLOGÍAS Y MÉTODOS UTILIZADOS
-------------------------------------------

 Analizador léxico implementado con PLY (Python Lex-Yacc):
   - Se han definido reglas léxicas personalizadas para detectar tokens `href`, `src` y `URL`.
   - El lexer analiza carácter a carácter el texto HTML y genera los tokens necesarios.

 Verificación de etiquetas balanceadas:
   - Implementada con expresiones regulares y una estructura de pila.
   - El código identifica las etiquetas de apertura y cierre, y utiliza una pila para comprobar el correcto anidamiento.
   - Se ignoran etiquetas autoconclusivas como `<br>`, `<img>`, `<hr>`, etc.

 No se han utilizado librerías externas como BeautifulSoup ni parsers automáticos de HTML.

-------------------------------------------
 ARCHIVOS INCLUIDOS
-------------------------------------------

- `main.py`        → Ejecuta el análisis completo de los archivos HTML.
- `lexer.py`       → Define los tokens necesarios usando PLY.
- `parser.py`      → Implementa la función de verificación de etiquetas balanceadas.
- `prueba1.html` a `prueba6.html` → Archivos HTML reales de prueba.
- `README.txt`     → Este documento explicativo.

-------------------------------------------
 INSTRUCCIONES DE USO
-------------------------------------------

1. Asegúrate de tener instalado Python 3.11 y el módulo PLY.
   Puedes instalar PLY ejecutando:
   > py -3.11 -m pip install ply

2. Ejecuta el programa principal:
   > py -3.11 main.py

3. El programa analizará todos los archivos `.html` en la carpeta,
   extraerá los enlaces e imágenes, y mostrará si cada archivo está bien balanceado.

