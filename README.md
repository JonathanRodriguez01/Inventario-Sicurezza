# 🛠️ Sistema de Inventario - Sicurezza

Este proyecto es un sistema de gestión de inventario básico desarrollado en Python como parte del curso **Python Full Stack + FastAPI** del ITU UNCuyo.

Permite crear, ver, editar y eliminar productos, guardar los datos en un archivo JSON, y exportarlos a un archivo CSV para su análisis.

---

## 🚀 Funcionalidades

- ✅ Crear productos  
- 📋 Ver productos cargados  
- ✏️ Editar productos existentes  
- 🗑️ Eliminar productos  
- 💾 Guardar automáticamente los productos en un archivo `productos.json`  
- 📤 Exportar los productos a un archivo CSV en la carpeta `output/`  

---

## ⚙️ Tecnologías y dependencias

- Python 3.10+
- [`termcolor`](https://pypi.org/project/termcolor/) para colorear la salida en consola

Instalación con pip:

```bash
pip install termcolor

🧱 Estructura del proyecto
📁 controllers/
    └── inventario.py
📁 helpers/
    ├── utils.py
    ├── utils_json.py
    └── converter.py
📁 output/
    └── productos.csv (se genera automáticamente)
📄 producto.py
📄 main.py
📄 .gitignore
📄 README.md
📄 productos.json

📦 Requisitos del sistema
Python 3.10 o superior

Git instalado (opcional)

🧪 Cómo ejecutar el proyecto
1. Crear entorno virtual
python -m venv venv

2. Activar entorno virtual
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3. Instalar dependencias
pip install -r requirements.txt

Si no tenés un archivo requirements.txt, podés instalar manualmente:
pip install termcolor

4. Ejecutar la app
python main.py

📝 Consideraciones
Todos los datos se guardan en el archivo productos.json.

El archivo CSV se genera automáticamente dentro de output/ al salir del programa.

El proyecto sigue los principios básicos de la programación orientada a objetos (POO).

🧾 .gitignore
El archivo .gitignore evita que archivos innecesarios se suban a GitHub. Incluye exclusiones para:

output/*.csv y productos.json

__pycache__/ y archivos .pyc

Carpetas de entornos virtuales venv/, env/

Archivos del sistema como .DS_Store

🧑‍💻 Autor
JonathanRodriguez01
Desarrollador en formación y Emprendedor.
www.linkedin.com/in/jonathan-rodríguez-642580251

