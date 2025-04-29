
from producto import Producto

def dict_a_producto(diccionario):
    return Producto(
        nombre=diccionario["nombre"],
        categoria=diccionario["categoria"],
        precio_costo=diccionario["precio_costo"],
        precio_lista=diccionario["precio_lista"],
        stock=diccionario["stock"]
    )
