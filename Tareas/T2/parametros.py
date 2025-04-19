from random import uniform

#Se definen los parametros escenciales para el funcionamiento del programa, tanto constantes 
#como variables, como la lectura de los archivos.

### PARAMETROS
#Parmatros constantes necesarios para el correcto funcionamiento del programa
 
DIA = 0
SOLES_INICIO = 0
TEMP_INICIAL = 18
MIN_SOLES = 0
MAX_SOLES = 20
DURACION = 15
POTENCIAL_SOLARETILLO_MIN = 1
POTENCIAL_SOLARETILLO_MAX = 5
CONSTANTE_SOLES = 10
ARMADURA = 20
AUMENTO_NUTRIENTE = 20
TEMP_MIN_JARDIN = -5
TEMP_MAX_JARDIN = 25
ANTI_ROBO = uniform(0,1)
AUM_POT_CIL = uniform(0,1)
AUM_AUM_CIL = uniform(0,1)
RED_ATQ = uniform(0,1)
RIEGO_1 = 10
RIEGO_2 = 5
ZOMBIE_FACIL = 3
ZOMBIE_NORMAL = 5
ZOMBIE_DIFICIL = 7
ATAQUE = 20
TEMP_MIN_HELADA = -5
TEMP_MAX_HELADA = 2
SOLES_EXTRA_HELADA = 20
SOLES_ROBADOS = 50
NUM_MIN_PLANTA = 2
NUM_MAX_PLANTA = 5


### JARDINES
#Lee la informacion dentro del archivo y la guarda en un diccionario, relacionando el
#nombre del jardin con el tablero que debe cargar

jardines_archivo = open(file="data/jardines.txt").readlines()
jardines = {

}
nombres_jardines = []
for jardin in jardines_archivo:
    jardin = jardin.strip().split("!")
    jardin[1] = jardin[1].split(";")
    tablero = [fila.split(",") for fila in jardin[1]]
    jardines[jardin[0]] = tablero
    nombres_jardines.append(jardin[0])
    
    
### PLANTAS   
#Lee el archivo indicado y guarda toda su informacion en la lista plantas

plantas_archivo = open(file="data/plantas.txt").readlines()
plantas = []
for planta in plantas_archivo:
    valida = True
    planta = planta.strip().split(";")
    for i in range (len(planta)):
        if i != 0:
            planta[i] = int(planta[i])     
    vida_max = planta[1]
    if len(planta[0])!= 1:
        valida = False
    if planta[1] not in range (0,101): #vida maxima
        valida = False
    if planta[2] not in range (0,vida_max + 1):#vida
        valida = False
    if planta[3] not in range (0,41):#resistencia
        valida = False
    if planta[4] not in range (-5,26):#resistencia termica 
        valida = False
    if planta[5] not in range (0,2):#congelacion
        valida = False
    if planta[6] not in range (0,31):#altura
        valida = False
    if valida:
        plantas.append(planta)
        
productoras = [plantas[0][0], plantas[3][0], plantas[4][0]] #Solaretillo, Aresauce, Cilantrillo
potenciadoras = [plantas[2][0], plantas[4][0], plantas [5][0]]#Potencilantro, Cilantrillo, #Fensaulantro

### EVENTOS
#Lee la informacion dentro del archivo eventos.txt y lo guarda en la lista homonima
eventos_archivo = open(file = "data/eventos.txt").readlines()  
eventos = []  
for evento in eventos_archivo: 
    evento = evento.strip().split(";")
    eventos.append(evento)


