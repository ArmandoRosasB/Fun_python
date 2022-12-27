from Vehiculo import *

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada) -> None:
        super().__init__(color, ruedas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada
    
    def getVelocidad(self) -> float:
        return self._velocidad
    
    def getCilindrada(self) -> int:
        return self._cilindrada

    def __str__(self) -> str:
        return super().__str__() + f", {self._velocidad} km/h, {self._cilindrada} cc"



    


    


