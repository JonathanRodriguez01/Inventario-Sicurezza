from producto import Producto

def crear_producto_desde_input():
    try:
        nombre = input("Nombre del producto: ")
        categoria = input("Categoria del producto: ")
        precio_lista = float(input("Ingrese precio de lista: "))
        stock = int(input("Stock disponible: "))
        return Producto(nombre, categoria, precio_lista, stock)
    except ValueError:
        print("⚠️  Error: Ingresaste un valor inválido. Intenta nuevamente.")
        return None

def mostrar_productos(productos):
    if not productos:
        print("📭 No hay productos registrados.")
        return
    print("📦 Productos registrados:")
    for i, p in enumerate(productos, start=1):
        print(f"{i}. {p.nombre} | Categoría: {p.categoria} | Precio de lista: ${p.precio_lista} | Stock: {p.stock}")

def editar_producto(productos):
    mostrar_productos(productos)
    try:
        indice = int(input("🔧 Ingrese el número del producto que desea editar: ")) - 1
        if 0 <= indice < len(productos):
            producto = productos[indice]
            print(f"✏️ Editando: {producto.nombre}")
            
            nuevo_nombre = input("Nuevo nombre (dejar vacío para mantener): ")
            nueva_categoria = input("Nueva categoría (dejar vacío para mantener): ")
            nuevo_precio = input("Nuevo precio de lista (dejar vacío para mantener): ")
            nuevo_stock = input("Nuevo stock disponible (dejar vacío para mantener): ")

            if nuevo_nombre:
                producto.nombre = nuevo_nombre
            if nueva_categoria:
                producto.categoria = nueva_categoria
            if nuevo_precio:
                producto.precio_lista = float(nuevo_precio)
            if nuevo_stock:
                producto.stock = int(nuevo_stock)

            print("✅ Producto actualizado con éxito.")
        else:
            print("❌ Índice fuera de rango.")
    except ValueError:
        print("⚠️ Entrada inválida.")

def eliminar_producto(productos):
    mostrar_productos(productos)
    try:
        indice = int(input("🗑️ Ingrese el número del producto que desea eliminar: ")) - 1
        if 0 <= indice < len(productos):
            eliminado = productos.pop(indice)
            print(f"🗑️ Producto '{eliminado.nombre}' eliminado del inventario.")
        else:
            print("❌ Índice fuera de rango.")
    except ValueError:
        print("⚠️ Entrada inválida.")
