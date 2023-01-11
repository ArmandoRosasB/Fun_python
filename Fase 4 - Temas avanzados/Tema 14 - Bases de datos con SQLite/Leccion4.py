import sqlite3

if __name__ == '__main__':
    try:
        link = sqlite3.connect('usuarios_autoincrementales.db')
        print("Successfully Connected to SQLite")

        cursor = link.cursor()

        cursor.execute('''
            CREATE TABLE usuarios(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                dni VARCHAR(9) UNIQUE,
                nombre VARCHAR(100),
                edad INTEGER,
                email VARCHAR(50)
            )
        ''')

        usuarios = [
            ('11111111A', 'Hector', 27, 'hector@ejemplo.com'),
            ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
            ('33333333C', 'Juan', 19, 'juan@ejemplo.com'),
            ('44444444D', 'Armando', 19, 'armando.rosas133@gmail.com')
        ]

        cursor.executemany('INSERT INTO usuarios VALUES (NULL,?,?,?,?)',
        usuarios)
        

        link.commit()
        print("The SQL execution was successfully inserted")

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if link:
            link.close()

        print("The SQLite connection is closed")