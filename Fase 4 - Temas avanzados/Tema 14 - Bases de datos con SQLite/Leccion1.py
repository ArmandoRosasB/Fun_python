import sqlite3

link = sqlite3.connect('ejemplo.db')

cursor = link.cursor()

# cursor.execute('CREATE TABLE  usuarios (nombre VARCHAR(100), edad INT, email VARCHAR(100))')
# cursor.execute('INSERT INTO usuarios(nombre, edad, email) VALUES ("Armando",19,"armando.rosas133@gmail.com")')

# cursor.execute('SELECT * FROM usuarios')

# usuario = cursor.fetchone() # fetchone -> Recuperar el primer registro
# print(usuario[0])

# usuarios = [
#   ('Hector', 27, 'hector@ejemplo.com'),
#    ('Mario', 51, 'mario@ejemplo.com'),
#    ('Juan', 19, 'juan@ejemplo.com')
# ]

# cursor.executemany("INSERT INTO usuarios(nombre, edad, email) VALUES (?, ?, ?)", usuarios)

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall() # fetchall -> Recuperar todos los registros

for usuario in usuarios:
    print("Nombre:",usuario[0], " - Email:", usuario[2])

link.commit()
link.close()