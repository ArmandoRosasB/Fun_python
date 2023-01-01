def suma(num1 = None, num2 = None):
    if num1 == None or num2 == None:
        print("Error, debes enviar dos numeros a la función")
        return
    try:
        return num1 + num2
    except TypeError:
        print("Error: Tipo de dato no valido")
        return

def resta(num1 = None, num2 = None):
    if num1 == None or num2 == None:
        print("Error, debes enviar dos numeros a la función")
        return
    try:
        return num1 - num2
    except TypeError:
        print("Error: Tipo de dato no valido")
        return

def producto(num1 = None, num2 = None):
    if num1 == None or num2 == None:
        print("Error, debes enviar dos numeros a la función")
        return
    try:
        return num1 * num2
    except TypeError:
        print("Error: Tipo de dato no valido")
        return
    
def division(num1 = None, num2 = None):
    if num1 == None or num2 == None:
        print("Error, debes enviar dos numeros a la función")
        return
    try:
        return num1 / num2
    except TypeError:
        print("Error: Tipo de dato no valido")
        return
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
        return
    
        
