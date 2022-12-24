multiplos = []

# Completa el ejercicio 
numero = 0
while((numero < 1) or (numero > 9)):
    numero = int(input("Introduce un numero entre 1 y 9: "))


multiplos = list(range(0, 100, numero))
multiplos = multiplos[1:]

print(multiplos)

