'''
Realiza una función recursiva llamada sumatorio(numero), que sin utilizar ningún bucle, 
sume todos los números desde numero hasta 1 y devuelva la suma total, dando por hecho que numero es siempre un entero.
'''

def sumatorio(numero):
    if numero == 1:
        return 1
    else:
        return numero + sumatorio(numero - 1)