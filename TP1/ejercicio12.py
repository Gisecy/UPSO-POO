# EJERCICIO 12:

"""
a) Implementar una función que permita extraer la última cifra de un número entero
positivo (es decir, la cifra de unidad).
b) Implementar una función que permita extraer todas las cifras excepto la última
cifra de un número entero positivo (es decir, todas menos la cifra de unidad).
c) Implementar una función que devuelva la cantidad de cifras que contiene un número
entero positivo.
"""

def ultimaCifra(numero):
    """Extrae la última cifra de un número entero positivo.

    Args:
        numero: El número entero del que se extraerá la última cifra.

    Returns:
        La última cifra del número.
    """

    return numero % 10

def cifrasSinUltima(numero):
    """Extrae todas las cifras excepto la última de un número entero positivo.

    Args:
        numero: El número entero del que se extraerán las cifras.

    Returns:
        Un número entero con todas las cifras excepto la última.
    """

    return numero // 10

def cantidadCifras(numero):
    """Cuenta la cantidad de cifras de un número entero positivo.

    Args:
        numero: El número entero del que se contarán las cifras.

    Returns:
        La cantidad de cifras del número.
    """

    return len(str(numero))

# Ejemplo de uso:
numero = 123456
print("Última cifra:", ultimaCifra(numero))
print("Cifras sin la última:", cifrasSinUltima(numero))
print("Cantidad de cifras:", cantidadCifras(numero))