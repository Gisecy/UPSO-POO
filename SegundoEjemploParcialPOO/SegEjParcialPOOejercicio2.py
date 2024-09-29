class Guion():
    def __init__(self, escritor, genero):
        self._escritor = escritor
        self._genero = genero

    # Getters
    def getEscritor(self):
        return self._escritor

    def getGenero(self):
        return self._genero

    # Setters
    def setEscritor(self, escritor):
        self._escritor = escritor

    def setGenero(self, genero):
        self._genero = genero


class Actor():
    def __init__(self, nombre, edad, nacionalidad):
        self._nombre = nombre
        self._edad = edad
        self._nacionalidad = nacionalidad

    # Getters
    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getNacionalidad(self):
        return self._nacionalidad

    # Setters
    def setNombre(self,nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setNacionalidad(self, nacionalidad):
        self._nacionalidad = nacionalidad


class Director():
    def __init__(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre


class Pelicula():
    def __init__(self, nombre, guion, directores):
        self._nombre = nombre
        self._guion = guion
        self._actores = []
        self._directores = directores

    # Getters
    def getNombre(self):
        return self._nombre

    # Setters
    def setNombre(self, nombre):
        self._nombre = nombre

    def setGuion(self, guion):
        if isinstance(guion, Guion):
            self._guion = guion

    # Métodos operacionales
    def detallarGuion(self):
        print(f"Guion: {self._guion.getEscritor()} - {self._guion.getGenero()}")

    def mostrarActores(self):
        if self._actores:
            for actor in self._actores:
                print(f"- {actor.getNombre()} ({actor.getEdad()} años), {actor.getNacionalidad()}")
        else:
            print("La película no tiene actores asignados.")

    def mostrarDirectores(self):
        if len(self._directores) > 0:
            for director in self._directores:
                print(f"- {director.getNombre()}")
        else:
            print("La película no tiene directores asignados.")

    def agregarActor(self, actor):
        if isinstance(actor, Actor):
            self._actores.append(actor)

    def quitarActor(self, actor):
        if isinstance(actor, Actor) and actor in self._actores:
            self._actores.remove(actor)

    def actorMasJoven(self):
        if self._actores:
            menor_edad = self._actores[0]
            for actor in self._actores:
                if actor.getEdad() < menor_edad.getEdad():
                    menor_edad = actor
            return menor_edad
        else:
            return None