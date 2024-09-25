'''Ejercicio 2:
a) Una clase Cliente y una clase Comercio, considerando que un comercio tiene
0 o más clientes.
Definir al menos tres atributos en cada clase e implementar el modelo elegido.
Crear un archivo de pruebas para las funcionalidades implementadas.'''

class Cliente:
    def __init__(self, nombre, dni, direccion, telefono):
        self._nombre = nombre
        self._dni = dni
        self._direccion = direccion
        self._telefono = telefono


    #Getters
    def getNombre(self):
        return self._nombre

    def getDni(self):
        return self._dni

    def getDireccion(self):
        return self._direccion

    def getTelefono(self):
        return self._telefono


    #Setters
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def setDni(self, nuevoDni):
        self._dni = nuevoDni

    def setDireccion(self, nuevaDireccion):
        self._direccion = nuevaDireccion

    def setTelefono(self, nuevoTelefono):
        self._telefono = nuevoTelefono



class Comercio:
    def __init__(self, nombre, direccion, rubro):
        self._nombre = nombre
        self._direccion = direccion
        self._rubro = rubro
        self._clientes = []  # Lista para guardar clientes

    # Getters
    def getNombre(self):
        return self._nombre

    def getDireccion(self):
        return self._direccion

    def getRubro(self):
        return self._rubro


    # Setters
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def setDireccion(self, nuevaDireccion):
        self._direccion = nuevaDireccion

    def setRubro(self, nuevoRubro):
        self._dni = nuevoRubro


    def agregarCliente(self, cliente):
        self._clientes.append(cliente)