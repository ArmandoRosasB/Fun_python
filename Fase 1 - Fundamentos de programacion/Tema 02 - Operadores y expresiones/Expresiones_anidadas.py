# no borres esta línea
from evaluate import edad, nombre

# completa el ejercicio
expresion = ((nombre != "****") and (edad > 10 and edad < 18) and 
(len(nombre) >= 3 and len(nombre) < 10))

print(expresion)