Evaluación 3 - PROGRAMACION WEB - FLASK

REQUISITOS
- Python instalado
- Flask

EJECUCION EN WINDOWS
1. Abre esta carpeta en Visual Studio Code.
2. Abre la terminal en la carpeta del proyecto.
3. (Recomendado) Crea el entorno virtual:
   python -m venv venv
4. Activa el entorno:
   venv\Scripts\activate
5. Instala Flask:
   pip install -r requirements.txt
6. Ejecuta:
   python main.py
7. Abre en el navegador:
   http://127.0.0.1:5000

ESTRUCTURA
Belen Aravena_EVA3/
  main.py
  requirements.txt
  README.txt
  templates/
    index.html
    ejercicio1.html
    ejercicio2.html
  static/
    estilos.css

EJERCICIO 1
Recibe tres notas entre 10 y 70 y asistencia entre 0 y 100.
Calcula el promedio. Aprueba solo si promedio >= 40 y asistencia >= 75.

EJERCICIO 2
Recibe tres nombres distintos e informa el/los de mayor longitud
y la cantidad de caracteres.

GITHUB
Desde la terminal, dentro de esta carpeta:
git init
git add .
git commit -m "Entrega TA6 Flask"
Crea un repositorio nuevo en GitHub y sigue las instrucciones que GitHub
muestre para conectar el repositorio local y subirlo.
