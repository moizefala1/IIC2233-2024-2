import parametros
from random import uniform, randint
from abc import ABC, abstractmethod

class Planta(ABC):
    #Define el creador de *cualquier* planta, por eso se usa una clase abstracta
    def __init__(self, tipo: str, vida_maxima: str, vida: str, resistencia: str, 
                 resistencia_termica: str, congelacion:str, altura: str, coords = [] ) ->None:
        self.tipo = tipo
        self.vida_maxima = int(vida_maxima)
        self.vida = int(vida)
        self. resistencia = int(resistencia)
        self.resistencia_termica = int(resistencia_termica)
        self.altura = int(altura)
        self.coords = coords

        if congelacion == "0":
            self.congelado = False
        else:
            self.congelado = True
            
    #Metodo abstracto, ya que todas las plantas pueden regarse
    @abstractmethod
    def regarse (self, sanacion: int) -> None:
        self.vida += sanacion
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
    
        
class Solaretillo(Planta):  ### S
    #Recibe los parametros para Solaretillo recibido en los archivos y los inicializa 
    # en la clase abstracta
    def __init__(self, tipo = parametros.plantas[0][0], 
                 vida_maxima = parametros.plantas[0][1], 
                 vida = parametros.plantas[0][2], 
                 resistencia = parametros.plantas[0][3], 
                 resistencia_termica = parametros.plantas[0][4], 
                 congelacion = parametros.plantas[0][5],
                 altura = parametros.plantas[0][6],
                 coords = []) -> None:
        
        super().__init__(tipo, vida_maxima, vida, resistencia, resistencia_termica, 
                         congelacion, altura, coords)   
        #Genera una variable "potencial" cada vez que se inicializa, siendo esta
        #un punto flotante entre "POTENCIAL_SOLARETILLO_MIN" y "POTENCIAL_SOLARETILLO_MAX"
        self.potencial = uniform(
            parametros.POTENCIAL_SOLARETILLO_MIN, parametros.POTENCIAL_SOLARETILLO_MAX
            )
        
    def __str__(self) -> str:
        return str(self.tipo)

    def regarse (self, sanacion: int) -> None:
        self.vida += sanacion
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
            
    #Define la generación de soles respetando la formula entregada
    def generar_soles(self, temperatura: int) -> int:
        return round(parametros.CONSTANTE_SOLES * self.potencial * 
                     (temperatura / 25) * (self.altura / 30))

class Defensauce(Planta): ###D
    def __init__(self, 
                 tipo = parametros.plantas[1][0], 
                 vida_maxima = parametros.plantas[1][1], 
                 vida = parametros.plantas[1][2], 
                 resistencia = parametros.plantas[1][3], 
                 resistencia_termica = parametros.plantas[1][4],
                 congelacion = parametros.plantas[1][5],
                 altura = parametros.plantas[1][6],
                 coords = []) -> None:
        self.armadura = parametros.ARMADURA
        #Inicializa el parametro armadura en base al valor entregado en parametros.py,
        #ademas de inicializar en la clase abstracta los valores leidos en los archivos.
        super().__init__(tipo, vida_maxima, vida, resistencia, resistencia_termica,congelacion, altura, coords)
        
    def __str__(self) -> str:
        return str(self.tipo)
        
    def regarse (self, sanacion: int) -> None:
        self.vida += sanacion
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
        
class Potencilantro(Planta): ####P
    def __init__(self, tipo = parametros.plantas[2][0],
                 vida_maxima = parametros.plantas[2][1], 
                 vida = parametros.plantas[2][2],
                 resistencia = parametros.plantas[2][3],
                 resistencia_termica = parametros.plantas[2][4], 
                 congelacion = parametros.plantas[2][5],
                 altura = parametros.plantas[2][6],
                coords = []) -> None:
        #Inicializa la clase leyendo los valores entregados en el archivo
        self.aumento = (1 + (parametros.AUMENTO_NUTRIENTE/100))
        super().__init__(tipo, vida_maxima, vida, resistencia, 
                         resistencia_termica, congelacion, altura, coords)
        
    def __str__(self) -> str:
        return str(self.tipo)
           
    def regarse (self, sanacion: int) -> None:
        self.vida += sanacion
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
    
