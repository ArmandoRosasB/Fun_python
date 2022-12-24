# Variables del ejercicio (no las edites)
from evaluate import cadena_1, cadena_2

# Completa el ejercicio a partir de aquí
if (len(cadena_1) > len(cadena_2)):
    resultado = 1
elif (len(cadena_2) > len(cadena_1)):
    resultado = 2
else:
    resultado = 0

print("El resultado es", resultado)
