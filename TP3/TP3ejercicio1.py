'''Ejercicio 1
En el ejercicio 1 del TP2 se realizó la implementación de las clases
Monitor y Teclado. Retomar el ejercicio creando ahora la clase
Computadora, con los atributos que se consideren apropiados, ymodelar
la relación que puede generarse entre las tres clases. Completar
el diagrama UML con la simbología correspondiente y crear un archivo
de pruebas para las funcionalidades implementadas'''

class Computadora:
    def __init__(self, marca, modelo, procesador, memoriaRam, almacenamiento, sistemaOperativo, monitor, teclado):
        self._marca = marca
        self._modelo = modelo
        self._procesador = procesador
        self._memoriaRam = memoriaRam
        self._almacenamiento = almacenamiento
        self._sistemaOperativo = sistemaOperativo
        self._monitor = monitor
        self._teclado = teclado


    # Getters
    def getMarca(self):
        return self._marca

    def getModelo(self):
        return self._modelo

    def getProcesador(self):
        return self._procesador

    def getMemoriaRam(self):
        return self._memoriaRam

    def getAlmacenamiento(self):
        return self._almacenamiento

    def getSistemaOperativo(self):
        return self._sistemaOperativo


    # Setters
    def setMarca(self, nuevaMarca):
        self._marca = nuevaMarca

    def setModelo(self, nuevoModelo):
        self._modelo = nuevoModelo

    def setProcesador(self, nuevoProcesador):
        self._procesador = nuevoProcesador

    def setMemoriaRam(self, nuevaMemoRam):
        self._memoriaRam = nuevaMemoRam

    def setAlmacenamiento(self,nuevoAlmacenamiento):
        self._almacenamiento = nuevoAlmacenamiento

    def setSistemaOperativo(self, nuevoSO):
        self._sistemaOperativo = nuevoSO

    # Metodos operacionales

    def obtenerTamanioMonitor(self):
        if self._monitor is None:
            return None
        return self._monitor.getTamanio()

    def obtenerMarcaTeclado(self):
        if self._teclado is None:
            return None
        return self._teclado.getMarca()

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





