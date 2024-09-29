# PRUEBAS DE EJEMPLO PARCIAL DE POO (EJERCICIO2)

from SegEjParcialPOOejercicio2 import *

# Creo un guion
guion1 = Guion("Quentin Tarantino", "Acción")
print(f'El escritor de guion1 es: {guion1.getEscritor()} y el genero es: {guion1.getGenero()}')
print("")

# Creo actores
actor1 = Actor("Leonardo DiCaprio", 48, "Estadounidense")
actor2 = Actor("Brad Pitt", 59, "Estadounidense")
print(f'El actor1 es {actor1.getNombre()}, tiene {actor1.getEdad()} años y es de nacionalidad {actor1. getNacionalidad()}')
print("")

# Creo director1
director1 = Director("Quentin Tarantino")

# Creo una película
pelicula1 = Pelicula("Once Upon a Time in Hollywood", guion1, [director1])
pelicula1.agregarActor(actor1)
pelicula1.agregarActor(actor2)
print("El nombre de la peicula es: ",pelicula1.getNombre())
print("")

# Imprimo el detalle del guion de la película1
pelicula1.detallarGuion()
print("")

# Muestro los actores de la película1
pelicula1.mostrarActores()
print("")

# Buesco el actor más joven y lo muestro
actorMasJoven = pelicula1.actorMasJoven()
print(f"El actor más joven es: {actorMasJoven.getNombre()}")
print("")

# Creo y grego otro director y muestro los directores de pelicula1
director2 = Director("Martin Scorsese")
pelicula1._directores.append(director2)  # Agregar un director adicional
print("Directores de pelicula1")
pelicula1.mostrarDirectores()
print("")

# Quito actor2 de la lista y muestro
pelicula1.quitarActor(actor2)
pelicula1.mostrarActores()