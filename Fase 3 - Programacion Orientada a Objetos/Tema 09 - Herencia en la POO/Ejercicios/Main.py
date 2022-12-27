from Coche import *
from Camioneta import *
from Bicicleta import *
from Motocicleta import *



def catalogar(vehiculos, ruedas = None):
    if ruedas == None:
        for v in vehiculos:
            print(type(v).__name__, v)
        
    else:
        i = 0
        for v in vehiculos:
            if v.getRuedas() == ruedas:
                print(v)
                i += 1
        
        print(f"\nSe han encontrado {i} vehiculos con {ruedas} ruedas")


vehiculos = [
    Coche("azul", 4, 150, 1200),
    Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta("verde", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

print()
catalogar(vehiculos)

print()
print()

catalogar(vehiculos, 4)

print()