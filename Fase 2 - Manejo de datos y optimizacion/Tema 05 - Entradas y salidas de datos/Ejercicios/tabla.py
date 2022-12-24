import sys

if len(sys.argv) != 3:
    print("\nError - Introduce los argumentos solicitados")
    print("Ejemplo: py talba.py int int")
    sys.exit("\nSystemExit: Numero de argumentos incorrecto")


if not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
    sys.exit("\nSystemExit: Argumento(s) diferentes a integers")

rows = int(sys.argv[1])
cols = int(sys.argv[2])
if (rows < 1 or rows > 9) or (cols < 1 or cols > 9):
    sys.exit("\nSystemExit: Argumento(s) fuera de limites")


for row in range(rows):
    for col in range(cols):
        print("*", end=" ")
    print()

