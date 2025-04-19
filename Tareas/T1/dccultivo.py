class Predio:
    def __init__(self, codigo_predio: str, alto: int, ancho: int) -> None:
        self.codigo_predio = codigo_predio
        self.alto = alto
        self.ancho = ancho
        self.plano = []
        self.plano_riego = []

    def crear_plano(self, tipo: str) -> None:
        #Crea la matriz en base al argumento recibido
        
        if tipo == "normal":
            for columna in range (self.alto):
                filas = []
                for fila in range (self.ancho):
                    filas.append("X")
                self.plano.append(filas)
                
        if tipo == "riego":
            for filas in range (self.alto):
                filas = []
                for columna in range (self.ancho):
                    filas.append(0)
                self.plano_riego.append(filas)
                
    def plantar (
        self, codigo_cultivo: int, coordenadas: list, alto: int, ancho: int 
        ) -> None:
        
        #Lee la matriz, y cada vez que pase por una celda que esté dentro del area de cultivo, 
        # reemplaza "X" con "codigo_cultivo"
        fila_i = coordenadas[0]
        columna_j = coordenadas[1]
        for fila in range (len(self.plano)):
            for columna in range (len(self.plano[fila])):
                if (fila in range (fila_i, alto + fila_i) and 
                    columna in range (columna_j, ancho + columna_j)): 
                    self.plano[fila][columna] = (codigo_cultivo)
            
    def regar(self, coordenadas: list, area: int) -> None:
        #Genera un cuadrado de lado "area*2", para luego eliminar sus esquinas.
        
        fila_i = coordenadas[0]
        columna_j = coordenadas[1]
        radio = area
        
        for fila in range (len(self.plano_riego)):
            for columna in range (len(self.plano_riego[fila])): 
                if (fila in range (fila_i - radio, fila_i + radio + 1)  
                    and columna in range (columna_j - radio, columna_j + radio + 1)):
                    self.plano_riego[fila][columna] += 1  
                    
                if ((fila == fila_i - radio) and (columna == columna_j - radio)):
                    self.plano_riego[fila][columna] -=1
                if ((fila == fila_i + radio) and (columna == columna_j + radio)):
                    self.plano_riego[fila][columna] -=1
                if ((fila == fila_i - radio) and (columna == columna_j + radio)):
                    self.plano_riego[fila][columna] -=1
                if ((fila == fila_i + radio) and (columna == columna_j - radio)):
                    self.plano_riego[fila][columna] -=1
        
    def eliminar_cultivo(self, codigo_cultivo: int) -> int:
        #Recorre la matriz buscando las celdas con "codigo_cultivo" y 
        #reemplazandolas con la str "X"
        
        celdas_borradas = 0
        for filas in range (len(self.plano)):
            for columnas in range (len(self.plano[filas])):
                if self.plano[filas][columnas] == codigo_cultivo:
                    self.plano[filas][columnas] = "X"
                    celdas_borradas+=1
        return celdas_borradas


class DCCultivo:
    def __init__(self) -> None:
        self.predios = []

    def crear_predios(self, nombre_archivo: str) -> str:
        #Crea la expeccion para el error FileNotFound, en caso de no leer 
        #el archivo, caso contrario, carga el archivo con los predios, crea sus 
        #planos, y los inserta en la lista de predios del cultivo.
        
        try:
            archivo_predios = open(f"data/{nombre_archivo}", "r").readlines()
        except FileNotFoundError:
            return "Fallo en la carga de DCCultivo"
        
        for predio in archivo_predios:
            predio = predio.strip().split(",")
            predio = Predio(str(predio[0]), int(predio[1]), int(predio[2]))
            predio.crear_plano("normal")
            predio.crear_plano("riego")
            self.predios.append(predio)
            
        return "Predios de DCCultivo cargados exitosamente"
        


    def buscar_y_plantar(self, codigo_cultivo: int, alto: int, ancho: int) -> bool:
        
        #Lee la matriz, revisa que no exista un codigo de cultivo igual ya plantado,
        # para luego generar un bucle for que busque si existe espacio
        #dentro del predio, usando el alto y ancho del cultivo a plantar.
        
        for predio in self.predios:
            for fila in range(len(predio.plano)):
                for columna in range (len(predio.plano[fila])):
                    if predio.plano[fila][columna] == codigo_cultivo:
                        plantar = False
                        break
                    else:
                        plantar = True
                if plantar == False:
                    break
                        
            if plantar:
                for fila in range (len(predio.plano) - alto + 1):
                    for columna in range(len(predio.plano[fila]) - ancho + 1):
                        espacio_libre = True
                        for fila_cultivo in range(alto):
                            for columna_cultivo in range(ancho):
                                if (predio.plano[fila + fila_cultivo]
                                    [columna + columna_cultivo] != "X"):
                                    espacio_libre = False
                                    break
                            if espacio_libre == False:
                                break
                        if espacio_libre:
                            predio.plantar(codigo_cultivo, [fila, columna], alto, ancho)
                            return True
        return False

    def buscar_y_regar(self, codigo_predio: str, coordenadas: list, area: int) -> None:
        # Recorre la matriz buscando el codigo a regar, y luego usa el metodo para lo mismo
        for predio in self.predios:
            if predio.codigo_predio == codigo_predio:
                predio.regar(coordenadas, area)

    def detectar_plagas(self, lista_plagas: list[list]) -> list[list]:
        
        #Recorre cada predio buscando el predio solicitado, para luego identificar la plaga,
        #borrando todos los cultivos con el mismo codigo dentro del predio.
        #Genera una lista ordenada usando como funcion clave los valores de las celdas eliminadas
        #y en caso de empate, el numero del predio, de manera ascendente.
        
        dict_de_predios = {}
        for predio in self.predios:
            celdas_eliminadas = 0
            for predio_infectado in lista_plagas:
                if predio.codigo_predio == predio_infectado[0]:
                    fila_i = predio_infectado[1][0]
                    columna_j = predio_infectado[1][1]
                    codigo = predio.plano[fila_i][columna_j] 
                    if codigo != "X":
                        for fila in range (len(predio.plano)):
                            for columna in range (len(predio.plano[fila])):
                                if predio.plano[fila][columna] == codigo:
                                    predio.plano[fila][columna] = "X"
                                    celdas_eliminadas +=1
            if celdas_eliminadas > 0:
                dict_de_predios[predio.codigo_predio] = celdas_eliminadas
        
        
        lista_ordenada = sorted([[k, v] for k, v in dict_de_predios.items()], 
                                key=lambda x: [x[1], x[0]])
        
        return lista_ordenada

                    



