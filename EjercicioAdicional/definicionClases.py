class Equipo():
    def __init__(self,nombreEquipo):
        self._nombreEquipo = nombreEquipo
        self._listaDeJugadores = []

    # Getters
    def getNombreEquipo(self):
        return self._nombreEquipo

    def getListaDeJugadores(self):
        return self._listaDeJugadores

    # Setters
    def setNombreEquipo(self, nuevoNombreEquipo):
        self._nombreEquipo = nuevoNombreEquipo

    def setListaDeJugadores(self, nuevaListaDeJugadores):
        self._listaDeJugadores = nuevaListaDeJugadores


class Gol():
    def __init__(self, nombreEquipo, minuto):
        self._nombreEquipo = nombreEquipo
        self._minuto = minuto

    # Getters
    def getNombreEquipo(self):
        return self._nombreEquipo

    def getMinuto(self):
        return self._minuto

    # Setters
    def setNombreEquipo(self, nuevoNombreEquipo):
        self._nombreEquipo = nuevoNombreEquipo

    def setMinuto(self, nuevoMinuto):
        self._minuto = nuevoMinuto


class Clima():
    def __init__(self, buenClima):
        self._buenClima = buenClima

    # Getter
    def getBuenClima(self):
        return self._buenClima

    # Setter
    def setBuenClima(self, nuevoClima):
        self._buenClima = nuevoClima


class PartidoDeFutbol():
    def __init__(self,equipo1, equipo2):
        self._losEquipos = (equipo1, equipo2)
        self._losGoles = []
        self._sePuedeJugar = False # a priori no hasta que no verifiquemos


    # Getters
    def getLosEquipos(self):
        return self._losEquipos

    def getLosGoles(self):
        return self._losGoles

    def getSePuedeJugar(self):
        return self._sePuedeJugar

    # Setters
    def setLosEquipos(self, nuevosEquipos):
        self._losEquipos = nuevosEquipos

    def setLosGoles(self, nuevoGoles):
        self._losGoles = nuevoGoles

    def setSePuedeJugar(self, nuevoEstado):
        self._sePuedeJugar = nuevoEstado


    # metodos operacionales para el partido ======================== ( IMPLEMENTAR )

    # Dependencia:
    def comprobarSiSePuedeJugar(self,clima):
        # esto debe cambiar el estado del atributo self._sePuedeJuar dependiendo el estado del clima
        if isinstance(clima, Clima):
            if clima.getBuenClima():
                self._sePuedeJugar = True

    # Composicion: Se instancian los objetos dentro de la clase./ Dejan de existir cuando se destruye la clase.
    def nuevoGol(self,nombreEquipo, minuto):
        # este metodo debe agregar un gol a la lista de goles del partido
        unGol = Gol(nombreEquipo, minuto)
        self._losGoles.append(unGol)

    def ganador(self):
        # debe retornarme el ganador del equipo,
        # considerar que los goles estan bien cargados en la lista de goles
        # no se deben considerar el empate, en estos partidos siempre existe un ganador
        golesEquipo1 = 0
        golesEquipo2 = 0
        for gol in self.getLosGoles():
            if gol.getNombreEquipo() == self.getLosEquipos()[0].getNombreEquipo():
                golesEquipo1 += 1
            else:
                golesEquipo2 += 1

        # Determinar el ganador
        if golesEquipo1 > golesEquipo2:
            return self._losEquipos[0]
        else:
            return self._losEquipos[1]