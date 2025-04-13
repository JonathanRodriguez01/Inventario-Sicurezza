
from producto import Producto

productos = [] # Lista para guardar productos temporalmente.

def crear_producto_desde_input():
    try:
        nombre = input("Nombre del producto: ")
        categoria = input("Categoria del producto: ")
        precio_lista = float(input("Ingrese precio de lista: "))
        stock = int(input("stock disponible: "))
        return Producto(nombre, categoria, precio_lista, stock)
    except ValueError:
        print("⚠️  Error: Ingresaste un valor inválido. Intenta nuevamente.")
        return None
    
def mostrar_productos():
    if not productos:
        print("📭No hay productos registrados.")
        return
    print("📦Productos registrados: ")
    for i, p in enumerate(productos, start=1):
        print(f"{i}. {p.nombre} | categoría: {p.categoria} | Precio de lista: ${p.precio_lista} | Stock: {p.stock}")

def mostrar_menu():
    while True:
        print("\n📋 Menu de opciones:")
        print("1.Crear producto")
        print("2.Ver productos")
        print("0.Salir")

        opcion= input("Seleccionar una opción: ")
        if opcion == "1":
            producto = crear_producto_desde_input()
            if producto is not None:
                productos.append(producto)
                print("✅producto creado y cargado al inventario.")
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "0":
            print("👋Saliendo del programa...")
            break
        else:
            print("❌Opcion inválida. Intenta de nuevo.")             

if __name__ == "__main__":
    mostrar_menu()