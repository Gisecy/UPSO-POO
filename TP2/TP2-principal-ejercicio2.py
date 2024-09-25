# PRUEBAS DE CLASE DE EJERCICIO 2:

from TP2ejercicio2 import *

# Prueba de Clase Libro:

# Creo dos libros y muetro por consola los autores:
libro1 = Libro("Sidney Sheldon", "El amo del juego", "Thriller", 300)
otroLibro = Libro("Deepak Chopra", "Almas gemelas", "Romántica", 280)
print("El autor es: ", libro1.getAutor())
print("El autor es: ", otroLibro.getAutor())

# Muestro el titulo de libro1 por consola, le cambio el titulo al libro
# y lo vuelvo a mostrar:
print("El titulo de libro es: ", libro1.getTitulo())
libro1.setTitulo("Escrito en las estrellas")
print("El nuevo titulo es: ", libro1.getTitulo())

# Clono libro1, lo guardo en libro_clon y muetro por consola el autor de libro_clon:
libro_clon = libro1.clone()
print("El autor del libro clonado es: ", libro_clon.getAutor())

# Muestro por consola si libro es igual a otroLibro
print(f'¿Los siguientes libros son iguales? : {libro1.equals(otroLibro)}')

# Copio otroLibro en libro1:
libro1.copy(otroLibro)

# Muestro los atributos y valores de libro1:
print(libro1.__dict__)