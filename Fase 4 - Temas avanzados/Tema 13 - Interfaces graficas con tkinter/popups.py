from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()


def test():
    # MessageBox.showinfo("Titulo", "Mensaje")
    # MessageBox.showwarning("Alerta", "Seccion solo para admins")
    # MessageBox.showerror("Error", "Ha ocurrido un error inesperado")

    # Devuelve yes o no
    # resultado = MessageBox.askquestion("Salir", "¿Esta seguro que desea salir sin guardar?")

    # if resultado == "yes":
    #     root.destroy() # Romper la ejecucion del programa

    # Devuelve true o false
    # flag = MessageBox.askyesno("Salir", "¿Sobreescribir el fichero actual?")

    # if flag:
    #     root.destroy()

    resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar")
    if not resultado:
        root.destroy()

Button(root, text="Presioname", command=test).pack()



root.mainloop()