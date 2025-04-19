from utilidades import Pizzas, ContenidoPedidos

def calcular_ganancia(pedido: ContenidoPedidos, dict_precios: dict) -> int:
    ganancia = ((dict_precios[pedido.nombre] * pedido.cantidad) * (1 - pedido.descuento))
    return int(round(ganancia))

def calcular_ahorro(pedido: ContenidoPedidos, dict_precios: dict) -> float:
    precio_total = dict_precios[pedido.nombre] * pedido.cantidad
    precio_con_descuento = precio_total * (1 - pedido.descuento)
    return precio_total - precio_con_descuento

def calcular_ganancia_total_pedido(pedido: ContenidoPedidos, dict_precios: dict) -> int:
    ganancia = ((dict_precios[pedido.nombre] * pedido.cantidad) * (1 - pedido.descuento))
    return ganancia