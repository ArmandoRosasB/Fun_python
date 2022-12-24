import sys

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    
    for repeticion in range(repeticiones):
        print(texto)

else:
    print("Error - Introduce los argumentos solicitados")
    print("Ejemplo: py Escribir_lineas.py \"Texto\" 5")