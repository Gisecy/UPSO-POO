# EJERCICIO 11:

"""
Considerar que se tiene una lista1 = [7, 4, 5, 3], indicar el resultado de realizar
las siguientes operaciones en forma consecutiva (es decir, la instrucción del
inciso ii se aplica sobre el resultado del inciso i y así sucesivamente).

i) lista1.append(6)
ii) lista1[2] = 10
iii) lista1.insert(3, 8)
iv) lista1.remove(4)
v) lista1.pop(2)
vi) lista1.extend([1, 2])
vii) lista1.reverse()
viii) lista1.sort()
ix) lista1.reverse()
x) lista1.clear()
xi) lista1.pop()
"""

# Lista inicial
lista1 = [7, 4, 5, 3]

# i) Agrego el valor 6 al final de la lista
lista1.append(6)
print("Después de append(6):", lista1)

# ii) Cambio el tercer elemento (índice 2) por 10
lista1[2] = 10
print("Después de lista1[2] = 10:", lista1)

# iii) Inserto el valor 8 en la posición 3
lista1.insert(3, 8)
print("Después de insert(3, 8):", lista1)

# iv) Elimino la primera aparición del valor 4
lista1.remove(4)
print("Después de remove(4):", lista1)

# v) Elimino el elemento en la posición 2
elemento_eliminado = lista1.pop(2)
print("Después de pop(2):", lista1)
print("Elemento eliminado:", elemento_eliminado)

# vi) Extiendo la lista con los elementos [1, 2]
lista1.extend([1, 2])
print("Después de extend([1, 2]):", lista1)

# vii) Invierto la lista
lista1.reverse()
print("Después de reverse():", lista1)

# viii) Ordeno la lista de menor a mayor
lista1.sort()
print("Después de sort():", lista1)

# ix) Invierto la lista nuevamente
lista1.reverse()
print("Después de reverse() nuevamente:", lista1)

# x) Elimino todos los elementos de la lista
lista1.clear()
print("Después de clear():", lista1)

# xi) lista1.pop(): Intento eliminar un elemento de una lista vacía (generará un IndexError)
try:
    lista1.pop()
except IndexError as e:
    print("Error:", e)