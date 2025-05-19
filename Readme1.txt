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


-------------------------------------------
 CONCLUSIONES
-------------------------------------------

 El analizador léxico construido con PLY ha sido eficaz para identificar correctamente las etiquetas <a> y <img>, así como para extraer las URLs contenidas en sus atributos href y src.

 El sistema funciona de forma robusta incluso con archivos HTML reales y complejos (como el de Amazon), lo que demuestra que las reglas léxicas diseñadas capturan adecuadamente los patrones relevantes en el texto.

 El verificador de balanceo de etiquetas basado en expresiones regulares y una pila ha permitido detectar correctamente si las etiquetas HTML están bien anidadas y cerradas, sin necesidad de librerías externas.

 Se han identificado correctamente casos mal formateados (como prueba4.html o prueba5.html), donde las etiquetas estaban anidadas de forma incorrecta o mal cerradas, y el programa ha señalado estos como no balanceados, cumpliendo el objetivo de validación sintáctica.

 El sistema ha mostrado que puede distinguir entre HTML balanceado y mal estructurado de forma fiable, aunque no realiza un parseo completo del árbol DOM (lo cual no era necesario para los objetivos de esta práctica).

 No se ha utilizado ningún parser automático como html.parser, BeautifulSoup o similares, cumpliendo estrictamente el uso de análisis léxico personalizado y estructuras clásicas como la pila.

