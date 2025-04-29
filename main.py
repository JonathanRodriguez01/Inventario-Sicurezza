import csv
from controllers.inventario import cargar_productos, mostrar_menu
from helpers.utils_json import write_json_file
from termcolor import colored


# Función para exportar los productos a un archivo CSV
def exportar_a_csv(productos):
    try:
        # Definir la ruta donde se guardará el archivo CSV
        with open('output/inventario.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Escribir los encabezados
            writer.writerow(["Nombre", "Categoría", "Precio Costo", "Precio Lista", "Stock"])

            # Escribir los datos de los productos
            for producto in productos:
                writer.writerow([producto.nombre, producto.categoria, producto.precio_costo, producto.precio_lista, producto.stock])
                
        print(colored("✅ Inventario exportado a CSV en la carpeta 'output'.", "green"))
    except Exception as e:
        print(f"⚠️ Error al exportar a CSV: {e}")


# Función principal
def main():
    productos = cargar_productos()
    mostrar_menu(productos)

    # Guardar productos en formato JSON
    dicts_para_guardar = [producto.to_dict() for producto in productos]
    write_json_file("productos.json", dicts_para_guardar)

    # Exportar productos a CSV
    exportar_a_csv(productos)

    print(colored("✅ Inventario guardado. ¡Hasta luego!", "green"))


if __name__ == "__main__":
    main()
