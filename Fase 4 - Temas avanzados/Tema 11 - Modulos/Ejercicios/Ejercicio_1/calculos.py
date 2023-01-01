import Operaciones.Operaciones as Operaciones


if __name__ == '__main__':
    
    a, b, c, d = 10, 5, 0, "Hola"

    print(f"{a} + {b} = {Operaciones.suma(a, b)}")
    print(f"{b} - {d} = {Operaciones.resta(b, d)}")
    print(f"{b} * {b} = {Operaciones.producto(b, b)}")
    print(f"{a} / {c} = {Operaciones.division(a, c)}")
