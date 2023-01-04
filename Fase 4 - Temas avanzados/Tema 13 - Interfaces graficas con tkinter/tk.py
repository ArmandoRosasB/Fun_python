# Importamos todos los widgets del modulo tkinter 
from tkinter import *

'''
=================== Root ====================
'''
# Definimos una raiz a partir del widget Tk
root = Tk()

# Asignamos un titulo a la ventana
root.title("Hola mundo")

# Cambiamos el icono de la ventana
root.iconbitmap("coffee.ico")

# Esatblecemos si es posible redimensionar la ventana
# (Ancho, Alto)
root.resizable(True, True)



'''
================== Frame ====================
'''

# Creacion de un frame en la raiz indicada
# En px
frame = Frame(root, width=480, height=320)

# El frame se emaqueta y distribuye en la raiz
# side => bottom, top, left, right
# anchor => n, s, e, w
# frame.pack(side="top", anchor="e")

# fill => x Rellenar en horizontal

# Se expande en vertical
# frame.pack(fill='y', expand='1')

# Se expande al mismo tamano que su widget padre
frame.pack(fill="both", expand='1')

# Configuracion del frame

frame.config(cursor="pirate")

# Background color
frame.config(bg="lightblue")

# Broder
frame.config(bd=25)

# Tipo de borde
frame.config(relief="solid")

# Configuracion de root
root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

# Ponemos en marcha el programa principal
root.mainloop()
