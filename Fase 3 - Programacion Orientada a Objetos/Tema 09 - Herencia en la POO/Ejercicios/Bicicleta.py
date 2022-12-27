from Vehiculo import *

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo) -> None:
        super().__init__(color, ruedas)
        self._tipo = tipo

    def getTipo(self) -> str:
        return self._tipo

    def __str__(self) -> str:
        return super().__str__() + f", tipo {self._tipo}"
    


