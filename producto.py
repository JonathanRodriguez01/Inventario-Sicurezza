# producto.py

class Producto:
    def __init__ (self, nombre: str, categoria: str, precio_costo: float, precio_lista: float, stock: int):
        self.nombre = nombre
        self.categoria = categoria
        self.precio_costo = precio_costo
        self.precio_lista = precio_lista
        self.stock = stock

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio_costo": self.precio_costo,
            "precio_lista": self.precio_lista,
            "stock": self.stock
        }
    
    @staticmethod
    def from_dict(data: dict):
        return Producto(
            nombre = data["nombre"],
            categoria = data["categoria"],
            precio_costo = data["precio_costo"],
            precio_lista = data["precio_lista"],
            stock = data["stock"]
        )    
    
