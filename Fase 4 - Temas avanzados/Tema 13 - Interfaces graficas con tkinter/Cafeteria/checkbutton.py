from tkinter import *

def Seleccionar():
    cadena = ""
    if leche.get() == 1:
        cadena += "Con leche"
    else:
        cadena += "Sin leche"
    
    if azucar.get() == 1:
        cadena += " y con azucar"
    else:
        cadena += " y sin azucar"

    monitor.config(text=cadena)

root = Tk()
root.title("Cafeteria")
root.resizable(False, False)
root.config(bd=15)

leche = IntVar()        # 1 si, 0 no
azucar = IntVar()       # 1 si, 0 no

imagen = PhotoImage(file="imagen.gif")

masterFrame = Frame(root)
masterFrame.pack(side="top")

frame1 = Frame(masterFrame)
frame1.pack(side="left")

Label(frame1, image=imagen).pack(side="left")

frame2 = Frame(masterFrame)
frame2.pack(side="right")

Label(frame2, text="¿Como quieres tu cafe?").pack(anchor="w")
Checkbutton(frame2, text="Leche", variable=leche, onvalue=1, offvalue=0, command=Seleccionar).pack(anchor="w")
Checkbutton(frame2, text="Azucar", variable=azucar, onvalue=1, offvalue=0, command=Seleccionar).pack(anchor="w")

frame3 = Frame(root)
frame3.pack(side="bottom")

monitor = Label(frame3)
monitor.pack()

root.mainloop()