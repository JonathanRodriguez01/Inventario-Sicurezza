"""
Este archivo contiene las funciones relacionadas con la gestión del inventario.
Incluye funcionalidades CRUD (crear, leer, actualizar, eliminar) para los productos
y la persistencia de los mismos en un archivo JSON.

Autor: Jonathan Rodríguez
"""

from json import JSONDecodeError  # Standard library
from termcolor import colored     # Third-party library

# First-party (proyecto)
from helpers.utils_json import read_json_file, write_json_file
from helpers.utils import calcular_precio_venta
from helpers.converter import dict_a_producto
from producto import Producto

def crear_productos():
    """
    Carga los productos desde un archivo JSON.

    Retorna:
        list: Lista de objetos Producto cargados desde el archivo.
    """
    try:
        productos_dict = read_json_file("productos.json")
        if not productos_dict:
            print(colored(
                "📂 No se encontraron productos en el archivo. "
                "Comenzamos con un inventario vacío.", 
                "yellow"
            ))
            return []
        productos = [dict_a_producto(prod_dict) for prod_dict in productos_dict]
        print(colored(
            f"📂 Productos cargados desde archivo: {len(productos)} productos.",
            "green"
        ))
        return productos
    except JSONDecodeError:
        print(colored("❌ Error: El archivo JSON está corrupto o mal formado.", "red"))
        return []
    except OSError as e:
        print(colored(f"❌ Error de lectura de archivo: {e}", "red"))
        return []

def guardar_productos(productos):
    """
    Guarda la lista de productos en un archivo JSON.

    Parámetros:
        productos (list): Lista de objetos Producto a guardar.
    """
    try:
        write_json_file("productos.json", productos)
        print(colored("✅ Los productos han sido guardados correctamente.", "green"))
    except OSError as e:
        print(colored(f"❌ Error al acceder al archivo para guardar: {e}", "red"))
    except TypeError as e:
        print(colored(f"❌ Error de datos al guardar productos: {e}", "red"))

def crear_producto_desde_input():
    """
    Solicita datos al usuario para crear un nuevo producto.

    Retorna:
        Producto: Objeto Producto creado, o None si hubo un error.
    """
    try:
        nombre = input("📦 Nombre del producto: ").strip()
        if not nombre:
            print("⚠️ El nombre no puede estar vacío")
            return None
        categoria = input("🏷️  Categoría del producto: ").strip()
        if not categoria:
            print("⚠️ La categoría no puede estar vacía")
            return None

        precio_costo = float(input("💰 Precio de costo: "))
        if precio_costo <= 0:
            print("⚠️ El precio de costo debe ser mayor que cero.")
            return None

        precio_lista = calcular_precio_venta(precio_costo)
        print(f"💡 Precio de lista (con 100% de ganancia): ${precio_lista:.2f}")

        stock = int(input("📦 Stock disponible: "))

        if stock < 0:
            print("⚠️ El stock no puede ser negativo")
            return None
        return Producto(nombre, categoria, precio_costo, precio_lista, stock)

    except ValueError:
        print("⚠️  Entrada inválida. Intenta nuevamente.")
        return None

def mostrar_productos(lista_productos):
    """
    Muestra por consola todos los productos del inventario.

    Parámetros:
        lista_productos (list): Lista de objetos Producto a mostrar.
    """
    if not lista_productos:
        print(colored("📭 No hay productos en el inventario.", "yellow"))
        return

    for idx, prod in enumerate(lista_productos, start=1):
        print(colored(
            f"📦 {idx}. {prod.nombre} - {prod.categoria}\n"
            f"   💰 Costo: ${prod.precio_costo:.2f} | 🏷️ Lista: ${prod.precio_lista:.2f}\n"
            f"   📊 Stock: {prod.stock}",
            "cyan"
        ))

def editar_producto(lista_productos):
    """
    Permite al usuario modificar un producto del inventario.

    Parámetros:
        lista_productos (list): Lista de productos existentes.
    """
    mostrar_productos(lista_productos)
    try:
        indice = int(input("🔧 Ingrese el número del producto que desea editar: ")) - 1
        if 0 <= indice < len(lista_productos):
            producto = lista_productos[indice]
            print(f"✏️ Editando: {producto.nombre}")

            nuevo_nombre = input("Nuevo nombre (dejar vacío para mantener): ").strip()
            nueva_categoria = input("Nueva categoría (dejar vacío para mantener): ").strip()
            nuevo_precio = input("Nuevo precio de costo (dejar vacío para mantener): ").strip()
            nuevo_stock = input("Nuevo stock (dejar vacío para mantener): ").strip()

            if nuevo_nombre:
                producto.nombre = nuevo_nombre
            if nueva_categoria:
                producto.categoria = nueva_categoria
            if nuevo_precio:
                try:
                    precio = float(nuevo_precio)
                    if precio <= 0:
                        print("⚠️ El precio debe ser mayor que cero. No se actualizó el precio.")
                    else:
                        producto.precio_costo = precio
                        producto.precio_lista = calcular_precio_venta(precio)
                except ValueError:
                    print("⚠️ Precio inválido. No se actualizó el precio.")
            if nuevo_stock:
                try:
                    stock = int(nuevo_stock)
                    if stock < 0:
                        print("⚠️ El stock no puede ser negativo. No se actualizó el stock.")
                    else:
                        producto.stock = stock
                except ValueError:
                    print("⚠️ Stock inválido. No se actualizó el stock.")

            print(colored("✅ Producto actualizado.", "green"))
        else:
            print(colored("❌ Índice fuera de rango.", "red"))
    except ValueError:
        print(colored("⚠️ Entrada inválida.", "red"))

def eliminar_producto(lista_productos):
    """
    Permite eliminar un producto del inventario por su índice.

    Parámetros:
        lista_productos (list): Lista de productos existentes.
    """
    mostrar_productos(lista_productos)
    try:
        indice = int(input("🗑️ Ingrese el número del producto a eliminar: ")) - 1
        if 0 <= indice < len(lista_productos):
            eliminado = lista_productos.pop(indice)
            print(colored(f"🗑️ Producto '{eliminado.nombre}' eliminado.", "green"))
        else:
            print(colored("❌ Índice fuera de rango.", "red"))
    except ValueError:
        print(colored("⚠️ Entrada inválida.", "red"))

def mostrar_menu(productos):
    """
    Muestra el menú principal de opciones y gestiona la navegación del usuario.

    Parámetros:
        productos (list): Lista de productos actual que se modifica durante la ejecución.
    """
    while True:
        print("\n" + colored("📋 Menú de opciones:", "cyan"))
        print(colored("1. Crear producto", "green"))
        print(colored("2. Ver productos", "yellow"))
        print(colored("3. Editar producto", "blue"))
        print(colored("4. Eliminar producto", "red"))
        print(colored("0. Salir", "magenta"))

        opcion = input("Seleccionar una opción: ")

        if opcion == "1":
            producto = crear_producto_desde_input()
            if producto:
                productos.append(producto)
                print(colored("✅ Producto creado y cargado al inventario.", "green"))
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            editar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "0":
            guardar_productos(productos)
            print(colored("👋 Saliendo del programa...", "magenta"))
            break
        else:
            print(colored("❌ Opción inválida. Intenta de nuevo.", "red"))
