import sys

if len(sys.argv) != 2:
    print("\nError - Introduce el argumento solicitado")
    print("Ejemplo: py talba.py int")
    sys.exit("\nSystemExit: Numero de argumentos incorrecto")

if not sys.argv[1].isnumeric():
    sys.exit("SystemExit: El argumento no es de tipo integer")


length = len(sys.argv[1])
num = int(sys.argv[1])


for i in range(length):
    aux = (num % 10) * (10 ** i)
    print(f"{aux:0{length}}")
    num //= 10

