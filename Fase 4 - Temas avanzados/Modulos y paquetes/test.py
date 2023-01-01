import Mensajes.Bienvenidas.Saludos as Saludos # Importamos el script saludos.py desde un paquete
import Mensajes.Despedidas.Adios as Adios
# Paquete.subpaquete.modulo
'''
Importacion selectiva

from saludos import saludar
from saludos import *

'''
if __name__ == '__main__':
    Saludos.saludar()
    Saludos.Saludo()

    Adios.despedir()
    Adios.Despedida()




