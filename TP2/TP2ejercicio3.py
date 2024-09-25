'''Ejercicio 3
Realizar una implementación de la clase Encomienda, que contenga información
de su remitente, destinatario, peso, dimensiones y costo. Incluir todos los
comandos de consulta y modificación de atributos. Dibujar el diagrama de
clases correspondiente.
Incorporar los atributos y métodos que se consideren necesarios para modelar
el estado del envío (ej. despachado, en viaje, visita a domicilio, recibido,
rechazado, etc)'''

class Encomienda:

    estadoDelEnvio = ["rechazado", "despachado", "en viaje", "visita a domicilio", "recibido"]

    def __init__(self, remitente, destinatario, peso, dimensiones, costo, motivoRechazo):
        self._remitente = remitente
        self._destinatario = destinatario
        self._peso = peso
        self._dimensiones = dimensiones
        self._costo = costo
        self._estado = 0
        self._motivoRechazo = motivoRechazo


    # Getters
    def getRemitente(self):
        return self._remitente

    def getDestinatario(self):
        return self._destinatario

    def getPeso(self):
        return self._peso

    def getDimensiones(self):
        return self._dimensiones

    def getCosto(self):
        return self._costo

    def getEstado(self):
        return self._estado


    # Setters
    def setRemitente(self, nuevoRemitente):
        self._remitente = nuevoRemitente

    def setDestinatario(self, nuevoDestinatario):
        self._destinatario = nuevoDestinatario

    def setPeso(self, nuevoPeso):
        self._peso = nuevoPeso

    def setDimensiones(self, nuevasDimensiones):
        self._dimensiones = nuevasDimensiones

    def setCosto(self, nuevoCosto):
        self._costo = nuevoCosto


    # Métodos operacionales
    def estadoDeEnvioEncomienda(self):
        return self.estadoDelEnvio[self._estado]

    def cambiarEstado(self):
        if (self._estado < len(self.estadoDelEnvio) - 1):
            self._estado += 1

    def rechazarEncomienda(self,motivoRechazo):
        self._estado = 0
        self._motivoRechazo = motivoRechazo

    def verMotivoDeRechazo(self):
        if self._estado == 0:
            return self._motivoRechazo









