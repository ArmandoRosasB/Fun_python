import random

numero = random.randint(10, 20)
lista = []
sumatorio = 0

# Completa el ejercicio aquí

for i in range(numero + 1):
    if((i%5 ==0) or (i %7 == 0)):
        pass
    else:
        lista.append(i)
        sumatorio += i

print(lista)
print(sumatorio)