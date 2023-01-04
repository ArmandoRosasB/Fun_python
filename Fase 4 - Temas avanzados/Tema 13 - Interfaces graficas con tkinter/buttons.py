from tkinter import *

def hola():
    print("Hola mundo")

def crear_label():
    Label(root, text="Label creada dinamicamente").pack()


root = Tk()


Button(root, text="Presioname", command=crear_label).pack()




root.mainloop()