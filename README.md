# 🛠️ Sistema de Inventario - Sicurezza

Este proyecto es un sistema de gestión de inventario básico desarrollado en Python como parte del curso **Python Full Stack + FastAPI** del ITU UNCuyo.

Permite **crear, ver, editar y eliminar productos**, guardar los datos en un archivo JSON y exportarlos a un archivo CSV para su análisis.

---

## 🚀 Funcionalidades

- ✅ Crear productos  
- 📋 Ver productos cargados  
- ✏️ Editar productos existentes  
- 🗑️ Eliminar productos  
- 💾 Guardado automático en `productos.json`  
- 📤 Exportación automática a `output/productos.csv` al finalizar

---

## ⚙️ Tecnologías y dependencias

- Python 3.10+
- [`termcolor`](https://pypi.org/project/termcolor/) – Colores en consola

### 📦 Instalación rápida

```bash
pip install termcolor

🧱 Estructura del proyecto
.
├── controllers/
│   └── inventario.py
├── helpers/
│   ├── utils.py
│   ├── utils_json.py
│   └── converter.py
├── models/
│   └── producto.py
├── output/
│   └── productos.csv  ← Se genera automáticamente
├── main.py
├── productos.json     ← Datos persistentes
├── README.md
├── .gitignore

🧪 Cómo ejecutar el proyecto
Crear entorno virtual:
python -m venv venv

Activar entorno virtual:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Instalar dependencias:
pip install termcolor

Ejecutar la app:
python main.py

📝 Consideraciones
Todos los productos se guardan en productos.json

El CSV se genera automáticamente al salir del programa

El proyecto sigue principios básicos de Programación Orientada a Objetos

🧑‍💻 Autor
JonathanRodriguez01
Desarrollador en formación y Emprendedor.
www.linkedin.com/in/jonathan-rodríguez-642580251

