# EJERCICIO 8:

"""Implementar un programa que permita al usuario ingresar tres valores:
valorInicial, valorFinal y salto.
En base a esos tres valores, mostrar la lista de todos los números a partir de
valorInicial de salto en salto hasta valorFinal. Resolver el ejercicio utilizando la
estructura de control for y luego la estructura de control while.
Ejemplo: si valorInicial = 10, valorFinal = 30 y salto = 5, se deberán mostrar los números “a partir de
10, de 5 en 5 hasta llegar a 20”, es decir: 10, 15, 20, 25, 30."""

# Generar secuencia con ciclo FOR:

def generarSecuenciaFor(valor_inicial, valor_final, salto):
    """Genera una secuencia de números utilizando un bucle for.

    Args:
        valor_inicial: El primer número de la secuencia.
        valor_final: El último número de la secuencia.
        salto: El incremento entre cada número.

    Returns:
        Una lista con los números de la secuencia.
    """

    secuencia = []
    for numero in range(valor_inicial, valor_final + 1, salto):
        secuencia.append(numero)
    return secuencia

# Obtengo los valores del usuario
valor_inicial = int(input("Ingrese el valor inicial: "))
valor_final = int(input("Ingrese el valor final: "))
salto = int(input("Ingrese el salto: "))

# Genero y muestro la secuencia
secuencia = generarSecuenciaFor(valor_inicial, valor_final, salto)
print(secuencia)

# Generar secuencia con ciclo WHILE:

def generarSecuenciaWhile(valor_inicial, valor_final, salto):
    """Genera una secuencia de números utilizando un bucle while.

    Args:
        valor_inicial: El primer número de la secuencia.
        valor_final: El último número de la secuencia.
        salto: El incremento entre cada número.

    Returns:
        Una lista con los números de la secuencia.
    """

    secuencia = []
    numero = valor_inicial
    while numero <= valor_final:
        secuencia.append(numero)
        numero += salto
    return secuencia

# Obtengo los valores del usuario
valor_inicial = int(input("Ingrese el valor inicial: "))
valor_final = int(input("Ingrese el valor final: "))
salto = int(input("Ingrese el salto: "))

# Genero y muestro la secuencia
secuencia = generarSecuenciaWhile(valor_inicial, valor_final, salto)
print(secuencia)

