# Nombre y apellido: GISELA CELESTE YEDE

class CuentaUsuario():
    def __init__(self, nombre, email, contrasenia):
        self._nombre = nombre
        self._email = email
        self._contrasenia = contrasenia
        self._estadoSesion = False
        self._registroOp = []

    # Getters
    def getNombre(self):
        return self._nombre

    def getEmail(self):
        return self._email

    def getContrasenia(self):
        return self._contrasenia

    def getEstadoSesion(self):
        return self._estadoSesion

    def getRegistroOp(self):
        return self._registroOp


    #Setters
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def setEmail(self, nuevoEmail):
        self._email = nuevoEmail

    def setEstadoSesion(self, nuevoEstado):
        self._estadoSesion = nuevoEstado

    # Metodos Operacionales
    def cambiarContrasenia(self, contraseniaActual, nuevaContrasenia):
        #permite actualizar la contraseña, para lo cual se requiere ingresar la contraseña actual
        #y comprobar si es correcta.
        if self._estadoSesion == True:
            if contraseniaActual == self._contrasenia:
                self._contrasenia = nuevaContrasenia
                self._registroOp.append("Cambio de contraseña")
            else:
                print("Contraseña actual incorrecta.")
                self._registroOp.append("No se pudo cambiar la contraseña.")

    def consultarDatos(self):
        #retorna un diccionario con el nombre de usuario y el correo electrónico del usuario.No debe
        #retornar la contraseña.
        if self._estadoSesion == True:
            self._registroOp.append("Se consulto los datos.")
            return {"Nombre Usuario": self._nombre, "Email": self._email}
        else:
            self._registroOp.append("No se pudieron consultar los datos.")

    def mostrarRegistroOperaciones(self):
        if self._estadoSesion == True:
            if len(self._registroOp) > 0:
                for registro in self._registroOp:
                    print("Registro: ", registro)

    def enviarMensaje(self, emailDestino, mensaje):
        #simula la operación de enviar un mensaje a una cuenta de correo
        #electrónico.No es posible enviar un mensaje si la dirección de correo del usuario es inválida.
        if self._estadoSesion == True:
            if '@' in self._email:
                if '@' in emailDestino:
                    self._registroOp.append(f"Mensaje enviado a {emailDestino}: {mensaje}")
                    print("Mensaje enviado correctamente.")
                else:
                    print(f"La dirección de correo {emailDestino} es inválida.")
                    self._registroOp.append("No se pudo enviar mensaje.")
            else:
                print("No se puede enviar mensajes con un email inválido. Verifica tu email.")
                self._registroOp.append("No se pudo enviar mensaje.")

    def iniciarSesion(self, email, contrasenia):
        # Si el email no contiene el símbolo ‘@’, se permite crear la instancia pero se considera
        # inválido y no es posible realizar operaciones que requieran su uso.

        if email == self._email:
            if contrasenia == self._contrasenia:
                self._estadoSesion = True
                self._registroOp.append("Inicio de sesión")
                print("Inicio de sesión exitoso.")
            else:
                print("Contraseña incorrecta.")
                self._registroOp.append("inicio de sesión incorrecto.")
        else:
            print("Nombre de usuario incorrecto.")
            self._registroOp.append("inicio de sesión incorrecto.")

    def cerrarSesion(self):
        #debe permitir el cierre de sesión del usuario.Incluir los parámetros que se consideren
        #necesarios.

        if self._estadoSesion == True:
            self.estadoSesion = False
            self._registroOp.append("Cierre de sesión")
            print("Cierre de sesión exitoso.")
        else:
            print("No hay ninguna sesión iniciada.")
            self._registroOp.append("Cierre de sesión incorrecto.")




