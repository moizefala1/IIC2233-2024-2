import parametros
from random import uniform
#Funcion definida para guardar en una lista todas las coordenadas coolindantes
#a las coordenadas recibidas. Ademas recibe el numero de filas y columnas de la 
#matriz a recorrer.

def coordenadas_alrededor(i:int, x:int, num_filas:int, num_columnas:int) -> list:
    #Calcula las coordenadas que se encuentran en los 8 bloques alrededor de un punto [i, x] y las
    #retorna dentro de una lista
    direcciones = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1),         (0, 1),
                   (1, -1), (1, 0), (1, 1)]
    
    resultados = []
    
    for delta_fila, delta_columna in direcciones:
        nueva_fila = i + delta_fila
        nueva_columna = x + delta_columna
        if nueva_fila in range (0, num_filas) and nueva_columna in range (0, num_columnas):
            resultados.append([nueva_fila, nueva_columna])
    return resultados

def calcular_probabilidad (dificultad:str, evento: str) ->bool:
    #Calcula las probabilidades de que suceda el evento recibido, tomando en cuenta las
    #probabilidades recibidas en el archivo "eventos.txt, y retorna un bool indicando 
    # si el evento sucede o no"
    
    if evento == "zombie":
        probabilidad = uniform(0,1)
        if dificultad == "facil":
            zombie = probabilidad <= float(parametros.eventos[0][1])
        elif dificultad == "normal":
            zombie = probabilidad <= float(parametros.eventos[0][2])
        elif dificultad == "dificil":
            zombie = probabilidad <= float(parametros.eventos[0][3])
        return zombie
    
    elif evento == "helada":
        probabilidad = uniform(0,1)
        if dificultad == "facil":
            helada = probabilidad <= float(parametros.eventos[1][1])
        elif dificultad == "normal":
            helada = probabilidad <= float(parametros.eventos[1][2])
        elif dificultad == "dificil":
            helada = probabilidad <= float(parametros.eventos[1][3])
        return helada