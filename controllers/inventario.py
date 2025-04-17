from helpers.utils_json import read_json_file, write_json_file
from termcolor import colored
from producto import Producto
from helpers.utils import calcular_precio_venta

productos = []  # Lista global de productos

# Cargar productos desde el archivo JSON
def cargar_productos():
    global productos
    try:
        productos = read_json_file("productos.json")
        if not productos:
            print(colored("📂 No se encontraron productos en el archivo, comenzamos con un inventario vacío.", "yellow"))
        else:
            print(colored(f"📂 Productos cargados desde archivo: {len(productos)} productos.", "green"))
    except Exception as e:
        print(f"⚠️ Error al cargar los productos: {e}")
        print("Comenzando con inventario vacío.")

# Función para guardar productos antes de salir
def guardar_productos():
    try:
        write_json_file("productos.json", productos)
        print(colored("✅ Los productos han sido guardados correctamente.", "green"))
    except Exception as e:
        print(f"⚠️ Error al guardar los productos: {e}")

# Crear un producto desde la entrada del usuario
def crear_producto_desde_input():
    try:
        nombre = input("📦 Nombre del producto: ")
        categoria = input("🏷️  Categoría del producto: ")

        precio_costo = float(input("💰 Precio de costo: "))
        if precio_costo <= 0:
            print("⚠️ El precio de costo debe ser mayor que cero.")
            return None

        precio_lista = calcular_precio_venta(precio_costo)
        print(f"💡 Precio de lista (con 100% de ganancia): ${precio_lista:.2f}")

        stock = int(input("📦 Stock disponible: "))
        return Producto(nombre, categoria, precio_lista, stock)

    except ValueError:
        print("⚠️  Entrada inválida. Intenta nuevamente.")
        return None

# Mostrar todos los productos
def mostrar_productos(lista_productos):
    if not lista_productos:
        print(colored("📭 No hay productos en el inventario.", "yellow"))
        return

    for idx, prod in enumerate(lista_productos, start=1):
        print(colored(f"{idx}. {prod.nombre} - {prod.categoria} - ${prod.precio_costo:.2f} - Stock: {prod.stock}", "cyan"))

# Editar un producto existente
def editar_producto(lista_productos):
    mostrar_productos(lista_productos)
    try:
        indice = int(input("🔧 Ingrese el número del producto que desea editar: ")) - 1
        if 0 <= indice < len(lista_productos):
            producto = lista_productos[indice]
            print(f"✏️ Editando: {producto.nombre}")

            nuevo_nombre = input("Nuevo nombre (dejar vacío para mantener): ")
            nueva_categoria = input("Nueva categoría (dejar vacío para mantener): ")
            nuevo_precio = input("Nuevo precio de costo (dejar vacío para mantener): ")
            nuevo_stock = input("Nuevo stock (dejar vacío para mantener): ")

            if nuevo_nombre:
                producto.nombre = nuevo_nombre
            if nueva_categoria:
                producto.categoria = nueva_categoria
            if nuevo_precio:
                precio = float(nuevo_precio)
                producto.precio_costo = calcular_precio_venta(precio)
            if nuevo_stock:
                producto.stock = int(nuevo_stock)

            print(colored("✅ Producto actualizado.", "green"))
        else:
            print(colored("❌ Índice fuera de rango.", "red"))
    except ValueError:
        print(colored("⚠️ Entrada inválida.", "red"))

# Eliminar un producto del inventario
def eliminar_producto(lista_productos):
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

# Función principal del menú
def mostrar_menu():
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
            guardar_productos()
            print(colored("👋 Saliendo del programa...", "magenta"))
            break
        else:
            print(colored("❌ Opción inválida. Intenta de nuevo.", "red"))
