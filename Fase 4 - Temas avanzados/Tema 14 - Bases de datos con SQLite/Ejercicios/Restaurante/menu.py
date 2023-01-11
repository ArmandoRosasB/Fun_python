import sqlite3
from tkinter import *


root = Tk()
root.title("Mexicali's")
root.iconbitmap('meal.ico')

root.resizable(False, False)

top = Frame(root)
top.pack()

Label(top, text="           Ramona's          ", fg='tomato3', font=('Times New Roman', 30, 'bold italic')).pack()
Label(top, text="Menu del dia", fg='tomato2', font=('Times New Roman', 26, 'bold italic')).pack()
Label(root, text="").pack()


link = sqlite3.connect('restaurante.db')
cursor = link.cursor()

categorias = cursor.execute('SELECT * FROM categoria').fetchall()


for categoria in categorias:
    Label(root, text= categoria[1], fg='grey20', font=('Times New Roman', 18, 'bold italic')).pack()

    platillos = cursor.execute(f"SELECT * FROM plato WHERE categoria_id = '{categoria[0]}'").fetchall()
    for platillo in platillos:
        Label(root, text=platillo[1], fg='light salmon', font=('Times New Roman', 14, 'bold italic')).pack()

    Label(root, text="").pack()

Label(root, text="$120 Incluye bebida", fg='tomato3', font=('Times New Roman', 16, 'bold italic') ).pack(anchor='se')


root.config(highlightbackground='salmon', highlightcolor='salmon', highlightthickness=2, bd=0)


root.mainloop()