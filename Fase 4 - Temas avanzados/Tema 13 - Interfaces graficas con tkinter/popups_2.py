from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

def test():
    # Regresa ((r, g, b), '#hex')
    # color = ColorChooser.askcolor(title="Elige un color")
    # print(color)

    # Regresa la ruta
    # ruta = FileDialog.askopenfilename(title= "Abrir un fichero", initialdir=r"C:\Users\arman\OneDrive\Documents",
    #     filetypes=(("Ficheros de texto", "*.txt"), 
    #         ("Ficheros binarios pickle", "*.pckl"),
    #         ("Todos los ficheros", "*.*")))
    # print(ruta)

    # Equivale a open('ruta', 'w')
    fichero = FileDialog.asksaveasfile(title="Guardando un fichero", mode='a+',
    defaultextension=".txt")

    if fichero is not None:
        fichero.write("Hola!")
        fichero.close()
        print(fichero)




root = Tk()


Button(root, text="Presioname", command=test).pack()


root.mainloop()