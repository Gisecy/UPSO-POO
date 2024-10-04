# Nombre y apellido: GISELA CELESTE YEDE

from GiselaYede_clases_ejercicio2 import *

# Códigos de prueba del ejercicio 2

# Creo un reglamento
reglamento1 = Reglamento("lunes", 13)
print(reglamento1.__dict__)

# Creo una fecha
fechaReunion = Fecha("martes", 10)
print(fechaReunion.__dict__)

# Creo una persona y muestro su nombre
persona1 = Persona("Gisela Yede", 12345678)
print("Nombre: ", persona1.getNombre())

# Creo una reunión
reunion1 = Reunion("Reunión semanal", fechaReunion)

# Consulto el reglamento
print("Consula de reglamento: ")
reglamento1.consultarReglamento()

# Solicito habilitación de la reunión
reunion1.solicitarHabilitacion(reglamento1)

# Agrego a persona1 con participante y muestro lista de participantes
reunion1.agregarParticipante(persona1)
print("Lista de participantes: ", reunion1.mostrarListaParticipantes())