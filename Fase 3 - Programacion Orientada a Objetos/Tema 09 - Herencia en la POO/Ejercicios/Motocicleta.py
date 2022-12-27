from Bicicleta import *

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada) -> None:
        super().__init__(color, ruedas, tipo)
        self.__velocidad = velocidad
        self.__cilindrada = cilindrada
    
    def getVelocidad(self) -> float:
        return self.__velocidad
    
    def getCilindrada(self) -> int:
        return self.__cilindrada
    
    def __str__(self) -> str:
        return super().__str__() + f", velocidad {self.__velocidad}, cilindrada {self.__cilindrada}"