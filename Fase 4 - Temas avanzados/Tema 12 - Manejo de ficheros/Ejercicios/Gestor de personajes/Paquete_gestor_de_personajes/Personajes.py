class Personajes:
    def __init__(self, nombre, vida, ataque, defensa, alcance) -> None:
        self.__nombre = nombre
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa
        self.__alcance = alcance
    
    def getNombre(self) -> str:
        return self.__nombre

    def __str__(self) -> str:
        return f"{self.__nombre} => {self.__vida} vida, {self.__ataque} ataque, {self.__defensa} defensa, {self.__alcance} alcance"
    
    