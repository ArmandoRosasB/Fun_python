# Variables del ejercicio (no modifiques esta línea)
animales = {"caballo":"", "vaca":""}

animales_aniadir = {"perro": "dog", "gato":"cat", "rana":"frog"}
# completa el ejercicio
for clave, animal in animales_aniadir.items():
    animales[clave] = animal

animales["caballo"] = "horse"
animales["vaca"] = "cow"

del(animales["rana"])
del(animales["vaca"])


for clave, animal in animales.items():
    print(clave, animal)
