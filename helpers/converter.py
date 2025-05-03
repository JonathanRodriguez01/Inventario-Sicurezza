"""
Funciones para conversión de datos entre formatos.

Incluye la función dict_a_producto para reconstruir objetos Producto
desde diccionarios, y exportar productos a CSV.
"""

from producto import Producto

def dict_a_producto(diccionario):
    """
    Convierte un diccionario en una instancia de la clase Producto.

    Parámetros:
    diccionario (dict): Diccionario con las claves 'nombre', 'categoria',
                        'precio_costo', 'precio_lista' y 'stock'.

    Retorna:
    Producto: Una instancia de Producto con los valores del diccionario.
    """
    return Producto(
        nombre=diccionario["nombre"],
        categoria=diccionario["categoria"],
        precio_costo=diccionario["precio_costo"],
        precio_lista=diccionario["precio_lista"],
        stock=diccionario["stock"]
    )
