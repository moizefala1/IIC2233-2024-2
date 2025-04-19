import dccultivo
import utils
seguir = True
while seguir:
    menu_inicio=int(input("¡Bienvenido a DCCultivo!\n"
                          "                        \n"
                      "*** Menú de Inicio ***\n"
                      "                            \n"
                      "[1] Crear predios\n"
                      "[2] Salir del programa\n"
                      "                            \n"
                      "Indique su opción (1, 2):   \n"))
    
    if menu_inicio == 1:
        cultivo = dccultivo.DCCultivo()
        cultivo.crear_predios("predios.txt")
        menu_acciones = True
        seguir = False
    elif menu_inicio == 2:
        seguir = False
        menu_acciones =False
        print("Saliendo del programa...")
        exit()
    else:
        print("\nPorfavor, ingrese un valor valido\n")
        menu_acciones = False

while menu_acciones:
    opcion_menu_acciones = int(input("¡Bienvenido a DCCultivo!\n"
                            "Tu terreno está listo para trabajar.\n"
                             "                             \n"
                            "*** Menú de Acciones ***\n"
                            "                             \n"
                            
                            "[1] Visualizar predio\n"
                            "[2] Plantar\n"
                            "[3] Regar\n"
                            "[4] Buscar y eliminar plagas\n"
                            "[5] Salir del programa\n"
                            "                             \n"
                            "Indique su opción (1, 2, 3, 4, 5)))\n:"))
                            
    if opcion_menu_acciones == 1:
        encontrado = False
        predio = input("Introduzca el codigo de predio a visualizar:\n")
        for predios in cultivo.predios:
            if predios.codigo_predio == predio:
                utils.imprimir_planos(predios)
                encontrado = True
        if encontrado == False:
            print("\nCodigo de predio no encontrado\n")
            
    elif opcion_menu_acciones == 2:
        codigo_cultivo = input("Ingrese el codigo de cultivo a plantar:")
        alto = int(input("Introduzca el alto del cultivo:"))
        ancho = int(input("Introduzca el ancho del cultivo:"))
        plantar = cultivo.buscar_y_plantar(codigo_cultivo, alto, ancho)
        if plantar:
            print("Cultivo realizado")
        else:
            print("No se encontró un predio disponible")
        
    elif opcion_menu_acciones == 3:
        codigo_predio = input("Introduzca el codigo del predio a regar:")
        centro_fila = int(input("Introduzca la fila del centro de riego"))
        centro_columna = int(input("Introduzca la columna del centro de riego"))
        area = int(input("Introduzca el area del riego:"))
        
        cultivo.buscar_y_regar(codigo_predio, [centro_fila, centro_columna], area)
        
    elif opcion_menu_acciones == 4:
        plagas = utils.plagas(cultivo)
        lista = cultivo.detectar_plagas(plagas)
        print("\n",lista)
        if lista != []:
            print("\nSe han eliminado las plagas exitosamente!\n")
        else:
            print("\nNo hay plagas que eliminar\n")
    elif opcion_menu_acciones == 5:
        print("\nSaliendo del programa...\n")
        exit()
    else:
        print("Porfavor ingrese un valor valido")