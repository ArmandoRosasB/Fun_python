from tkinter import *

# Configuracion de la raiz
root = Tk()
root.title("Using Labels")
root.iconbitmap("coffee.ico")


# Variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")

# Configuracion de las labels
Label(root, text="Hola mundo!").pack(anchor="nw")
label = Label(root, text="Otra etiqueta!")
label.pack(anchor="center")
Label(root, text="Ultima etiqueta!").pack(anchor="se")


# fg => color del texto
# font (tipo de fuente, tamanio)
label.config(bg = "green", fg="blue", font=("Verdana", "24"))
label.config(textvariable=texto)

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="bottom")

# Bucle de la aplicacion
root.mainloop()