# Completa el ejercicio en la siguiente línea
from evaluate import numeros

numeros = list(filter(lambda x: x % 5 == 0, map(lambda n : n/2, numeros)))

print(numeros)