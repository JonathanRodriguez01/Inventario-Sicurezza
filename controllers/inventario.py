from helpers.utils_json import read_json_file, write_json_file
from termcolor import colored
from producto import Producto
from helpers.utils import calcular_precio_venta
from helpers.converter import dict_a_producto

# Cargar productos desde el archivo JSON
def cargar_productos():
    try:
        productos_dict = read_json_file("productos.json")
        if not productos_dict:
            print(colored("📂 No se encontraron productos en el archivo, comenzamos con un inventario vacío.", "yellow"))
            return []
        else:
            productos = [dict_a_producto(prod_dict) for prod_dict in productos_dict]
            print(colored(f"📂 Productos cargados desde archivo: {len(productos)} productos.", "green"))
            return productos
    except Exception as e:
        print(f"⚠️ Error al cargar los productos: {e}")
        return []
# Función para guardar productos antes de salir
def guardar_productos(productos):
    try:
        write_json_file("productos.json", productos)
        print(colored("✅ Los productos han sido guardados correctamente.", "green"))
    except Exception as e:
        print(f"⚠️ Error al guardar los productos: {e}")

# Crear un producto desde la entrada del usuario
def crear_producto_desde_input():
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

        if stock <0:
            print("⚠️ El stock no puede ser negativo")
            return None
                    
        return Producto(nombre, categoria, precio_costo, precio_lista, stock)

    except ValueError:
        print("⚠️  Entrada inválida. Intenta nuevamente.")
        return None

# Mostrar todos los productos
def mostrar_productos(lista_productos):
    if not lista_productos:
        print(colored("📭 No hay productos en el inventario.", "yellow"))
        return

    for idx, prod in enumerate(lista_productos, start=1):
        print(colored(  f"📦 {idx}. {prod.nombre} - {prod.categoria}\n"
        f"   💰 Costo: ${prod.precio_costo:.2f} | 🏷️ Lista: ${prod.precio_lista:.2f}\n"
        f"   📊 Stock: {prod.stock}",
        "cyan"
    ))

# Editar un producto existente
def editar_producto(lista_productos):
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
def mostrar_menu(productos):
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

