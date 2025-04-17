
import json
from termcolor import cprint

def read_json_file(filename):
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
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        cprint("✅ Inventario guardado correctamente en archivo JSON.", "green")
    except (TypeError, OSError) as e:
        cprint(f"❌ Error al guardar el archivo: {e}", "red")
