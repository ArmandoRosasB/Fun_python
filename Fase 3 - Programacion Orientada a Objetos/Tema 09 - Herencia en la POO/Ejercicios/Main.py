import Coche
import Camioneta
import Bicicleta
import Motocicleta



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
    Coche.Coche("azul", 4, 150, 1200),
    Camioneta.Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta.Bicicleta("verde", 2, "urbana"),
    Motocicleta.Motocicleta("negro", 2, "deportiva", 180, 900)
]

print()
catalogar(vehiculos)

print()
print()

catalogar(vehiculos, 4)

print()