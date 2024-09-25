class Televisor:

    # Inciso 1:
    def __init__(self, marca, totalCanales, canalActual, volumen, encendido):
        self._marca = marca
        self._totalCanales = totalCanales
        self._canalActual = 1
        self._volumen = 0
        self._encendido = False
        self._canalesVistos = [] # Lista para guardar los canales vistos para la implementación del inciso 6.


    # Inciso 2:
    # Getters
    def getMarca(self):
        return self._marca

    def getTotalCanales(self):
        return self._totalCanales

    def getCanalActual(self):
        return self._canalActual

    def getVolumen(self):
        return self._volumen

    def getEncendido(self):
        return self._encendido

    # Inciso 3:
    # Setters
    def setMarca(self, nuevaMarca):
        self._marca = nuevaMarca

    def setTotalCanales(self, nuevoTotalCanales):
        self._totalCanales = nuevoTotalCanales

    def setCanalActual(self, nuevoCanal):
        self._canalActual = nuevoCanal

    #Inciso 4:
    # Métodos Operacionales
    def canalSiguiente(self):
        if self._encendido:
            if self._canalActual != self._totalCanales:
                self._canalActual += 1
            else:
                self._canalActual = 1
        self._canalesVistos.append(self._canalActual)

    def canalAnterior(self):
        if self._encendido:
            if self._canalActual == 1:
                self._canalActual = self._totalCanales
            else:
                self._canalActual -= 1
        self._canalesVistos.append(self._canalActual)

    def subirVolumen(self):
        if self._encendido:
            if self._volumen < 100:
                self._volumen += 1

    def bajarVolumen(self):
        if self._encendido:
            if self._volumen > 0:
                self._volumen -= 1

    def silenciar(self):
        if self._encendido:
            self._volumen = 0

    def encender(self):
        self._encendido = True

    def apagar(self):
        self._encendido = False

# Inciso 6:
    def canalPrevio(self):
        if self._encendido and len(self._canalesVistos) > 1:
            self._canalesVistos.pop()
            self._canalActual = self._canalesVistos[-1]