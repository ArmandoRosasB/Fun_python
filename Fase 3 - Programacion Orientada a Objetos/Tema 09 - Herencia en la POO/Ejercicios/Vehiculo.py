class Vehiculo():
    
    def __init__(self, color, ruedas) -> None:
        self._color = color
        self._ruedas = ruedas

    def getColor(self) -> str:
        return self._color

    def getRuedas(self) -> int:
        return self._ruedas

    def __str__(self) -> str:
        return f"Color {self._color}, {self._ruedas} ruedas"