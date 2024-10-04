 # Nombre y apellido: GISELA CELESTE YEDE

class Fecha():
    def __init__(self, dia, hora):
        self._dia = dia
        self._hora = hora

    #Getters
    def getDia(self):
        return self._dia

    def getHora(self):
        return self._hora

    #Setters
    def setDia(self, nuevoDia):
        self._dia = nuevoDia

    def setHora(self, nuevaHora):
        self._hora = nuevaHora

class Persona():
    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni

    # Getters
    def getNombre(self):
        return self._nombre

    def getDni(self):
        return self._dni

    # Setters
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def set(self, nuevoDni):
        self._dni = nuevoDni

    # Metodo operacional
    def mostrarInformacion(self):
        print(f'Nombre: {self._nombre} DNI: {self._dni}')

class Reglamento():
    def __init__(self,diaNoPermitido, horaNoPermitida):
        self._diaNoPermitido = diaNoPermitido
        self._horaNoPermitida = horaNoPermitida

    # Metodos Operacionales
    def habilitarReunion(self, dia, hora):
        if dia != self._diaNoPermitido and hora != self._horaNoPermitida:
            return True
        else:
            return False

    def consultarReglamento(self):
        print(f'No se permiten reuniones los dias {self._diaNoPermitido}, ni reuniones que comiencen a las {self._horaNoPermitida}')


class Reunion():
    def __init__(self, nombre, fecha):
        self._nombre = nombre
        self._fecha = fecha
        self._habilitada = False
        self._listaParticipantes = []

    # Getters
    def getNombre(self):
        return self._nombre

    def getFecha(self):
        return f"Día: {self._fecha.getDia()}, Hora: {self._fecha.getHora()}"

    # Setters
    def setNombre(self, NuevoNombre):
        self._nombre = NuevoNombre

    def setFecha(self, NuevaFecha):
        self._fecha = NuevaFecha

    def setDia(self, nuevoDia):
        self._dia = nuevoDia

    def setHora(self, nuevaHora):
            self.fecha = nuevaHora

    def solicitarHabilitacion(self, reglamento):
        if isinstance(reglamento, Reglamento):
            dia = self._fecha.getDia()
            hora = self._fecha.getHora()
            self._habilitada = reglamento.habilitarReunion(dia, hora)

    def reunionHabilitada(self):
        return self._habilitada

    def agregarParticipante(self, persona):
        if isinstance(persona, Persona):
            esta = False
            for p in self._listaParticipantes:
                if p.getDni() == persona.getDni():
                    esta = True
                if not esta:
                    self._listaParticipantes.append(persona)

    def mostrarListaParticipantes(self):
        for participante in self._listaParticipantes:
            print(participante.mostrarInformacion())