class Aresauce(Solaretillo, Defensauce):
    def __init__(self, tipo = parametros.plantas[3][0], 
                 vida_maxima = parametros.plantas[3][1], 
                 vida = parametros.plantas[3][2], 
                 resistencia = parametros.plantas[3][3], 
                 resistencia_termica = parametros.plantas[3][4], 
                 congelacion = parametros.plantas[3][5], 
                 altura = parametros.plantas[3][6],
                 coords = []) -> None:
        self.armadura = parametros.ARMADURA
        self.anti_robo = parametros.ANTI_ROBO    
        super().__init__(tipo, vida_maxima, vida, resistencia, resistencia_termica, 
                         congelacion, altura, coords)
    
    def generar_soles(self, temperatura: int) -> int:
        return round(parametros.CONSTANTE_SOLES * self.potencial * 
                     (temperatura / 25) * (self.altura / 30))
    
class Cilantrillo(Solaretillo, Potencilantro):
    def __init__(self, tipo = parametros.plantas[4][0], 
                 vida_maxima = parametros.plantas[4][1], 
                 vida = parametros.plantas[4][2], 
                 resistencia = parametros.plantas[4][3], 
                 resistencia_termica = parametros.plantas[4][4], 
                 congelacion = parametros.plantas[4][5], 
                 altura = parametros.plantas[4][6],
                 coords = []) -> None:
        super().__init__(tipo, vida_maxima, vida, resistencia, resistencia_termica, 
                         congelacion, altura, coords)
        
    def generar_soles(self, temperatura: int) -> int:
        self.potencial = self.potencial * (1 + (parametros.AUM_POT_CIL/100))
        self.aumento = self.aumento * (1 + (parametros.AUM_AUM_CIL)/100)
        
        soles = (parametros.CONSTANTE_SOLES * (self.potencial) * 
                 (temperatura / 25) * (self.altura / 30)) * self.aumento 
        return soles
    
class Fensaulantro(Defensauce, Potencilantro):
    def __init__(self, tipo = parametros.plantas[5][0], 
                 vida_maxima = parametros.plantas[5][1], 
                 vida = parametros.plantas[5][2], 
                 resistencia = parametros.plantas[5][3], 
                 resistencia_termica = parametros.plantas[5][4], 
                 congelacion = parametros.plantas[5][5], 
                 altura = parametros.plantas[5][6],
                 coords = []) -> None:
        self.armadura = int(parametros.ARMADURA)
        super().__init__(tipo, vida_maxima, vida, resistencia, resistencia_termica, congelacion, altura, coords)
    
    
    
    
