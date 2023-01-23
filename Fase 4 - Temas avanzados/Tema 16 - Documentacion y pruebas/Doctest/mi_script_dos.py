def doblar(lista):
    """
    Dobla el valor de los elementos de una lista

    >>> l = [1, 2, 3, 4, 5]
    >>> doblar(l)
    [2, 4, 6, 8, 10]

    >>> l  = []
    >>> for i in range(10):
    ...     l.append(i)
    >>> doblar(l)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    return [i * 2 for i in lista]

def sumar(a, b):
    """
    Esta funcion recibe dos parametros y devuelve la suma de ambos

    Pueden ser numeros:

    >>> sumar(5, 10)
    15

    Cadenas de texto:

    >>> sumar('aa', 'bb')
    'aabb'

    Listas

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> sumar(a, b)
    [1, 2, 3, 4, 5, 6]

    Sumar distintos tipos:

    >>> sumar(10, 'hola')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


if __name__ == '__main__':
    import doctest
    doctest.testmod()