# **Traductor - Large Language Model**
Un modelo de lenguaje a gran escala con una interfaz para poder interactuar con la misma, y realizada para presentar como trabajo final en la materia _Técnicas de Procesamiento del Habla_.

La app puede ser utilizada de manera local, y también estará desplegado en _Render_ para poder interactuar con el LLM basado en los motores de _Google Translator_ (de Google) y MyMemory (de Microsoft).

## 🏗️ **Estructura del Proyecto**
```text
.
├── static/                 # Se agregan los archivos .mp3 en esta carpeta
│
├── tests/                  # Experimentación y análisis de los motores
│   ├── README.md
│   ├── sesgo_ambigüedad.md
│   └── texto_corto.md
│
├── Procfile                # Comando para indicarle a Render como arrancar la aplicación
├── README.md               # Información sobre el repositorio
├── app.py                  # Archivo de python que consume un LLM
├── ejecutar.bat            # Abre la app.py de manera local
├── index.html              # Estructura base de la interfaz de la app.py
└── requirements.txt        # Requisitos (librerias) para utilizar el LLM

```
## 🛫 **Deployment del LLM**
### Opción 1: Abrir localmente
1. Hacer doble click en el archivo `ejecutar.bat`
   - Debería de aparecer el siguiente mensaje 
     ```
     * Serving Flask app 'app'
     * Debug mode: off
     WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
     Press CTRL+C to quit
     ```
     
2. Abrir el navegador e ir al sitio:
   `http://localhost:5000/`
   
### Opción 2: Abrir con Render
Enlace a la app desplegada en RENDER: https://tph-traductor.onrender.com/

## 🛠️ Herramientas

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://docs.python.org/es/3/)
[![edge-tts](https://img.shields.io/badge/edge--tts-0078D4?style=flat&logo=microsoftedge&logoColor=white)](https://pypi.org/project/edge-tts/)
[![deep-translator](https://img.shields.io/badge/deep--translator-4285F4?style=flat&logo=googletranslate&logoColor=white)](https://deep-translator.readthedocs.io/en/latest/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat\&logo=html5\&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/stable/)
[![Render](https://img.shields.io/badge/Render-000000?style=flat\&logo=render\&logoColor=white)](https://render.com/)
[![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat\&logo=googlegemini\&logoColor=white)](https://gemini.google.com/)
<!--
[![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-3776AB?style=flat\&logo=python\&logoColor=white)](https://pypi.org/project/SpeechRecognition/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat\&logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![os](https://img.shields.io/badge/os-3776AB?style=flat\&logo=python\&logoColor=white)](https://docs.python.org/es/3/library/os.html)
[![asyncio](https://img.shields.io/badge/asyncio-3776AB?style=flat&logo=python&logoColor=white)](https://docs.python.org/es/3/library/asyncio.html)
[![uuid](https://img.shields.io/badge/uuid-3776AB?style=flat&logo=python&logoColor=white)](https://docs.python.org/es/3/library/uuid.html)
[![glob](https://img.shields.io/badge/glob-3776AB?style=flat&logo=python&logoColor=white)](https://docs.python.org/3/library/glob.html)
-->

## 👥 **Autores**
- Arnaldo Antonio Fustet
- Uriel Maximiano Casas

<!--## ⚖️ **Licencia**
[MIT]()-->
