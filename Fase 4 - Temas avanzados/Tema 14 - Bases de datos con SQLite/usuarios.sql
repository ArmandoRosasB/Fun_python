CREATE DATABASE usuarios;
USE usuarios;

CREATE TABLE usuarios (
    dni VARCHAR(9) NOT NULL PRIMARY KEY,
    nombre VARCHAR(50),
    edad INTEGER,
    email VARCHAR(50)
);

INSERT INTO usuarios(dni, nombre, edad, email) VALUES
    ('11111111A', 'Hector', 27, 'hector@ejemplo.com'),
    ('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
    ('33333333C', 'Juan', 19, 'juan@ejemplo.com'),
    ('44444444D', 'Armando', 19, 'armando.rosas133@gmail.com');


/* Queries */

SELECT * FROM usuarios WHERE edad = 19;
UPDATE usuarios SET nombre = 'Hector Costa', edad = 30 WHERE dni = '11111111A';
DELETE FROM usuarios WHERE dni = '11111111A';