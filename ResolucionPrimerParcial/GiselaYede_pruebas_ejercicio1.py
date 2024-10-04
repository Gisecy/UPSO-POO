# Nombre y apellido: GISELA CELESTE YEDE

from GiselaYede_clases_ejercicio1 import *

# Códigos de prueba del ejercicio 1

# Creo una nueva cuenta de usuario (usuario1
usuario1 = CuentaUsuario("Gisela Yede", "gisecy@gmail.com", 1234)

# Obtengo el nombre de usuario
print("Nombre de usuario: ",usuario1.getNombre())

# Muestro el estado de la sesión, inicio sesión y vuelvo a mostrar el estado
print("Estado sesion: ", usuario1.getEstadoSesion())
usuario1.iniciarSesion("gisecy@gmail.com", 1234)
print("Estado sesion: ", usuario1.getEstadoSesion())

# Envio un mensaje con el mail bien escrito
usuario1.enviarMensaje("giselacyede@gmail.com", "Hola mundo!")

# Envio un mensaje con el mail mal escrito
usuario1.enviarMensaje("giselacyedegmail.com", "Hola mundo!")

# Consulto los datos del usuario
datos_usuario = usuario1.consultarDatos()
print(datos_usuario)

# Muestro el registro de operaciones
print("Registro de operaciones: ")
usuario1.mostrarRegistroOperaciones()

# Cambio el email
usuario1.setEmail("giselacyede@gmail.com")

# Cambio la contraseña
usuario1.cambiarContrasenia(1234, 4321)
print("Contraseña nueva: ", usuario1.getContrasenia())

# Cierro sesion de usuario1
usuario1.cerrarSesion()

# Muestro el estado de sesión luego de cerrarla
print("Estado sesion: ", usuario1.getEstadoSesion())