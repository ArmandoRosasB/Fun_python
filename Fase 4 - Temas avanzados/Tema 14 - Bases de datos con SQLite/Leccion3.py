import sqlite3

if __name__ == '__main__':
    try:
        link = sqlite3.connect('productos.db')
        print("Successfully Connected to SQLite")

        cursor = link.cursor()

 #       cursor.execute('''
 #           CREATE TABLE productos (
 #               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 #               nombre VARCHAR(50) NOT NULL,
 #               marca VARCHAR(25) NOT NULL,
 #               precio FLOAT NOT NULL
 #           );
 #       ''')

 #       productos = [
 #           ('Teclado', 'Logitech', 19.95),
 #           ('Pantalla', 'LG', 89.95)
 #       ]

 #       cursor.executemany('INSERT INTO productos VALUES (NULL,?,?,?)', productos)

        cursor.execute('SELECT * FROM productos')

        productos = cursor.fetchall()
        for producto in productos:
            print(producto)


        link.commit()
        print("The SQL execution was successfully inserted")

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if link:
            link.close()

        print("The SQLite connection is closed")