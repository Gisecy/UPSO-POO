'''Ejercicio 1
Implementar una clase A, que contenga un constructor para asignar
el valor de un atributo _a1, y un método calcularCuadrado que calcule
y retorne el cuadrado de _a1. Luego incorporar los siguientes requisitos:
a) Crear una clase B por herencia de A, que contenga un constructor
para asignar el valor de _a1 y un segundo parámetro _b1.
b) Sobreescribir el método calcularCuadrado, de forma que calcule y
retorne el cuadrado de _b1.
c) Crear una clase C por herencia de B, que contenga un constructor
para asignar valores de _a1 y _b1.
d) Agregar a C un método sumar, que calcule y retorne la suma de _a1
y _b1.
Nota: con esta jerarquía, la clase A es la clase padre de B, mientras
que C es clase hija de B'''

class A:

    def __init__(self, a1):
        self._a1 = a1

    def calcularCuadrado(self):
        return self._a1 ** 2

class B(A):
    def __init__(self, a1, b1):
        super().__init__(a1)  # Llamo al constructor de la clase A.
        self._b1 = b1

    def calcularCuadrado(self):
        return self._b1 ** 2  # Sobreescribo el método de la clase A.

class C(B):
    def __init__(self, a1, b1):
        super().__init__(a1, b1) # Llamo al constructor de la clase B.

    def sumar(self):
        return self._a1 + self._b1

