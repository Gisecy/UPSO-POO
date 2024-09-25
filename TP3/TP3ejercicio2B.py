'''Ejercicio 2:
b) Una clase AlbumMusical y una clase Tema, considerando que un álbum musical tiene un
conjunto de temas.
Definir al menos tres atributos en cada clase e implementar el modelo elegido.
Crear un archivo de pruebas para las funcionalidades implementadas.'''

class Tema:
    def __init__(self, titulo, duracion):
        self._titulo = titulo
        self._duracion = duracion


    #Getters
    def getTitulo(self):
        return self._titulo

    def getDuracion(self):
        return self._duracion

    #Setters
    def setTitulo(self, nuevoTitulo):
        self._titulo = nuevoTitulo

    def setDuracion(self, nuevaDuracion):
        self._duracion = nuevaDuracion


class AlbumMusical:
    def __init__(self, titulo, artista, anio):
        self._titulo = titulo
        self._artista = artista
        self._anio = anio
        self._temas = []


    # Getters
    def getTitulo(self):
        return self._titulo

    def getArtista(self):
        return self._artista

    def getAnio(self):
        return self._anio


    # Setters
    def setTitulo(self, nuevoTitulo):
        self._titulo = nuevoTitulo

    def setArtista(self, nuevoArtista):
        self._artista = nuevoArtista

    def setAnio(self, nuevoAnio):
        self._anio = nuevoAnio


    # Metodos Operacionales
    def agregarTema(self, tema):
        self._temas.append(tema)