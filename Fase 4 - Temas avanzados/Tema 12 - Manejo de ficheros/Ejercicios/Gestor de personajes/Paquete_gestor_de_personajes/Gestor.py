
import pickle
from io import open

class Gestor:
    __personajes = []

    def __init__(self) -> None:
        self.cargar()
    
    def agregar(self, p) -> None:
        for personaje in self.__personajes:
            if personaje.getNombre() == p.getNombre():
                return

        self.__personajes.append(p)
        self.guardar()

    def borrar(self, nombre) -> None:
        for i, personaje in enumerate(self.__personajes):
            if personaje.getNombre() == nombre:
                self.__personajes.remove(personaje)
                print(f"Personaje {nombre} eliminado")
                break
        self.guardar()

    def mostrar(self) -> None:
        if len(self.__personajes) == 0:
            print("El gestor esta vacio")
            return
        
        for personaje in self.__personajes:
            print(personaje)
    
    def cargar(self) -> None:
        with open('personajes.pckl', 'ab+') as input:
            input.seek(0)
            try:
                self.__personajes = pickle.load(input)

            except EOFError:
                # print("El fichero esta vacio")
                pass

            finally:
                print(f"Se han cargado {len(self.__personajes)} personajes")

    def guardar(self) -> None:
        with open('personajes.pckl', 'wb') as output:
            pickle.dump(self.__personajes, output)

    def __del__(self):
        self.guardar()
