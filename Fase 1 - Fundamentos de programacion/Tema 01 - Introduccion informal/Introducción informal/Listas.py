# no modifiques el nombre de ninguna variable, puedes crear nuevas
lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

# completa el ejercicio
lista1.append(1234)
lista1.append("Hola")
sublista2 = ["Adiós", 1234]
lista2 = lista2 + sublista2
lista3 = lista1[:(len(lista1)-1)]
lista4 = lista2[1:(len(lista2)-1) ]
lista5 = lista4 + lista3

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)