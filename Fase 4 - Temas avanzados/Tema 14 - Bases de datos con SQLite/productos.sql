CREATE DATABASE productos;
USE productos;

CREATE TABLE productos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(50) NOT NULL,
    marca VARCHAR(25) NOT NULL,
    precio FLOAT NOT NULL
);
INSERT INTO productos(nombre, marca, precio) VALUES 
    ('Teclado', 'Logitech', 19.95),
    ('Pantalla', 'LG', 89.95);
