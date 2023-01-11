import sqlite3

if __name__ == '__main__':
    try:
        link = sqlite3.connect("usuarios.db")
        cursor = link.cursor()

        print("Successfully Connected to SQLite")

        cursor.execute('''
            CREATE TABLE usuarios (
                dni VARCHAR(9) NOT NULL PRIMARY KEY,
                nombre VARCHAR(50),
                edad INT,
                email VARCHAR(50)
        );
        ''')

        usuarios = [
            ('11111111A', 'Hector', 27, 'hector@ejemplo.com'),
            ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
            ('33333333C', 'Juan', 19, 'juan@ejemplo.com'),
            ('44444444D', 'Armando', 19, 'armando.rosas133@gmail.com')
        ]

        cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

        link.commit()
        print("Record inserted successfully into usuarios table") 
        cursor.close()
    
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if link:
            link.close()

        print("The SQLite connection is closed")
