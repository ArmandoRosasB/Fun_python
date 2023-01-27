from django.db import models

# Create your models here.

'''
Modelos: Clases para definir la estructura de los datos para la base de
datos de django.

Cada que creemos un registro django nos permitira recuperarlas en 
forma de objetos y modificar su informacion como si fueran lso atributos
de un objeto.

Al guardarlo se escribira en la base de datos.
'''

class Post(models.Model):
    title = models.CharField(max_length=200) # VARCHAR
    content = models.TextField() # TEXT Longitud dinamica
    created = models.DateTimeField(auto_now_add=True) # DATETIME
    modified = models.DateTimeField(auto_now=True)
