'''
Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres argumentos:
El primero es el número a recortar

El segundo es el límite inferior

El tercero el límite superior.

La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste

Devolver el límite superior si el número es mayor que éste.

Devolver el número sin cambios si no se supera ningún límite.

'''

def recortar(numero, minimo, maximo):
    if numero > maximo:
        return maximo
    elif numero < minimo:
        return minimo
    else:
        return numero