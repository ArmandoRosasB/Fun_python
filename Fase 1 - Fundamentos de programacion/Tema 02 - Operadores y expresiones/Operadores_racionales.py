# no borres esta línea
expresiones = [False == True, 10>= 2*4, 33/3 == 11,
True > False, True*5 == 2.5*2]

# completa el ejercicio

resultados = [0, 0, 0, 0, 0]
i= 0
while(i < len(expresiones)):
    if expresiones[i] == True:
        resultados[i] = True
       
    if expresiones[i] == False:
        resultados[i] = False
    
    i = i+1

print(resultados)
