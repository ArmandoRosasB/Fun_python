from Coche import *

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga) -> None:
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.__carga = carga
    
    def getCilindrada(self) -> float:
        return self.__carga
    
    def __str__(self) -> str:
        return super().__str__() + f", carga {self.__carga} kg"


