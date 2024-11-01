'''Ejercicio 3
Implementar la clase Sobre, que permita modelar un sobre de papel con sus dimensiones
de ancho y alto. Incorporar los métodos necesarios para que sea posible ejecutar las
siguientes sentencias:
a) s1 = Sobre(10, 20)
b) s2 = Sobre(8, 15)
c) a = s2 < s1 # resultado esperado: True, ya que el área de s2 es menor al área de s1
d) b = s1 in s2 # resultado esperado: False, ya que s1 no podría colocarse dentro de s2
e) s3 = s1 / 2 # resultado esperado: [Sobre(10,10), Sobre(10,10)], ya que recorta s1 en dos
sobres más chicos, respetando el ancho.'''

class Sobre:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    # Getters:
    def getAncho(self):
        return self._ancho

    def getAlto(self):
        return self._alto

    # Setters:
    def setAncho(self, nuevo):
        self._ancho = nuevo

    def setAlto(self, nuevo):
        self._alto = nuevo

    # Metodo operacional:
    def area(self):
        return self.getAncho() * self.getAlto()

    # Metodos mágicos:
    def __str__(self):
        return f'Sobre = ({self._ancho}, {self._alto})'

    def __lt__(self, other):
        if isinstance(other, Sobre):
            if self.area() < other.area():
                return True
            else:
                return False

    def __contains__(self, other):
        if isinstance(other, Sobre):
            if self._ancho >= other.getAncho() and self._alto >= other.getAlto():
                return True
            else:
                return False

    def __truediv__(self, divisor):
        if isinstance(divisor, int):
            nuevoAlto = self._alto / divisor
            return [Sobre(self._ancho, nuevoAlto), Sobre(self._ancho, nuevoAlto)]

    def __repr__(self):
        return f"Sobre({self.getAncho()}, {self.getAlto()})"
