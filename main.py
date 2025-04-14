# Importamos el menu de opciones

from controllers.inventario import (
    crear_producto_desde_input,
    mostrar_productos,
    editar_producto,
    eliminar_producto
)

productos = []  # Lista para guardar productos

from termcolor import colored

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
            print(colored("👋 Saliendo del programa...", "magenta"))
            break
        else:
            print(colored("❌ Opción inválida. Intenta de nuevo.", "red"))


if __name__ == "__main__":
    mostrar_menu()