# EJERCICIO 5:

"""
Implementar un programa que permita generar cuatro números aleatorios y
calcule el promedio."""

import random

listaAleatorios = []
for i in range (4):
    numero = random.randint(1, 100)
    listaAleatorios.append(numero)

print("Los números aleatorios son:", listaAleatorios)

promedio = sum(listaAleatorios) / len(listaAleatorios)

print("El promedio es:", promedio)
