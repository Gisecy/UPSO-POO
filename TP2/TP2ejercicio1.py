'''Ejercicio 1:

Realizar la implementación de las siguientes clases, incluyendo todos los comandos
de consulta y modificación de atributos. Dibujar el diagrama de clases
correspondiente en cada caso.

a) Clase Monitor, que contenga información de su marca, tamaño, tipo de
pantalla (ej, LED, LCD) y tipos de conexión (ej. VGA, HDMI, ambas).

b) Clase Teclado, que contenga información de su marca, lenguaje, si incluye
teclado numérico y si tiene retroiluminación. Incluir todos los comandos de
consulta y modificación de atributos. Dibujar el diagrama de clases correspondiente.'''

class Monitor:
    def __init__(self, marca, tamanio, tipoPantalla, tiposConexion):
        self._marca = marca
        self._tamanio = tamanio
        self._tipoPantalla = tipoPantalla
        self._tiposConexion = tiposConexion


    # Getters
    def getMarca (self):
        return self._marca

    def getTamanio (self):
        return self._tamanio

    def getTipoPantalla (self):
        return self._tipoPantalla

    def getTiposConexion (self):
        return self._tiposConexion

    # Setters
    def setMarca (self, nuevaMarca):
        self._marca = nuevaMarca

    def setTamanio (self,nuevoTamanio):
        self._tamanio = nuevoTamanio

    def setTipoPantalla (self,nuevaPantalla):
        if nuevaPantalla in ['LED', 'LCD']:
            self._tipoPantalla = nuevaPantalla

    def setTiposConexion (self, nuevaConexion):
        if nuevaConexion in ['VGA', 'HDMI', 'AMBAS']:
            self._tiposConexion = nuevaConexion


class Teclado:
    def __init__(self, marca, lenguaje, tecladoNumerico, retroiluminacion):
        self._marca = marca
        self._lenguaje = lenguaje
        self._tecladoNumerico = tecladoNumerico
        self._retroiluminacion = retroiluminacion

    # Getters

    def getMarca(self):
        return self._marca

    def getLenguaje(self):
        return self._lenguaje

    def getTecladoNumerico(self):
        return self._tecladoNumerico

    def getRetroiluminacion(self):
        return self._retroiluminacion

    #Setters

    def setMarca(self, nuevaMarca):
        self._marca = nuevaMarca

    def setLenguaje(self, nuevoLenguaje):
        self._lenguaje = nuevoLenguaje

    def setTecladoNUmerico(self, nuevoTeclado):
            self._tecladoNumerico = nuevoTeclado

    def setRetroiluminacion(self, nuevoRetroiluminacion):
            self._retroiluminacion = nuevoRetroiluminacion



