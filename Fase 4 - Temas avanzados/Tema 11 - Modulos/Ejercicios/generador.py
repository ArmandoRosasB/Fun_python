import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            numero = int(input(mensaje))
        except:
            print("Numero no valida")
        else:
            if numero >= ini and numero <= fin:
                break
    
    return numero

def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1] Al alza [2] A la baja [3] Normal: ")

    aleatory_numbers = []

    for i in range(numeros):
        aux = random.uniform(0, 101)
        if modo == 1:
            print(f"{aux} => {math.ceil(aux)}")
            aleatory_numbers.append(math.ceil(aux))

        elif modo == 2:
            print(f"{aux} => {math.floor(aux)}")
            aleatory_numbers.append(math.floor(aux))

        else:
            print(f"{aux} => {round(aux)}")
            aleatory_numbers.append(round(aux))

    return aleatory_numbers

def main():
    lista = generador()
    print()
    print(lista)


if __name__ == '__main__':
    main()
