#PRUEBAS DE EJERCICIO 3:

from TP4ejercicio3 import *

# a)
s1 = Sobre(10, 20)
print(s1)

# b)
s2 = Sobre(8, 15)
print(s2)

# c)
a = s2 < s1 # resultado esperado: True, ya que el área de s2 es menor al área de s1
print(a)

# d)
b = s1 in s2 # resultado esperado: False, ya que s1 no podría colocarse dentro de s2
print(b)

# e)
s3 = s1 / 2 # resultado esperado: [Sobre(10,10), Sobre(10,10)], ya que recorta s1 en dos
            #sobres más chicos, respetando el ancho
print(s3)