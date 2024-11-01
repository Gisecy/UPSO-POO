# PRUEBAS DE EJERCICIO 1:

from TP5ejercicio1 import *

# Instancia de la clase A
a = A(2)
print("Resultado del cuadrado en A:", a.calcularCuadrado())

# Instancia de la clase B
b = B(2, 4)
print("Resultado del cuadrado en B:", b.calcularCuadrado())

# Instancia de la clase C
c = C(2, 4)
print("Resultado del cuadrado en C (hereda el cálculo cuadrado de B):", c.calcularCuadrado())

print("Resultado de la suma en C:", c.sumar())
