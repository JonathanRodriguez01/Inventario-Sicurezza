# producto.py

class Producto:
    def __init__ (self, nombre: str, categoria: str, precio_lista: float, stock: int):
        self.nombre = nombre
        self.categoria = categoria
        self.precio_lista = precio_lista
        self.stock = stock

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio_lista": self.precio_lista,
            "stock": self.stock
        }