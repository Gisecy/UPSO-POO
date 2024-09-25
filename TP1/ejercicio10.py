# EJERCICIO 10:

"""
a) Crear una lista que contenga valores enteros desde 3 a 12 incluidos.
Utilizar el identificador listaNumeros.

b) Indicar el resultado de las siguientes operaciones realizadas sobre la lista del
inciso anterior:

i) x = len(listaNumeros)
ii) x = listaNumeros[3]
iii) x = listaNumeros[:3]
iv) x = listaNumeros[3:]
v) x = listaNumeros[3:6]
vi) x = listaNumeros[1:8:2]
vii) x = listaNumeros[-1]
viii) x = listaNumeros[-6:-2]
ix) x = listaNumeros[ : : -1]
"""

# a) Creo la lista de números
listaNumeros = list(range(3, 13))
print("Lista original:", listaNumeros)


# b) Operaciones sobre la lista

# i) Obtengo la longitud de la lista
x = len(listaNumeros)
print("Longitud de la lista:", x)

# ii) Obtengo el cuarto elemento (índice 3)
x = listaNumeros[3]
print("Cuarto elemento:", x)

# iii) Obtengo los primeros tres elementos
x = listaNumeros[:3]
print("Primeros tres elementos:", x)

# iv) Obtengo los elementos desde el cuarto hasta el final
x = listaNumeros[3:]
print("Elementos desde el cuarto hasta el final:", x)

# v) Obtengo los elementos desde el cuarto hasta el sexto (excluyendo el séptimo)
x = listaNumeros[3:6]
print("Elementos del cuarto al sexto:", x)

# vi) Obtengo los elementos desde el segundo hasta el octavo (excluyendo el octavo), de dos en dos
x = listaNumeros[1:8:2]
print("Elementos del segundo al octavo, de dos en dos:", x)

# vii) Obtengo el último elemento
x = listaNumeros[-1]
print("Último elemento:", x)

# viii) Obtengo los elementos desde el sexto hasta el segundo (excluyendo el segundo), en orden inverso
x = listaNumeros[-6:-2]
print("Elementos del sexto al segundo (inverso):", x)

# ix) Invertir la lista completa
x = listaNumeros[::-1]
print("Lista invertida:", x)