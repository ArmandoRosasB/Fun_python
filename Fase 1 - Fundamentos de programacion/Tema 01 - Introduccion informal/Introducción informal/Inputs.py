# Completa el ejercicio

'''
 ** Inputs **

'''

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")

edad = int(input("Introduce tu edad: "))
numero_magico = float(input("Introduce un numero entero o decimal: "))

numero_suerte = edad * numero_magico

numero_suerte= str(numero_suerte) #Transformar un nuemri a str, asi como int() o float()

cadena_final = nombre + " " +apellido + ": Tu número de la suerte es el " + numero_suerte

print(cadena_final)