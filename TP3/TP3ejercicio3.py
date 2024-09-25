'''Ejercicio 3
Realizar una implementación de la clase Impresora, modelada por una relación de
dependencia con la clase Archivo. Se debe incluir al menos:
- Clase Impresora:
- atributos: _marca: String, _modelo: String, _estaEncendida: bool = False.
- métodos: encender, apagar, imprimirArchivo(archivo: Archivo)
- Clase Archivo:
- atributos: _titulo: String, _cantidadPaginas: entero, _contenido: String.
- métodos: consulta y modificación de atributos.
El método imprimirArchivo debe mostrar en pantalla toda la información del
archivo recibido comoparámetro. Realizar el diagrama UML con la simbología
correspondiente y crear un archivo depruebas para las funcionalidades
implementadas.'''

class Archivo:
    def __init__(self, titulo, cantidadPaginas, contenido):
        self._titulo = titulo
        self._cantidadPaginas = cantidadPaginas
        self._contenido = contenido


    # Getters
    def getTitulo(self):
        return self._titulo

    def getCantidadPaginas(self):
        return self._cantidadPaginas

    def getContenido(self):
        return self._contenido


    # Setter
    def setTitulo(self, nuevoTitulo):
        self._titulo = nuevoTitulo

    def setCantidadPaginas(self, nuevaPagina):
        self._cantidadPaginas = nuevaPagina

    def setContenido(self, nuevoContenido):
        self._contenido = nuevoContenido


class Impresora:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._estaEncendida = False

    def encender(self):
        self._estaEncendida = True

    def apagar(self):
        self._esta_encendida = False

    def imprimirArchivo(self, archivo):
        descripContenido = ""
        if self._estaEncendida:
            descripContenido = f"Imprimiendo archivo: {archivo._titulo} : {archivo._contenido}"
        else:
            descripContenido = "La impresora está apagada. Enciéndala primero para poder imprimir."
        return descripContenido