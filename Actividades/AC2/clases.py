class Vehiculo:
    identificador = 0
    def __init__(self, rendimiento: int, marca: str, energia = 111.5, *args, **kwargs) -> None:
        self.rendimiento = int(rendimiento)
        self.marca = marca
        self._energia = float(energia)
        self.identificador = Vehiculo.identificador
        Vehiculo.identificador +=1
        if self._energia < 0:
            self._energia = 0.0
            
    @property
    def autonomia(self) -> float:
        return float(self._energia * self.rendimiento)
    
    @property
    def energia (self) ->float:
        return float(round(self._energia,1))
    
    @energia.setter
    def energia(self, energia: float):
        (self._energia) = float(energia)
        if self._energia < 0:
            (self._energia) = 0.0
        
class AutoBencina(Vehiculo):
    def __init__(self, bencina_favorita: str, **kwargs ) -> None:
        super().__init__(**kwargs)
        self.bencina_favorita = bencina_favorita
        
    def recorrer(self, kilometros:float) -> str:
        if kilometros <= self.autonomia:
            n = kilometros
            z = round(kilometros / self.rendimiento, 1)
            
        else: 
            n = self.autonomia
            z = round(self.autonomia / self.rendimiento , 1)
        
        self.energia -= z
            
        return f"Anduve {n}Km y eso consume {z}L de bencina"
    
class AutoElectrico(Vehiculo):
    def __init__(self, vida_util_bateria: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.vida_util_bateria = vida_util_bateria
    def recorrer(self, kilometros:float) -> str:
        if kilometros <= self.autonomia:
            n = kilometros
            z = round(kilometros / self.rendimiento, 1)
            
        else: 
            n = self.autonomia
            z = round(self.autonomia / self.rendimiento , 1)
        
        self.energia -= z
            
        return f"Anduve {n}Km y eso consume {z}W de energia electrica"
        

class Camioneta(AutoBencina):
    def __init__(self, capacidad_maleta: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.capacidad_maleta = capacidad_maleta
class Telsa(AutoElectrico):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def recorrer(self, kilometros: float) -> str: 
        return f"{super().recorrer(kilometros)} de forma muy inteligente" 

class FaitHibrido(AutoElectrico, AutoBencina):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs, vida_util_bateria = 5)
        
    def recorrer(self, kilometros: float) -> str:
        if kilometros > 10:
            bencina = AutoBencina.recorrer(self, 10)
            kilometros_restantes = kilometros - 10
            electrico = AutoElectrico.recorrer(self, kilometros_restantes)
            return f"{bencina} {electrico}"
        else:
            return AutoElectrico.recorrer(self, kilometros)
        


