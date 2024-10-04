# Nombre y apellido: COMPLETAR ACA

class CuentaUsuario():
    def __init__(self, nombreUsuario, email, contrasenia):
        self._nombreUsuario = nombreUsuario
        self._email = email
        self._contrasenia = contrasenia
        self._estadoSesion = False
        self._registroOperaciones = []

    def setNombreUsuario(self,nuevo):
        self._nombreUsuario = nuevo

    def getNombreUsuario(self):
        return self._nombreUsuario

    def setEmail(self, nuevo):
        self._email = nuevo

    def getEmail(self):
        return self._email

    def setContrasenia(self, nuevo):
        self._contrasenia = nuevo

    def getContrasenia(self):
        return self._contrasenia

    def setEstadoSesion(self, nuevo):
        self._estadoSesion = nuevo

    def getEstadoSesion(self):
        return self._estadoSesion

    def setRegistroOperaciones(self, nuevo):
        self._registroOperaciones = nuevo

    def getRegistroOperaciones(self):
        return self._registroOperaciones

    #===========================================================
    def cambiarContrasenia(self,contraseniaActual,nuevaContrasenia):
        if contraseniaActual == self.getContrasenia():
            self.setContrasenia(nuevaContrasenia)
            self._registroOperaciones.append('se cambio la contrasenia')
        self._registroOperaciones.append('no se cambio la contrasenia')

    def consultarDatos(self):
        self._registroOperaciones.append('se consulto los datos')
        return {'nombre':self.getNombreUsuario(),'email':self.getEmail()}

    def mostrarRegistroOperaciones(self):
        self._registroOperaciones.append('se mostro el registro de operaciones')
        for operacion in self.getRegistroOperaciones():
            print(operacion)

    def enviarMensaje(self,emailDestino, mensaje):
        if ('@' in self.getEmail()) and ('@' in emailDestino) and self.getEstadoSesion():
            print('enviando mensaje')
            self._registroOperaciones.append('se envio un mensaje')
        else:
            self._registroOperaciones.append('no se envio un mensaje')

    def inicioSesion(self,contrasenia, email):
        if (contrasenia == self.getContrasenia()) and (email == self.getEmail()):
            self.setEstadoSesion(True)
            self._registroOperaciones.append('se inicio sesion')
        else:
            self._registroOperaciones.append('inicio de sesion fallida')

    def cierreSesion(self):
        if self.getEstadoSesion():
            self.setEstadoSesion(False)
            self._registroOperaciones.append('se cerro la sesion')
        else:
            self._registroOperaciones.append('comando invalido')

    def borrarOperacionesRealizadas(self):
        self.getRegistroOperaciones().clear()
        self._registroOperaciones.append('se borro la lista de operaciones')


