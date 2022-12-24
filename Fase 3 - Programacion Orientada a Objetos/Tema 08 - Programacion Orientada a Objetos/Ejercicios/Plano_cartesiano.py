import math

class Coordenada:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    
    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def cuadrante(self):
        if self.__x == 0 and self.__y == 0:
            return f"{self} pertenece al origen"
        
        if self.__x > 0 and self.__y > 0:
            return f"{self} pertenece al primer cuadrante"
        
        if self.__x > 0 and self.__y < 0:
            return f"{self} pertenece al cuarto cuadrante"
        
        if self.__x < 0 and self.__y > 0:
            return f"{self} pertenece al segundo cuadrante"
        
        else:
            return f"{self} pertenece al tercer cuadrante"
        
    def vector(self, other):
        return f"El vector entre {self} y {other} es ({other.__x - self.__x}, {other.__y - self.__y})"
    
    def distancia(self, other):
        aux = (other.__x - self.__x)**2 + (other.__y - self.__y)**2
        aux = math.sqrt(aux)
        return f"La distancia entre {self} y {other} puntos es de {aux:.4f} unidades"



class Rectangulo:
    def __init__(self, d_inf = Coordenada(), d_sup = Coordenada()):
        self.__d_inf = d_inf
        self.__d_sup = d_sup
    
    def base(self):
        base = self.__d_sup.getX() - self.__d_inf.getX()
        return abs(base)
    
    def altura(self):
        altura = self.__d_sup.getY() - self.__d_inf.getY()
        return abs(altura)
    
    def area(self):
        return self.altura() * self.base()

    

# Experimentacion

A = Coordenada(2, 3)
B = Coordenada(5, 5)
C = Coordenada(-3, -1)
D = Coordenada()

print(f"Coordenada A: {A}")
print(f"Coordenada B: {B}")
print(f"Coordenada C: {C}")
print(f"Coordenada D: {D}")

print()

print(f"A{A.cuadrante()}")
print(f"C{C.cuadrante()}")
print(f"D{D.cuadrante()}")

print()

print(A.vector(B))
print(B.vector(A))

print()

print(A.distancia(B))
print(B.distancia(A))

print()

# Considerando que no hay dos puntos iguales

if A.distancia(D) < B.distancia(D) and A.distancia(D) < C.distancia(D):
    print("El punto A es el mas cercano al origen")
elif B.distancia(D) < A.distancia(D) and B.distancia(D) < C.distancia(D):
    print("El punto B es el mas cercano al origen")
else:
    print("El punto C es el mas cercano al origen")


R1 = Rectangulo(A, B)

print(f"La base del rectangulo formado por {A} y {B} es de {R1.base()}")
print(f"La altura del rectangulo formado por {A} y {B} es de {R1.altura()}")
print(f"El area del rectangulo formado por {A} y {B} es de {R1.area()}")
    