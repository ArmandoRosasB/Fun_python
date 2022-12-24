'''
) Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. 
Al parecer contiene el nombre de un alumno y la nota de un exámen.
¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?:

Nombre Apellido ha sacado un Nota de nota.
Ayuda: Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: *cadena[::-1]** *
'''

cadena = "zeréP nauJ,01"

# Completa el ejercicio aquí

cadena_ordenada = cadena[::-1]

cadena_correcta = (cadena_ordenada[3:7] + " " + cadena_ordenada[-5:]
+ " ha sacado una Nota de " + cadena_ordenada[0:2])

print(cadena_correcta)