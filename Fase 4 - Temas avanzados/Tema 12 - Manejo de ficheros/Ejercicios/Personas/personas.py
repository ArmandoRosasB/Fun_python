from io import open

if __name__ == '__main__':

    informacion = {"contactos": []}

    with open('personas.txt', 'r', encoding='utf8') as input:
        lineas = input.readlines()

    for linea in lineas:
        aux = linea.split(';')
        informacion['contactos'].append({'id': aux[0], 'nombre': aux[1], 'apellido':aux[2], 'nacimiento': aux[3]})

    print()
    for persona in informacion['contactos']:
        print(f"(id={persona['id']}) {persona['nombre']} {persona['apellido']} => {persona['nacimiento']}", end='')

print()
print()