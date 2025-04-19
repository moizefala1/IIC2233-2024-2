from typing import Any, Generator, Iterable
from utilidades import Pizzas, Locales, ContenidoPedidos, Pedidos
from itertools import cycle, islice, tee
from collections import defaultdict
from funciones_extra import calcular_ganancia, calcular_ahorro, calcular_ganancia_total_pedido
# Carga de datos

def cargar_pizzas(path: str) -> Generator:
    with open (path, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip().split(",")
            if linea[0] != "Nombre":
                yield Pizzas(linea[0], linea[1], int(linea[2]))

def cargar_locales(path: str) -> Generator:
        with open (path, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip().split(",")
                if linea[0] != "id_local":
                    yield Locales (int(linea[0]), linea[1], linea[2], 
                                   linea[3], int(linea[4]))

def cargar_pedidos(path: str) -> Generator:
        with open (path, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip().split(",")
                if linea[0] != "id_pedido":
                    yield Pedidos (int(linea[0]), int(linea[1]), int(linea[2]), 
                                   linea[3], linea[4])

def cargar_contenido_pedidos(path: str, ) -> Generator:
        with open (path, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip().split(",")
                if linea[0] != "id_pedido":
                    yield ContenidoPedidos (int(linea[0]), linea[1], 
                                            int(linea[2]), float(linea[3]))
                    
### Consultas que reciben un generador

def pedidos_con_al_menos_esta_pizza(
        generador_contenido_pedidos: Generator,
        tipo_de_pizza: str
        ) -> Iterable:
    lista = []
    for pedido in generador_contenido_pedidos:
        tipo_pizza_sin_tamano = pedido[1].split("_")[0]
        if tipo_de_pizza == tipo_pizza_sin_tamano:
            lista.append(pedido)
    return lista
        
def cantidad_vendida_de_pizza_por_tipo(
        generador_contenido_pedidos: Generator,
        tipo_de_pizza: str
        ) -> int:
    cant_pedidos = 0
    for pedido in generador_contenido_pedidos:
        tipo_pizza_sin_tamano = pedido[1].split("_")[0]
        if tipo_de_pizza == tipo_pizza_sin_tamano:
            cant_pedidos += 1 * pedido[2]
    return cant_pedidos

def pedido_con_mayor_descuento_utilizado(
        generador_contenido_pedidos: Generator
        ) -> Iterable:
    lista = []
    descuento_anterior = 0.0
    for pedido in generador_contenido_pedidos:
        if pedido[3] > descuento_anterior:
            descuento_anterior = pedido[3]
            lista = [pedido]
        elif pedido[3] == descuento_anterior:
            lista.append(pedido)
    return lista
    
def ajustar_precio_segun_ingredientes(
        generador_pizzas: Generator,
        ingrediente: str,
        diferencia_precio: int
        ) -> Iterable:
    pizzas_modificadas = []
    for pizza in generador_pizzas:
        ingredientes_pizza = pizza[1].split(";")
        if ingrediente in ingredientes_pizza:
            valor = pizza[2]
            valor_nuevo = valor + diferencia_precio
            if valor_nuevo < 7000:
                valor_nuevo = 7000
            pizza_nueva = Pizzas (pizza[0], pizza[1], valor_nuevo) 
            pizzas_modificadas.append(pizza_nueva)
    return pizzas_modificadas

def clientes_despues_hora(
        generador_pedidos: Generator,
        hora: str 
        ) -> str:
    def esta_en_rango(hora_pedido: str, hora_limite: int, minuto_limite: int) -> bool:
        hora_pedido_split = int(hora_pedido.split(':')[0])
        minuto_pedido_split = int(hora_pedido.split(':')[1])
        return ((hora_pedido_split > hora_limite) or
                (hora_pedido_split == hora_limite and minuto_pedido_split >= minuto_limite))
    lista = []
    hora_limite = int(hora.split(':')[0])
    minuto_limite = int(hora.split(":")[1])
    pedidos_en_rango = filter(lambda pedido: esta_en_rango(pedido.hora, hora_limite, 
                                                          minuto_limite), generador_pedidos)
    id_clientes = map(lambda pedido: pedido.id_cliente, pedidos_en_rango)
    
    for id in id_clientes:
        lista.append(str(id))
    return (" ".join(lista))

def cliente_indeciso(
        generador_pizzas: Generator,
        ingrediente_no_deseado: str,
        cantidad_pizzas: int
        ) -> Iterable:    
    generador1 , generador2 = tee(generador_pizzas, 2) 
    if all(ingrediente_no_deseado in pizza.ingredientes for pizza in generador1):
        return []
    pizzas_filtradas = filter(lambda pizza: ingrediente_no_deseado not in pizza[1], 
                              cycle(generador2)) 
    return list(islice(pizzas_filtradas, cantidad_pizzas))    

def pizzas_con_ingrediente(
        generador_pizzas: Generator,
        ingrediente: str
        ) -> Iterable:
    def tiene_ingrediente(pizza: Pizzas, ingrediente: str) -> bool:
        ingredientes = pizza.ingredientes.split(";")
        return ingrediente in ingredientes
    filtro = filter(lambda pizza: tiene_ingrediente(pizza, ingrediente), generador_pizzas)
    return list(filtro)

def pizzas_pagables_de_un_tamano(
        generador_pizzas: Generator,
        dinero: int,
        tamano: str
    ) -> Iterable:
    lista_pizzas = []
    for pizza in generador_pizzas:
       tamano_pizza = pizza.nombre.split("_")[1]
       if tamano_pizza == tamano and pizza.precio <= dinero:
               lista_pizzas.append(pizza)
    return lista_pizzas

def cantidad_empleados_pais(
        generador_locales: Generator,
        pais: str
        ) -> int:
    empleados = 0
    for local in generador_locales:
        if local.pais == pais:
            empleados += local.cantidad_trabajadores    
    return empleados

# Consultas que ocupan 2 Generadores
def ganancias_producidas_en_los_pedidos(
        generador_contenido_pedidos: Generator,
        generador_pizzas: Generator
        ) -> Iterable:
    dict_precios = dict(map(lambda pizza: (pizza.nombre, pizza.precio), generador_pizzas))
    ganancias_totales = defaultdict(int)
    for pedido in generador_contenido_pedidos:
        ganancias_totales[pedido.id_pedido] += calcular_ganancia(pedido, dict_precios)
    return list(map(lambda id_pedido: (id_pedido, ganancias_totales[id_pedido]),
                    ganancias_totales.keys()))
       
def pizza_mas_vendida_del_dia(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        fecha: str
        ) -> set:
    pedidos_del_dia = filter(lambda pedido: pedido.fecha == fecha, generador_pedidos)
    id_pedidos_del_dia = set(map(lambda pedido: pedido.id_pedido, pedidos_del_dia))
    contenido_pedidos_del_dia = filter(lambda pedido: pedido.id_pedido in 
                                       id_pedidos_del_dia, generador_contenido_pedidos)
    lista_pizzas = []
    dict_pizzas = defaultdict(int)
    for pedido in contenido_pedidos_del_dia:
        dict_pizzas[pedido.nombre.split("_")[0]] += int(pedido.cantidad)
    if not dict_pizzas:
        return []
    cantidad_maxima = max(dict_pizzas.values())
    for pizza, cantidad in dict_pizzas.items():
        if cantidad == cantidad_maxima:
            lista_pizzas.append(pizza)
    return lista_pizzas

def pizza_del_mes(
        generador_pedidos: Generator,
        generador_contenido_pedidos: Generator,
        mes: str
        ) -> str:
    pedidos_del_mes = filter(lambda pedido: pedido.fecha.split("-")[1] == mes, generador_pedidos)
    id_pedidos_del_mes = set(map(lambda pedido: pedido.id_pedido, pedidos_del_mes))
    contenido_pedidos_del_mes = filter(lambda pedido: pedido.id_pedido in 
                                       id_pedidos_del_mes, generador_contenido_pedidos)
    lista_pizzas = []
    dict_pizzas = defaultdict(int)
    for pedido in contenido_pedidos_del_mes:
        dict_pizzas[pedido.nombre.split("_")[0]] += int(pedido.cantidad)
    if not dict_pizzas:
        return []
    cantidad_maxima = max(dict_pizzas.values())
    for pizza, cantidad in dict_pizzas.items():
        if cantidad == cantidad_maxima:
            lista_pizzas.append(pizza)
    return lista_pizzas
            
def popularidad_mezcla_de_ingredientes(
        generador_pizzas: Generator,
        generador_contenido_pedidos: Generator,
        ingredientes: set
        ) -> int:
    cantidad_vendida = 0
    pizzas_con_ingredientes = filter(lambda pizza: ingredientes.issubset(
        set(pizza.ingredientes.split(";"))),generador_pizzas)
    pizzas_con_ingredientes = list(map(lambda pizza: pizza.nombre, pizzas_con_ingredientes))
    pedidos_pizzas = filter(lambda pedido: pedido.nombre in pizzas_con_ingredientes, 
                            generador_contenido_pedidos)
    for pedido in pedidos_pizzas:
        cantidad_vendida += (1 * pedido.cantidad)
    return cantidad_vendida    

def total_ahorrado_pedidos(
        generador_contenido_pedidos: Generator,
        generador_pizzas: Generator
        ) -> str:  
    dict_precios = dict(map(lambda pizza: (pizza.nombre, pizza.precio), generador_pizzas))
    cantidad_ahorrada = 0
    for pedido in generador_contenido_pedidos:
        cantidad_ahorrada += calcular_ahorro(pedido, dict_precios)
    return round(cantidad_ahorrada)

def pizza_favorita_cliente(
        generador_pedidos: Generator,
        generador_contenido_pedidos: Generator,
        id_cliente: int,
        ) -> tuple:
    pizzas_del_cliente = filter(lambda pedido: pedido.id_cliente == id_cliente, generador_pedidos)
    id_pedidos_cliente = set(map(lambda pedido: pedido.id_pedido, pizzas_del_cliente))
    filtro_pedidos_cliente = filter(lambda pedido: pedido.id_pedido in id_pedidos_cliente, 
                                    generador_contenido_pedidos)
    dict_pizzas_vendidas = defaultdict(int)
    for pedido in filtro_pedidos_cliente:
        dict_pizzas_vendidas[pedido.nombre.split("_")[0]] += int(pedido.cantidad)    
    if not dict_pizzas_vendidas:
        return []
    maximo_ventas = max(dict_pizzas_vendidas.values())
    pizzas = [tupla for tupla in dict_pizzas_vendidas.items() if tupla[1] == maximo_ventas]
    return pizzas
    
# Consultas que ocupan 3 o mas Generadores
def local_mas_pizzas_vendidas_por_tipo_de_pizza(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_locales: Generator,
        tipo_de_pizza: str
        ) -> Iterable:
    
    dict_id_pedido_cantidad = defaultdict(int)
    dict_id_local_cantidad = defaultdict(int)
    lista = []
    contenido_pedidos_con_tipo_de_pizza = filter(lambda pedido: pedido.nombre.split("_")[0] ==  
                                            tipo_de_pizza, generador_contenido_pedidos)
    for pedido in contenido_pedidos_con_tipo_de_pizza:
        dict_id_pedido_cantidad[pedido.id_pedido] += pedido.cantidad 
        
    pedidos_con_tipo_pizza = filter(lambda pedido: pedido.id_pedido in 
                                  dict_id_pedido_cantidad.keys(), generador_pedidos)
    for pedido in pedidos_con_tipo_pizza:
        dict_id_local_cantidad[pedido.id_local] += dict_id_pedido_cantidad[pedido.id_pedido]
    if not dict_id_local_cantidad:
        return []    
    locales = filter(lambda local: local.id_local in dict_id_local_cantidad.keys(), 
                     generador_locales)
    cantidad_maxima = max(dict_id_local_cantidad.values())
    for local in locales:
        if dict_id_local_cantidad[local.id_local] == cantidad_maxima:
            lista.append(local)
    return lista
    
def ganancia_total_de_un_local(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_pizzas: Generator,
        id_local: int
        ) -> int:
    ganancias_local = 0
    dict_precios = dict(map(lambda pizza: (pizza.nombre, pizza.precio), 
                            generador_pizzas))
    pedidos_del_local = filter(lambda pedido: pedido.id_local == id_local, generador_pedidos)
    ids_pedidos_local = set(map(lambda pedido: pedido.id_pedido, pedidos_del_local))
    contenido_pedidos_local = filter(lambda pedido: pedido.id_pedido in ids_pedidos_local, 
                                     generador_contenido_pedidos)
    ganancias_local = sum(map(lambda pedido: calcular_ganancia(pedido, dict_precios),
                              contenido_pedidos_local))
    return ganancias_local

def promedio_ventas_con_descuento_de_un_pais(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_locales: Generator,
        pais: str
        ) -> float:
    descuento_total = 0
    locales_del_pais = filter(lambda local: local.pais == pais, generador_locales)
    ids_locales_del_pais = set(map(lambda local: local.id_local, locales_del_pais))
    pedidos_locales = filter(lambda pedido: pedido.id_local in ids_locales_del_pais, 
                                     generador_pedidos)
    ids_pedidos_locales = set(map(lambda pedido: pedido.id_pedido, pedidos_locales))
<<<<<<< Updated upstream
    contenido_pedido_locales = filter(lambda pedido: pedido.id_pedido in ids_pedidos_locales,
                                      generador_contenido_pedidos)
    dict_id_descuento_pedidos = dict(map(lambda pedido: (pedido.id_pedido, pedido.descuento),
                                         contenido_pedido_locales))
    if not dict_id_descuento_pedidos:
        return 0.0
    for descuento in dict_id_descuento_pedidos.values():
        descuento_total += descuento
    return round(descuento_total / len(dict_id_descuento_pedidos), 2)
=======
    contenido_pedidos_local = filter(lambda pedido: pedido.id_pedido in ids_pedidos_locales,
                                     generador_contenido_pedidos)

    return 
    
    

>>>>>>> Stashed changes

def gasto_cliente_por_mes(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_pizzas: Generator,
        id_cliente: int,
        year: int,
        ) -> list:
    gastos_por_mes = []
    pedidos_del_ano = list(filter(lambda pedido: pedido.id_cliente == id_cliente and \
        int(pedido.fecha.split("-")[0]) == year, generador_pedidos))
    ids_pedidos = set(map(lambda pedido: pedido.id_pedido, pedidos_del_ano))
    contenido_pedidos_ano = list(filter(lambda pedido: pedido.id_pedido in ids_pedidos, 
                                     generador_contenido_pedidos))
    nombres_pizzas = set(map(lambda pedido: pedido.nombre, contenido_pedidos_ano))
    pizzas_del_ano = filter(lambda pizza: pizza.nombre in nombres_pizzas, generador_pizzas)
    dict_precios = dict(map(lambda pizza: (pizza.nombre, pizza.precio), pizzas_del_ano))
    for mes in range (1, 13):
        pedidos_del_mes = list(filter(lambda pedido: int(pedido.fecha.split("-")[1]) == mes, 
                                 pedidos_del_ano))
        ids_mes = set(map(lambda pedido: pedido.id_pedido, pedidos_del_mes))
        contenido_pedidos_mes = list(filter(lambda pedido: pedido.id_pedido in ids_mes,
                                            contenido_pedidos_ano))  
        ganancias_del_mes = sum(map(lambda pedido: calcular_ganancia_total_pedido(pedido, dict_precios), 
                                    contenido_pedidos_mes))
        gastos_por_mes.append(round(ganancias_del_mes))
    return gastos_por_mes 

def pizzas_vendidas_mes_pais(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_locales: Generator,
        pais: str,
        mes: int,
        year: int,
        ) -> int:
    pedidos_del_local = filter(lambda local: local.pais == pais, generador_locales)
    id_locales = set(map(lambda local: local.id_local, pedidos_del_local))
    pedidos_en_tiempo = filter(lambda pedido: (pedido.id_local in id_locales) and \
        (int(pedido.fecha.split("-")[1]) == mes) and \
        (int(pedido.fecha.split("-")[0]) == year), generador_pedidos)
    id_pedidos_en_tiempo = set(map(lambda pedido: pedido.id_pedido, pedidos_en_tiempo))
    contenido_pedidos_en_tiempo = filter(lambda pedido: pedido.id_pedido in id_pedidos_en_tiempo, 
                                     generador_contenido_pedidos)
    cantidad_de_pizzas = sum(map(lambda pedido: pedido.cantidad, contenido_pedidos_en_tiempo))
    return cantidad_de_pizzas

# Consulta anidada
def consulta_anidada(instrucciones: dict) -> Any:  
    funciones = {
    "cargar_pizzas": cargar_pizzas,
    "cargar_locales": cargar_locales,
    "cargar_pedidos": cargar_pedidos,
    "cargar_contenido_pedidos": cargar_contenido_pedidos,
    "cliente_indeciso": cliente_indeciso,
    "pizzas_con_ingrediente": pizzas_con_ingrediente,
    "pizzas_pagables_de_un_tamano": pizzas_pagables_de_un_tamano,
    "cantidad_empleados_pais": cantidad_empleados_pais,
    "total_ahorrado_pedidos": total_ahorrado_pedidos
    }

    funcion_en_dict = instrucciones["funcion"]
    funcion = funciones[funcion_en_dict]
    args = {}
    
    for llave, valor in instrucciones.items():
        if llave != "funcion":
            if isinstance(valor, dict) and "funcion" in valor:
                args[llave] = consulta_anidada(valor)
            else:
                args[llave] = valor
    return funcion(**args)
    