class Jardin:
    def __init__(self, tablero: list) -> None:
        self.tablero = tablero
        self.inventario_plantas = []
        self.soles = parametros.SOLES_INICIO
        self.temperatura = parametros.TEMP_INICIAL
        self._plantas_en_jardin = []           
  
    @property
    def plantas_en_jardin (self) -> None:
        return self._plantas_en_jardin
    
    @plantas_en_jardin.setter 
    def plantas_en_jardin (self, planta:Planta) -> None:
        if isinstance(planta, Planta):
            self._plantas_en_jardin.append(planta)
            
    def __str__(self) -> str:
        plantas_dispo = self.contador_plantas()
        tablero_en_cadena = "\n".join([str(fila) for fila in self.tablero])
        return ("*** Este es tu Jardín Actual ***        \n"
                f"Temperatura: {self.temperatura}°C     \n"
                "                                       \n"
                f"{tablero_en_cadena}                   \n"
                "                                       \n"
                "Te quedan:                             \n"
                f"{plantas_dispo[0]} solaretillo        \n"
                f"{plantas_dispo[1]} defensauce         \n"
                f"{plantas_dispo[2]} potencilantro      \n"
                f"{plantas_dispo[3]} aresauce           \n"
                f"{plantas_dispo[4]} cilantrillo        \n"
                f"{plantas_dispo[5]} fensaulantro       \n"
                "                                       \n"
                "Inventario Plantas:                    \n"
            f"{[self.inventario_plantas[i].tipo for i in range (len(self.inventario_plantas))]}"
                  
        )
    def instanciador(self, tipo:str, coords:list) -> None:
        tipo_a_clase = {
            parametros.plantas[0][0]: Solaretillo,
            parametros.plantas[1][0]: Defensauce,
            parametros.plantas[2][0]: Potencilantro,
            parametros.plantas[3][0]: Aresauce,
            parametros.plantas[4][0]: Cilantrillo,
            parametros.plantas[5][0]: Fensaulantro
        }
        
        planta_clase = tipo_a_clase.get(tipo)
        if planta_clase:
            if coords != []:
                planta = planta_clase(coords=coords)
                self.plantas_en_jardin = planta
            else:
                planta = planta_clase()
                self.inventario_plantas.append(planta)
    
            
    def contador_plantas (self) -> list:
        self.solar = 0 
        self.defen = 0 
        self.poten = 0
        self.ares = 0 
        self.cilan = 0
        self.fensa = 0
        for i in range (len(self.inventario_plantas)):
            if self.inventario_plantas[i].tipo == parametros.plantas[0][0]:
                self.solar += 1
            elif self.inventario_plantas[i].tipo == parametros.plantas[1][0]:
                self.defen += 1
            elif self.inventario_plantas[i].tipo == parametros.plantas[2][0]:
                self.poten += 1
            elif self.inventario_plantas[i].tipo == parametros.plantas[3][0]:
                self.ares += 1
            elif self.inventario_plantas[i].tipo == parametros.plantas[4][0]:
                self.cilan += 1
            elif self.inventario_plantas[i].tipo == parametros.plantas[5][0]:
                self.fensa += 1
        lista = [self.solar, self.defen, self.poten, self.ares, self.cilan, self.fensa]
        return lista
   
   
    def intercambiar (self, coordenadas: str) -> bool:
        coordenadas = coordenadas.strip().split(";")
        for i in range (len(coordenadas)):
            coordenadas[i] = coordenadas[i].split(",")
        if len(coordenadas) != 2:
            return False
        fila_original = int(coordenadas[0][0])
        columna_original = int(coordenadas[0][1])
        fila_nueva = int(coordenadas[1][0])
        columna_nueva = int(coordenadas[1][1])
        if (fila_nueva >= len(self.tablero)) or (columna_nueva >= len(self.tablero[0])) or (
            fila_original >= len(self.tablero)) or (columna_original >= len(self.tablero[0])):  
            return False
        for i in range (len(self.tablero)):
            for x in range (len(self.tablero[i])):
                if (i == fila_original) and (x == columna_original):
                    if self.tablero[i][x] != "X" and (
                        self.tablero [fila_nueva][columna_nueva] != "X"):
                        for z in range(len(self.plantas_en_jardin)):
                            for y in range(len(self.plantas_en_jardin)):
                                if z != y and (self.plantas_en_jardin[z].coords == [i, x] and 
                                        self.plantas_en_jardin[y].coords == 
                                        [fila_nueva, columna_nueva]):
                                        self.plantas_en_jardin[z].coords = (
                                            [fila_nueva, columna_nueva])
                                        self.plantas_en_jardin[y].coords = [i, x] 
                    elif self.tablero[i][x] == "X" and (
                        self.tablero [fila_nueva][columna_nueva] != "X"):
                        for z in range (len(self.plantas_en_jardin)):
                            if self.plantas_en_jardin[z].coords == [fila_nueva, columna_nueva]:
                                self.plantas_en_jardin[z].coords = [i, x] 
                    if not ((self.tablero[i][x] in [parametros.plantas[i][0] 
                        for i in range (len(parametros.plantas))]) and (
                        self.tablero[fila_nueva][columna_nueva] in ["X"])):
                        valor_original = (self.tablero[fila_original][columna_original])
                        valor_nuevo = (self.tablero[fila_nueva][columna_nueva])
                        (self.tablero[fila_original][columna_original]) = valor_nuevo
                        (self.tablero[fila_nueva][columna_nueva]) = valor_original 
                        return True                                  
        return False
    
    def cultivar(self, tipo:str, coords:str) -> str:
        coords = coords.strip().split(",")
        if (int(coords[0]) >= len(self.tablero)) or (int(coords[1])>= len(self.tablero[0])):
            return("\nPosición inválida\n")
        else:
            for i in range (len(self.tablero)):
                for x in range (len(self.tablero[i])):
                    if (i == int(coords[0])) and (x == int(coords[1])):
                        if self.tablero[i][x] != "X":
                            for n in range (len(self.plantas_en_jardin)):
                                if self.plantas_en_jardin[n].coords == [i, x]:
                                    self.plantas_en_jardin.pop(n)    
                        for y in range (len(self.inventario_plantas)):
                            if self.inventario_plantas[y].tipo == tipo:
                                self.inventario_plantas.pop(y)
                                break
                        self.instanciador(tipo, [i, x])   
                        self.tablero[i][x] = tipo
                        return "\nCultivo Exitoso\n"
    def mutar (self, codigo_mutacion:int) -> bool:
        plantas = self.contador_plantas()
        if codigo_mutacion == 1:
            solar = False
            defen = False
            if plantas [0] >= 1 and plantas[1] >= 1:
                for z in range (len(self.inventario_plantas)):
                    if self.inventario_plantas[z].__class__.__name__ == "Solaretillo" and (
                        not solar):
                        planta_1 = z
                        solar = True
                        
                    elif self.inventario_plantas[z].__class__.__name__ == "Defensauce" and (
                        not defen
                    ):
                        planta_2 = z
                        defen = True
                    
                    if defen and solar:
                        self.inventario_plantas.pop(planta_1)
                        self.inventario_plantas.pop((planta_2) - 1)
                        self.instanciador("A", [])
                        return True
        elif codigo_mutacion == 2:
            if plantas [0] >= 1 and plantas[2] >= 1:
                solar = False
                poten = False
                if plantas [0] >= 1 and plantas[2] >= 1:
                    for z in range (len(self.inventario_plantas)):
                        if self.inventario_plantas[z].__class__.__name__ == "Solaretillo" and (
                            not solar):
                            planta_1 = z
                            solar = True
                            
                        elif self.inventario_plantas[z].__class__.__name__ == "Potencilantro" and (
                            not poten
                        ):
                            planta_2 = z
                            poten = True
                        
                        if solar and poten:
                            self.inventario_plantas.pop(planta_1)
                            self.inventario_plantas.pop((planta_2) - 1)
                            self.instanciador("A", [])
                            return True
                    
        elif codigo_mutacion == 3:
            defen = False
            poten = False
            if plantas [1] >= 1 and plantas[2] >= 1:
                for z in range (len(self.inventario_plantas)):
                    if self.inventario_plantas[z].__class__.__name__ == "Defensauce" and (
                        not defen):
                        planta_1 = z
                        defen = True
                        
                    elif self.inventario_plantas[z].__class__.__name__ == "Potencilantro" and (
                        not poten
                    ):
                        planta_2 = z
                        poten = True
                    
                    if defen and poten:
                        self.inventario_plantas.pop(planta_1)
                        self.inventario_plantas.pop((planta_2) - 1)
                        self.instanciador("A", [])
                        return True
        return False
            
                
                
        
    def regar(self) -> str:
        texto = ""
        for i in range (len(self.tablero)):
            for x in range (len(self.tablero[i])):
                if self.tablero[i][x] != "X":
                    for z in range(len(self.plantas_en_jardin)):
                        if self.plantas_en_jardin[z].coords == [i, x]:
                            print("hola2")
                            vida_anterior = self.plantas_en_jardin[z].vida
                            regado = randint(0,1)
                            if regado:
                                self.plantas_en_jardin[z].regarse(parametros.RIEGO_1)
                            else: 
                                self.plantas_en_jardin[z].regarse(parametros.RIEGO_2)
                            vida_nueva = self.plantas_en_jardin[z].vida
                            if vida_nueva != vida_anterior:
                                texto += (f"Un {self.plantas_en_jardin[z].__class__.__name__} en " 
                                        f"({i},{x}) ha subido su salud de {vida_anterior} a " 
                                        f"{vida_nueva}\n")
                            break
        return texto    