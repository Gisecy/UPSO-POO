'''Ejercicio 2:

Realizar una implementación de la clase Libro, que contenga información de su autor, título del libro,
género y cantidad de páginas. Incluir todos los comandos de consulta y modificación de atributos.
Dibujar el diagrama de clases correspondiente.
Implementar los métodos equals, copy y clone. Mostrar ejemplos de uso de cada uno para verificar el
correcto funcionamiento.'''

class Libro:

    def  __init__(self, autor, titulo, genero, nroPaginas):
        self._autor = autor
        self._titulo = titulo
        self._genero = genero
        self._nroPaginas = nroPaginas


    # Getters
    def getAutor(self):
        return self._autor

    def getTitulo(self):
        return self._titulo

    def getGenero(self):
        return self._genero

    def getNroPaginas(self):
        return self._nroPaginas


    # Setters
    def setAutor(self, nuevoAutor):
            self._autor = nuevoAutor

    def setTitulo(self, nuevoTitulo):
        self._titulo = nuevoTitulo

    def setGenero(self, nuevoGenero):
        self._genero = nuevoGenero

    def setNroPaginas(self, nuevaPagina):
        self._nroPaginas = nuevaPagina

#
    def equals(self, otroLibro):
       if isinstance(otroLibro, Libro):
            if (self._autor == otroLibro.getAutor()
                and self._genero == otroLibro.getGenero()
                and self._titulo == otroLibro.getTitulo()
                and self._nroPaginas == otroLibro.getNroPaginas()):
                return True
            else:
                return False
       else:
            return False

    def copy(self, libroACopiar):
        if isinstance(libroACopiar, Libro):
            self._autor = libroACopiar.getAutor()
            self._genero = libroACopiar.getGenero()
            self._titulo = libroACopiar.getTitulo()
            self._nroPaginas = libroACopiar.getNroPaginas()

    def clone(self):
        objetoLibro = Libro(self._autor, self._titulo, self._genero, self._nroPaginas)
        return objetoLibro