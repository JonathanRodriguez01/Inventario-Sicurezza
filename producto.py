"""
Este archivo contiene la definición de la clase Producto, que representa un producto
en el inventario. La clase incluye atributos como nombre, categoría, precio de costo,
precio de lista y stock, junto con métodos para interactuar con estos datos.

Autor: Jonathan Rodríguez
"""

class Producto:
    """
    Representa un producto del inventario de Sicurezza.
    """

    def __init__(
        self,
        nombre: str,
        categoria: str,
        precio_costo: float,
        precio_lista: float,
        stock: int
    ):
        """
        Inicializa un nuevo producto.

        Parámetros:
            nombre (str): Nombre del producto.
            categoria (str): Categoría del producto.
            precio_costo (float): Precio de costo del producto.
            precio_lista (float): Precio de venta sugerido.
            stock (int): Stock disponible del producto.
        """
        self.nombre = nombre
        self.categoria = categoria
        self.precio_costo = precio_costo
        self.precio_lista = precio_lista
        self.stock = stock

    def to_dict(self) -> dict:
        """
        Convierte el objeto Producto en un diccionario.

        Retorna:
            dict: Representación del producto como diccionario.
        """
        return {
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio_costo": self.precio_costo,
            "precio_lista": self.precio_lista,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Crea un objeto Producto a partir de un diccionario.

        Parámetros:
            data (dict): Diccionario con datos del producto.

        Retorna:
            Producto: Objeto Producto construido a partir del diccionario.
        """
        return Producto(
            nombre=data["nombre"],
            categoria=data["categoria"],
            precio_costo=data["precio_costo"],
            precio_lista=data["precio_lista"],
            stock=data["stock"]
        )
