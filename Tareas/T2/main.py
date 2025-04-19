from sys import argv, exit
from random import randint, uniform
import parametros
from entidades import (Jardin, Planta, Potencilantro, Defensauce, 
                    Solaretillo, Aresauce, Cilantrillo, Fensaulantro)
from funciones import coordenadas_alrededor, calcular_probabilidad

seguir = False
nombre_jardin = argv[1]
dificultad = argv[2]

if nombre_jardin in parametros.nombres_jardines:
    seguir = True
    if dificultad in ["facil", "normal", "dificil"]:
        seguir = True
    else: 
        print("Porfavor introduzca una dificultad válida (facil, normal o dificil)")
        seguir = False
else:
    print("Porfavor introduzca un nombre válido para el jardín a cargar")
    seguir = False
    
tablero = parametros.jardines[nombre_jardin]
jardin = Jardin(tablero)
#Usa el instanciador para instanciar las plantas que ya se encontraban en el jardin 
#(en el caso de haber)

for i in range (len(jardin.tablero)):
    for x in range (len(jardin.tablero[i])):
        if jardin.tablero[i][x] != "X":
            jardin.instanciador(jardin.tablero[i][x], [i, x])
jardin.instanciador("D", [])
jardin.instanciador("P", [])
while seguir:
    menu_inicial = (input
         ("---------------------------\n"
                "Menú de inicio\n"
           "---------------------------\n"
        f"Soles disponibles: {jardin.soles}\n"
            f"Temperatura: {jardin.temperatura}°C\n"
            f"Día actual: {parametros.DIA} \n"
            "                      \n"
            "[1] Menu Jardín\n"
            "[2] Laboratorio\n"
            "[3] Pasar Día\n"
            "                          \n"
            "[0] Salir del programa\n"
        ))
    if menu_inicial == "1": ###MENU JARDIN
        seguir_jardin = True
        while seguir_jardin:
            tablero_en_cadena = "\n".join([str(fila) for fila in jardin.tablero])
            menu_jardin = input(
                "---------------------------\n"
                "          Jardín           \n"
                "---------------------------\n"
                "                            \n"
            f"{tablero_en_cadena} \n"
                "                           \n"
                "[1] Intercambiar\n"
                "[2] Cultivar\n"
                "[3] Regar\n"           
                "[0] Volver al Menú de inicio\n"
                "                           \n"
                "Indique su opción:"
                )
            if menu_jardin == "1":
                valido = False
                coords = input("Introduzca las coordenadas a remeplazar, de la forma (1,1;2,2)")
                validos = "1234567890,;"
                for i in range (len(coords)):
                    if coords[i] not in validos:
                        print("\nPorfavor introduzca una opción valida\n") 
                        break
                    valido = True
                if valido:
                    intercambio = jardin.intercambiar(coords)
                    valido = False
                    if intercambio:
                        print("\nIntercambio realizado con éxito.\n"
                              )
                    else:
                        print("\nPorfavor introduzca una opción valida (planta-planta,"
                              " vacio-planta, vacio-vacio\n") 
            elif menu_jardin == "2":  ### CULTIVAR              
                plantas_dispo = jardin.contador_plantas()
                menu_plantas_dispo = input(
                    "                                      \n"
                    "Plantas Disponibles:                  \n"
                    "                                      \n"
                    f"[1] Solaretillo: {plantas_dispo[0]}  \n"
                    f"[2] Defensauce: {plantas_dispo[2]}   \n"
                    f"[3] Potencilantro: {plantas_dispo[2]}\n"
                    f"[4] Aresauce: {plantas_dispo[3]}     \n"
                    f"[5] Cilantrillo: {plantas_dispo[4]}  \n"
                    f"[6] Fensaulantro: {plantas_dispo[5]} \n"
                    "[0] Volver al Menú Jardín             \n"
                    "                                      \n"
                    "Escoge el número de la planta a cultivar: (ej. 5)\n")
                if  menu_plantas_dispo in "123456" :
                    coords= input("Escoge la posición donde quieres cultivar: (ej. 2,3)")
                    indices = [0, 1, 2, 3, 4, 5]
                    indice_planta = int(menu_plantas_dispo) - 1 
                    if plantas_dispo[indice_planta] >= 1:
                        print(jardin.cultivar(parametros.plantas[indice_planta][0], coords))
                    else:
                        print("Planta no disponible")
                elif menu_plantas_dispo == "0": ## VOLVER AL MENU
                    pass
                else:
                    print("Opción no válida")
                    
            elif menu_jardin == "3": ###REGAR PLANTAS
                texto = jardin.regar()
                if texto != "":
                    print("============================\n"
                    "                            \n"
                    "  Se han regado tus plantas \n"
                    "                            \n"
                    "============================\n")
                    print(texto)
                else:
                    print("============================\n"
                          "                            \n"
                          "  No hay plantas que regar  \n"
                          "                            \n"
                          "============================\n"
                         )
 
            elif menu_jardin == "0": ### VOLVER AL MENU JARDIN
                seguir_jardin = False
            else:
                print("\nPorfavor introduzca una opción valida\n")
                
    elif menu_inicial == "2": ##LABORATORIO
        seguir_lab = True
        mutacion = False
        plantas_dispo = jardin.contador_plantas()
        while seguir_lab:
            opcion = int(input(
                "=================================================\n"
                "                  LABORATORIO                    \n"
                "=================================================\n"
                "                                                 \n"
                "                      |Guía|                     \n"
                "                                                 \n"
                "Solaretillo + Defensauce = Aresauce              \n"
                "Solaretillo + Potencilantro = Cilantrillo        \n"
                "Defensauce + Potencilantro = Fensaulantro        \n"
                "                                                 \n"
                "                    |Tienes|                     \n"
                "Solaretillo        Defensauce       Potencilantro\n"
                f"{plantas_dispo[0]}                       "                 
                f"{plantas_dispo[1]}                 "    
                f"{plantas_dispo[2]}\n"
                "                   |Mutaciones|                  \n"
                " Arensauce          Cilantrillo      Fensaulantro\n"
                "     [1]                 [2]               [3]   \n"
                "                                                 \n"
                "[0] Volver al menú principal\n"
                "Indique su mutación a crear:\n"
            ))
            if opcion == 1: #Solaretillo + Defensauce = Aresauce 
                mutacion = jardin.mutar(1)
            elif opcion == 2:
                mutacion = jardin.mutar(2)
            elif opcion == 3: #Solaretillo + Potencilantro = Cilantrillo
                mutacion = jardin.mutar(3)
            elif opcion == 0: #Defensauce + Potencilantro = Fensaulantro
                seguir_lab = False
            else: 
                print("\nPorfavor introduzca una opcion válida\n")
                
            if mutacion:
                print("\nMutacion completada con éxito\n")
                seguir_lab = False
            else:
                print("\nMutacion fallida, revise inventario de plantas\n")   
    elif menu_inicial == "3": #SIMULACION DEL DIA
        parametros.DIA += 1 
        temperatura = randint(parametros.TEMP_MIN_JARDIN, parametros.TEMP_MAX_JARDIN)
        jardin.temperatura = temperatura
        for i in range (len(jardin.plantas_en_jardin)):
            planta = jardin.plantas_en_jardin[i]
            if planta.resistencia_termica > jardin.temperatura:
                planta.congelado = True
                for i in range (len(jardin.tablero)):
                    for x in range (len(jardin.tablero[i])):
                        if [i, x] == planta.coords:                                
                            jardin.tablero[i][x] = f"*{planta.tipo}*"
            else:
                for i in range (len(jardin.tablero)):
                    for x in range (len(jardin.tablero[i])):
                        if [i, x] == planta.coords:
                            jardin.tablero[i][x] = planta.tipo
                            planta.congelado = False                                        
        #EVENTOS
        helada = False
        zombie = False
        zombie = calcular_probabilidad(dificultad, "zombie")
        if not zombie:        
            helada = calcular_probabilidad(dificultad, "helada")
        ### NO HAY EVENTO    
        if (helada == False and zombie == False):
            print("==========================\n"
                  "      Día tranquilo       \n"
                  "==========================\n")
        ## EVENTO ZOMBIE
        elif zombie:
            print ("=================================\n"
                   "Se avecina una oleada de zombies!\n"
                   "=================================\n"
                   "Las plantas podrían sufrir daños \n"
                   "=================================\n"   
            )
            sin_daño = True
            daño_reducido = False
            texto = ""
            casillas_atacadas = 0
            dificultad_repeticiones = {
                "facil" : parametros.ZOMBIE_FACIL,
                "normal" : parametros.ZOMBIE_NORMAL,
                "dificil" : parametros.ZOMBIE_DIFICIL
            }
            for z in range (len(jardin.plantas_en_jardin)):
                if jardin.plantas_en_jardin[z].__class__.__name__ == "Fensaulantro":
                    daño_reducido = True
            for i in range (dificultad_repeticiones[dificultad]):
                fila_atacada = randint(0, ((len(jardin.tablero))-1))
                columna_atacada = randint (0, ((len(jardin.tablero[0]))-1))
                if jardin.tablero[fila_atacada][columna_atacada] != "X":
                    casillas_atacadas += 1
                    for i in range (len(jardin.plantas_en_jardin)):
                        if (jardin.plantas_en_jardin[i].coords == [fila_atacada, columna_atacada]):
                            planta = jardin.plantas_en_jardin[i]   
                            daño = (max(1,round(parametros.ATAQUE * 
                                    ((40-planta.resistencia)/40))))
                            if daño_reducido:
                                daño = round(daño * parametros.RED_ATQ)
                            if planta.__class__.__name__ == "Defensauce":
                                if daño >= planta.armadura:
                                    sin_daño = False
                                    planta.armadura = 0
                                    planta.vida = planta.vida_maxima
                                    texto += (f"La planta {planta.__class__.__name__} en" 
                                            f" ({fila_atacada},{columna_atacada}) ha perdido" 
                                            f" {daño} puntos de armadura, rompiéndola,\n")
                                elif daño < planta.armadura:
                                    sin_daño = False
                                    planta.armadura -= daño
                                    planta.vida = planta.vida_maxima
                                    texto += (f"La planta {planta.__class__.__name__} en" 
                                            f" ({fila_atacada},{columna_atacada}) ha perdido" 
                                                f" {daño} puntos de armadura\n")
                            else:
                                if planta.vida - daño <= 0:
                                    jardin.tablero[fila_atacada][columna_atacada] = "X"
                                    jardin.plantas_en_jardin.pop(i)
                                    sin_daño = False
                                    texto += (f"La planta {planta.__class__.__name__} en" 
                                                f" ({fila_atacada},{columna_atacada}) ha perdido" 
                                                f" {daño} puntos de vida, lo que acabó con su vida\n")
                                    break
                                else:
                                    planta.vida -= daño
                                    sin_daño = False
                                    texto += (f"La planta {planta.__class__.__name__} en" 
                                                f" ({fila_atacada},{columna_atacada}) ha perdido" 
                                                f" {daño} puntos de vida\n")
                                    break
                else:
                    texto += (f"¡Un zombie intentó atacar la posición ({fila_atacada},"
                                f"{columna_atacada}) pero estaba vacía!\n")
            soles_robados = casillas_atacadas * parametros.SOLES_ROBADOS
            if sin_daño:
                print("\n¡Ninguna de tus plantas fue atacada! No has sufrido robos de soles\n")
            else:
                print("====================================================================\n"
                    f"Durante la noche pasó una oleada de {dificultad_repeticiones[dificultad]}" 
                    " zombies!\n"
                    "======================================================================\n"
                    f"{texto}" 
                    f"Los zombies lograron atacar {casillas_atacadas} casiilas, " 
                    f"robando {soles_robados} soles!\n"
                    )
        #HELADA
        elif helada:
            print (
                "============================================================\n"
                "               Se ha activado el evento: Helada             \n"
                "============================================================\n"
                "Las plantas con baja temperatura verán reduca su produccion \n"
                "============================================================\n"
            )
            jardin.temperatura = randint(parametros.TEMP_MIN_HELADA, parametros.TEMP_MAX_HELADA)
            for i in range (len(jardin.plantas_en_jardin)):
                planta = jardin.plantas_en_jardin[i]
                if planta.resistencia_termica > jardin.temperatura:
                    planta.congelado = True
                    for i in range (len(jardin.tablero)):
                        for x in range (len(jardin.tablero[i])):
                            if [i, x] == planta.coords:                                
                                jardin.tablero[i][x] = f"*{planta.tipo}*"
                else:
                    for i in range (len(jardin.tablero)):
                        for x in range (len(jardin.tablero[i])):
                            if [i, x] == planta.coords:
                                jardin.tablero[i][x] = planta.tipo
                                planta.congelado = False               
        #CALCULAR SOLES
        potenciado = False
        texto = ""
        soles_totales = 0
        soles_cielo = randint(parametros.MIN_SOLES, parametros.MAX_SOLES)
        soles_totales += soles_cielo
        for i in range (len(jardin.tablero)):
            for x in range (len(jardin.tablero[i])):
                if jardin.tablero[i][x] in parametros.productoras:
                    for z in range (len(jardin.plantas_en_jardin)):
                        if jardin.plantas_en_jardin[z].coords  == [i, x] and (
                            jardin.plantas_en_jardin[z].congelado == False):
                            soles_generados = 0
                            planta = jardin.plantas_en_jardin[z]
                            coords_colindantes = coordenadas_alrededor(
                                i, x, len(jardin.tablero), len(jardin.tablero[i]))
                            for coord in coords_colindantes:
                                if jardin.tablero[coord[0]][coord[1]] in parametros.potenciadoras:
                                    potenciado = True
                            if potenciado:
                                if helada:
                                    soles_generados += parametros.SOLES_EXTRA_HELADA
                                if planta.__class__.__name__ == Cilantrillo:                               
                                    soles_generados = round(planta.generar_soles(jardin.temperatura) + ( 
                                    parametros.SOLES_EXTRA_HELADA))
                                    soles_totales += soles_generados
                                    texto += (f"Un {planta.__class__.__name__} potenciado en "
                                    f"({i},{x}) ha producido {soles_generados} soles.\n")
                                else:
                                    soles_generados = round(planta.generar_soles(jardin.temperatura) * (
                                        1 + (parametros.AUMENTO_NUTRIENTE/100)))
                                    soles_totales += soles_generados
                                    texto += (f"Un {planta.__class__.__name__} potenciado en "
                                    f"({i},{x}) ha producido {soles_generados} soles\n")
                                
                            else:
                                soles_generados = planta.generar_soles(jardin.temperatura)
                                soles_totales += soles_generados
                                texto += (f"Un {planta.__class__.__name__} normal en({i},{x})"
                                f"ha producido {soles_generados} soles\n")      
        jardin.soles += soles_totales    
        productoras = False
        for i in range (len(jardin.tablero)):
            for x in range (len(jardin.tablero[i])):
                if jardin.tablero[i][x] in parametros.productoras:
                    productoras = True        
        if texto == "" and productoras:
            texto = "Dadas las bajas temperaturas no se han generado soles!\n"
        elif texto == "" and not productoras:
            texto = "No hay plantas que produzcan soles\n"
        print ("================================================================\n"
               "                                                                \n"
              "        Se ha iniciado la produccion de soles                    \n" 
              "                                                                 \n"
              "=================================================================\n"
              f"{texto}"
              "=================================================================\n"
              "                                                                 \n"
              f"Se han obtenido {soles_cielo} soles del cielo                   \n"
              "                                                                 \n"       
              f"En total se han recolectado {soles_totales} soles durante el día\n"
               )  
        ## LLEGADA DE PLANTAS
        diccionario_plantas = {
            1 : parametros.plantas[0][0],
            2 : parametros.plantas[1][0],
            3 : parametros.plantas[2][0]
        }          
        cantidad_plantas = randint(parametros.NUM_MIN_PLANTA, parametros.NUM_MAX_PLANTA)          
        for i in range (cantidad_plantas):
            azar = randint(1,3)
            tipo_planta = diccionario_plantas[azar]
            jardin.instanciador(tipo_planta, [])
        print(f"\n*** Han llegado {cantidad_plantas} plantas a tu inventario ***\n")
        ##### PRESENTACIÓN        
        print(jardin)
        #Fin del juego
        if parametros.DIA > parametros.DURACION:
            print("Se ha acabado el juego!\n"
                  f"Has terminado con una puntuacion de: {jardin.soles}" 
            )
            exit()  
    elif menu_inicial == "0":
        seguir = False
        print("Saliste de DCCampesino, supongo que vas a seguir tu camino..."
                "Gracias por ayudar a Hernán a combatir los zombies!!")
        exit()
    else:
        print("\nPorfavor introduzca una opción valida\n")
        