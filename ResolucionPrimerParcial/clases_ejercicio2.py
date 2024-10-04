# Nombre y apellido: COMPLETAR ACA

class Fecha():
    def __init__(self, dia, hora):
        self._dia = dia
        self._hora = hora

    def setDia(self,nuevo):
        self._dia = nuevo

    def getDia(self):
        return self._dia

    def setHora(self, nuevo):
        self._hora = nuevo

    def getHora(self):
        return self._hora

class Persona():
    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni

    def setNombre(self, nuevo):
        self._nombre = nuevo

    def getNombre(self):
        return self._nombre

    def setDni(self, nuevo):
        self._dni = nuevo

    def getDni(self):
        return self._dni

    def mostrarInformacion(self):
        return f'el nombre es {self.getNombre()} con dni {self.getDni()}'

class Reglamento():
    def __init__(self, diaNoPermitido, horaNoPermitida):
        self._diaNoPermitido = diaNoPermitido
        self._horaNoPermitida = horaNoPermitida

    def habilitarReunion(self, dia, hora):
        if (dia != self._diaNoPermitido) and (hora != self._horaNoPermitida):
            return True
        return False

    def consultarReglamento(self):
        print(f'No se permiten reuniones los días {self._diaNoPermitido}, ni reuniones que comiencen a las {self._horaNoPermitida} horas"')

class Reunion():
    def __init__(self, nombre, fecha):
        self._nombre = nombre
        self._fecha = fecha
        self._habilitada = False
        self._listaParticipantes = []

    def getNombre(self):
        return self._nombre

    def getFecha(self):
        return f"Día: {self._fecha.getDia()}, Hora: {self._fecha.getHora()}"

    def setNombre(self, nuevo):
        self._nombre = nuevo

    def setDia(self, dia):
        self._fecha.setDia(dia)

    def setHora(self, hora):
        self._fecha.setHora(hora)

    #====================================
    def solicitarReglamento(self, reglamento):
        if isinstance(reglamento,Reglamento) and reglamento.habilitarReunion(self._fecha.getDia(),self._fecha.getHora()):
            self._habilitada = True

    def reunionHabilitada(self):
        return self._habilitada

    def agregarParticipante(self, persona):
        if isinstance(persona,Persona):
            esteDni = persona.getDni()
            esta = False
            for unaPersona in self._listaParticipantes:
                if unaPersona.getDni() == esteDni:
                    esta = True
            if not esta:
                self._listaParticipantes.append(persona)

    def mostrarListaPraticipantes(self):
        for persona in self._listaParticipantes:
            print(persona.mostrarInformacion())