# EJERCICIO 9:

"""Implementar un programa que permita ingresar valores enteros positivos. El ingreso
termina cuando el usuario no desee ingresar más valores, para lo cual se deberá
definir un criterio que indique esta decisión. Luego deberá calcular y mostrar el
promedio, la cantidad de valores ingresados, el mayor y menor valor."""

def calcular():
    """Calcula el promedio, cantidad, máximo y mínimo de una serie de números ingresados
     por el usuario.

    El usuario indica el final de la entrada ingresando un número negativo.
    """

    numeros = []
    while True:
        numero = int(input("Ingrese un número entero positivo (o un número negativo para finalizar): "))
        if numero < 0:
            break
        numeros.append(numero)

    # Calcular
    cantidad = len(numeros)
    promedio = sum(numeros) / cantidad if cantidad > 0 else 0
    maximo = max(numeros) if numeros else None
    minimo = min(numeros) if numeros else None

    # Muestro los resultados
    print(f"Cantidad de números: {cantidad}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Valor máximo: {maximo}")
    print(f"Valor mínimo: {minimo}")


calcular()