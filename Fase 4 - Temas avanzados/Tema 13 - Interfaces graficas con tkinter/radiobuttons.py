from tkinter import *

def seleccionar():
    monitor.config(text=f"{opcion.get()}")

def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
root.title("RadioButtons")

opcion = IntVar()

frame1 = Frame(root)
frame1.pack()

Radiobutton(frame1, text="Opcion 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(frame1, text="Opcion 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(frame1, text="Opcion 3", variable=opcion, value=3, command=seleccionar).pack()

frame2 = Frame(root)
frame2.pack()

monitor = Label(frame2)
monitor.pack()

frame4 = Frame(root)
frame4.pack()

Button(frame4, text="Reiniciar", command=reset).pack()

root.mainloop()