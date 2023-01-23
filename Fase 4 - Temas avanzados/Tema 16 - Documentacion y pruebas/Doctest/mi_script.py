def suma(a, b):
    """
    La funcion suma(a, b) recibe dos parametros a y b.
    Devuelve la suma de ambos
    
    >>> suma(5, 10)
    15

    >>> suma(0, 0)
    0

    >>> suma(-5, 7)
    2
    """
    return a + b

def palindromo(palabra):
    """
    La funcion palindromo(palabra) recibe una palabra.
    Si la alabra es un palindromo devuelve True, si no False

    Un palindromo es una palabra o frase que se lee igual
    tanto de izquierda a derecha como de derecha a izquierda.

    >>> palindromo('radar')
    True

    >>> palindromo('somos')
    True

    >>> palindromo('hola')
    False

    >>> palindromo('Ana')
    True

    >>> palindromo('Anita lava la tina')
    True

>>> 
    """
    if palabra.lower().replace(" ", "") == palabra[::-1].lower().replace(" ", "") :
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod() # py mi_script.py -v




