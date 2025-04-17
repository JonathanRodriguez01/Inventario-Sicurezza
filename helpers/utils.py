def calcular_precio_venta(precio_costo, margen=1.0):
    """
    Calcula el precio de venta a partir del precio de costo y el margen deseado.

    Args:
        precio_costo (float): Costo base del producto.
        margen (float): Margen de ganancia en decimales (0.5 = 50%).

    Returns:
        float: Precio de venta sugerido.
    """
    return round(precio_costo * (1 + margen), 2)
