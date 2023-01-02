import Paquete_gestor_de_personajes.Gestor as Gestor
import Paquete_gestor_de_personajes.Personajes as Personaje

if __name__ == '__main__':
    print()
    g = Gestor.Gestor()

    # g.agregar(Personaje.Personajes("Caballero", 4, 2, 4, 2))
    # g.agregar(Personaje.Personajes("Guerrero", 2, 4, 2, 4))
    # g.agregar(Personaje.Personajes("Arquero", 2, 4, 1, 8))
    print()
    g.borrar("Arquero")
    g.mostrar()
  

    print()

