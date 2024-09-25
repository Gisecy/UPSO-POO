# PRUEBAS DE CLASE DE EJERCICIO 3:

from TP2ejercicio3 import *

# Pruebas de Clase Encomienda:

# Creo una nueva encomienda
encomienda1 = Encomienda("Juan Pérez", "Pepito Sanchez", 2.5, (20, 30, 40), 10000, "Dirección incorrecta")

# Muestro los datos de la encomienda
print("Remitente:", encomienda1.getRemitente())
print("Estado actual:", encomienda1.estadoDeEnvioEncomienda())
print("Motivo del Rechazo: ", encomienda1.verMotivoDeRechazo())

# Cambio el destinatario y muestro el nuevo destinatario
encomienda1.setDestinatario("Gisela Yede")
print("Nuevo Destinatario: ", encomienda1.getDestinatario())

# Aumento el costo de la encomienda
nuevoCosto = encomienda1.getCosto() + 1000
encomienda1.setCosto(nuevoCosto)
print("Nuevo costo: ", encomienda1.getCosto())

# Rechazar la encomienda
encomienda1.rechazarEncomienda("Destinatario ausente")
print("Motivo de rechazo:", encomienda1.verMotivoDeRechazo())

# Cambio el estado a despachado
encomienda1.cambiarEstado()
print("Nuevo estado:", encomienda1.estadoDeEnvioEncomienda())
