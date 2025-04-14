# Importamos el menu de opciones

from controllers.inventario import (
    crear_producto_desde_input,
    mostrar_productos,
    editar_producto,
    eliminar_producto
)

productos = []  # Lista para guardar productos

def mostrar_menu():
    while True:
        print("\n📋 Menú de opciones:")
        print("1. Crear producto")
        print("2. Ver productos")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("0. Salir")

        opcion = input("Seleccionar una opción: ")

        if opcion == "1":
            producto = crear_producto_desde_input()
            if producto:
                productos.append(producto)
                print("✅ Producto creado.")
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            editar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    mostrar_menu()