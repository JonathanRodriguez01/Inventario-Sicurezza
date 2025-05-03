"""
Este archivo contiene funciones para leer y escribir datos en archivos JSON.
Es utilizado para cargar y guardar el inventario de productos en formato JSON.

Autor: Jonathan Rodríguez
"""

import json
from termcolor import cprint

def read_json_file(filename):
    """
    Lee datos desde un archivo JSON.

    Parámetros:
    filename (str): Ruta del archivo JSON a leer.

    Retorna:
    list: Lista de productos cargados desde el archivo. Si el archivo no existe
          o tiene errores de formato, retorna una lista vacía.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        cprint("⚠️ Archivo no encontrado. Se creará uno nuevo cuando guardes productos.", "yellow")
        return []
    except json.JSONDecodeError:
        cprint("❌ Error al leer el archivo JSON. Verifica su formato.", "red")
        return []


def write_json_file(filename, data):
    """
    Escribe datos en un archivo JSON.

    Parámetros:
    filename (str): Ruta del archivo JSON donde se guardarán los datos.
    data (list): Lista de diccionarios que representan los productos.

    Retorna:
    None
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        cprint("✅ Inventario guardado correctamente en archivo JSON.", "green")
    except (TypeError, OSError) as e:
        cprint(f"❌ Error al guardar el archivo: {e}", "red")
