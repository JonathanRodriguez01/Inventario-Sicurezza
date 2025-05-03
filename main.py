"""
Este archivo es el punto de entrada del sistema de inventario.
Gestiona el ciclo de vida de los productos, incluyendo su carga desde un archivo JSON,
las operaciones CRUD y la exportación de datos a formato CSV.

Autor: Jonathan Rodríguez
"""

import csv  # Biblioteca estándar
from termcolor import colored  # Import de terceros

from controllers.inventario import crear_productos, mostrar_menu  # Import local
from helpers.utils_json import write_json_file


def exportar_a_csv(productos):
    """
    Exporta la lista de productos a un archivo CSV en la carpeta 'output'.

    Parámetros:
        productos (list): Lista de objetos Producto a exportar.
    """
    try:
        with open('output/inventario.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow(["Nombre", "Categoría", "Precio Costo", "Precio Lista", "Stock"])

            for producto in productos:
                writer.writerow([
                    producto.nombre,
                    producto.categoria,
                    producto.precio_costo,
                    producto.precio_lista,
                    producto.stock
                ])
        print(colored("✅ Inventario exportado a CSV en la carpeta 'output'.", "green"))
    except OSError as e:
        print(f"⚠️ Error al exportar a CSV: {e}")

# Función principal
def main():
    """
    Función principal para gestionar el inventario. 
    Carga los productos desde un archivo JSON, permite gestionar el inventario,
    guardar los productos actualizados en un archivo JSON y exportar el inventario
    a un archivo CSV.

    Retorna:
        None
    """
    # Cargar productos desde archivo JSON (debe llamarse crear_productos)
    productos = crear_productos()

    # Mostrar el menú de opciones para gestionar productos
    mostrar_menu(productos)

    # Guardar los productos en formato JSON
    dicts_para_guardar = [producto.to_dict() for producto in productos]
    write_json_file("productos.json", dicts_para_guardar)

    # Exportar productos a formato CSV
    exportar_a_csv(productos)

    print(colored("✅ Inventario guardado. ¡Hasta luego!", "green"))


if __name__ == "__main__":
    main()
