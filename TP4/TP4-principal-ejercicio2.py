# PRUEBAS DE EJERCICIO 2:

from TP4ejercicio2 import *

# a)-
v1 = Vector(2, 3)

# b)-
v2 = Vector(1, 4)

# c)-
print(v1) # resultado esperado: imprime ‘ Vector = ( x : 2, y : 3) ‘

# d)-
v3 = v1 + v2 # resultado esperado: v3 = Vector(3,7)
print(v3)

# e)-
v4 = 5*v1 # resultado esperado: v4 = Vector(10, 15)
print(v4)

# f)-
v5 = v1.invertir()# resultado esperado: v5 = Vector(-2, -3)
print(v5)

# g)-
for i in v2:
    print (i) # resultado esperado: imprime 1, luego imprime 4

# h)-
v6 = v2 - v1 # resultado esperado: v6 = Vector(-1,1)
print(v6)

# i)-
v7 = len(v2) # resultado esperado: 2 (cantidad de dimensiones del v2, es decir, x e y)
print(v7)

# j)-
v8 = v1 + 4 # resultado esperado: Vector(6,7)
print(v8)

# k)-
v9 = 9 + v1 # resultado esperado: Vector(11, 12)
print(v9)

