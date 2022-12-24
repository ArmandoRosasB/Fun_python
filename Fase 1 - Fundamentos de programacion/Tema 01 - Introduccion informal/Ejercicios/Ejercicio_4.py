'''
4) A partir del ejercicio anterior, vamos a suponer que cada número es una nota, 
y lo que queremos es obtener la nota media. 

El problema es que cada nota tiene un valor porcentual: *

La primera nota vale un 15% del total
La segunda nota vale un 35% del total
La tercera nota vale un 50% del total
Desarrolla un programa para calcular perfectamente la nota final.

'''

nota_1 = 10
nota_2 = 7
nota_3 = 4

porcentaje_1 = nota_1 * .15
porcentaje_2 = nota_2 * .35
porcentaje_3 = nota_3 * .5

nota_final = porcentaje_1 + porcentaje_2 + porcentaje_3
print("La nota final es de:", "{0:.2f}".format(nota_final))