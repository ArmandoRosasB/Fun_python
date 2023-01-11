import sqlite3

if __name__ == '__main__':
    try:
        link = sqlite3.connect('usuarios_autoincrementales.db')
        print("Successfully Connected to SQLite")

        cursor = link.cursor()
        
 #       cursor.execute('SELECT * FROM usuarios WHERE dni = "33333333C"')
 #       usuario = cursor.fetchone()
 #       print (usuario)

 #       cursor.execute("UPDATE usuarios SET nombre = 'Hector Costa', edad = 30 WHERE dni = '11111111A'")

        cursor.execute("DELETE FROM usuarios WHERE dni = '11111111A'")
        link.commit()
        print("The SQL execution was successfully inserted")

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if link:
            link.close()

        print("The SQLite connection is closed")