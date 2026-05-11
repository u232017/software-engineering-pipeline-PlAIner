def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def power(base, exponente):
    return base ** exponente


def root(index, radicand):
    if index == 0:
        raise ValueError("El índice de la raíz no puede ser cero.")
    if radicand < 0 and index % 2 == 0:
        raise ValueError("No se puede calcular la raíz par de un número negativo.")
    if radicand < 0:
        return -((-radicand) ** (1 / index))
    return radicand ** (1 / index)
