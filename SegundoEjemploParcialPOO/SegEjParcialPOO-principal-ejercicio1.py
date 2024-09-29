# PUEBAS DEL SEGUNDO EJEMPLO PARCIAL DE POO (EJERCICIO1)

from SegEjParcialPOOejercicio1 import *

# Creo un informe1 con código de seguridad y muestro el detalle con el código validado
informe1 = Informe("Ejercicio 1 de POO", "Gisela Yede", "Me está costando un poco realizar los ejercicios.", False, 1234)
informe1.mostrarDetalle(1234)
print("")

# Agrego contenido al informe1 y muetro el contenido con el código validado
informe1.agregarContenido("Si sigo practicando los voy a poder resolver.")
print("Con el contenido agregado: ")
informe1.mostrarDetalle(1234)
print("")

# Elimino el una frase del contenido y lo muestro con codigo validado
informe1.eliminarContenido("Me está costando un poco realizar los ejercicios.")
print("Con el contenido borrado: ")
informe1.mostrarDetalle(1234)
print("")

# Como el informe no tiene código de seguridad y no etá confirmado solo muestra el título y el autor.
informe1.mostrarDetalle(0)

# Confirmo el informe1
informe1.confirmarInforme()

# Agrego contenido a informe1 pero como está confirmado no se puede modificar
informe1.agregarContenido("Nueva información")  # Esto no va a hacer nada, porque el informe está confirmado
print("")

informe2 = Informe("Parcial de POO", "Gisela", "Sigo practicando para el parcical de POO.", False, 4321)
print("Informe2: ")
print("Detalle sin código de seguridad:")
informe2.mostrarDetalle(0)  # Como no tiene código de seguridad, muestra solo titulo y autor
print("")
print("Detalle con código de seguridad:")
informe2.mostrarDetalle(4321)