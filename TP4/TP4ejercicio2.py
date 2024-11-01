'''Implementar una clase Vector, que permita almacenar una
representación de vectores en dos dimensiones (x,y).
Incorporar los métodos necesarios para que sea posible
ejecutar las siguientessentencias:

a) v1 = Vector(2, 3)
b) v2 = Vector(1, 4)
c) print(v1) # resultado esperado: imprime ‘ Vector = ( x : 2, y : 3) ‘
d) v3 = v1 + v2 # resultado esperado: v3 = Vector(3,7)
e) v4 = 5*v1 # resultado esperado: v4 = Vector(10, 15)
f) v5 = v1.invertir()# resultado esperado: v5 = Vector(-2, -3)
g) for i in v2:
print (i) # resultado esperado: imprime 1, luego imprime 4
h) v6 = v2 - v1 # resultado esperado: v6 = Vector(-1,1)
i) v7 = len(v2) # resultado esperado: 2 (cantidad de dimensiones del v2, es decir, x e y)
j) v8 = v1 + 4 # resultado esperado: Vector(6,7)
k) v9 = 9 + v1 # resultado esperado: Vector(11, 12)'''

class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Getters:
    def getX(self):
        return self._x

    def getY(self):
        return self._y

    # Setters:
    def setX(self, nuevoX):
        self._x = nuevoX

    def setY(self, nuevoY):
        self._y = nuevoY

    # Métodos Operacionales:
    def invertir(self):
        return Vector(-1 * self._x, -1 * self._y)

    # Metodos mágicos:
    def __str__(self):
        return f'Vector = ({self.getX()}, {self.getY()})'

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._x + other.getX(), self._y + other.getY())
        else:
            if isinstance(other, int):
                return Vector(self._x + other, self._y + other)

    def __rmul__(self, other):
        if isinstance(other, int):
            return Vector(self._x * other, self._y * other)


    def __iter__(self):
        self._ind = 0
        self._coord = (self._x, self._y)
        return self

    def __next__(self):
        if self._ind < len(self._coord):
            self._ind += 1
            return self._coord[self._ind - 1]
        raise StopIteration

    '''def __iter__(self):       # Esta forma es igual que utilizar __iter__ y __next__ para iterar??
        yield self._x
        yield self._y  '''

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._x - other.getX(), self._y - other.getY())

    def __len__(self):
        v = [self._x, self._y]  # Hay alguna otra forma de realizarlo??
        return len(v)

    def __radd__(self, other):
        if isinstance(other, int):
            return Vector(self._x + other, self._y + other)
