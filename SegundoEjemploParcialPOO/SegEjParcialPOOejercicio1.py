class Informe():
    def __init__(self, titulo, autor, contenido,confirmado, codSeguridad=0):
        self._titulo = titulo
        self._autor = autor
        self._contenido = contenido
        self._codSeguridad = codSeguridad
        self._confirmado = confirmado

    # Getters
    def getTitulo(self):
        return self._titulo

    def getAutor(self):
        return self._autor

    def getContenido(self):
        return self._contenido

    def getCodSeguridad(self):
        return self._codSeguridad

    def getConfirmado(self):
        return self._confirmado


    # Setters
    def setTitulo(self, nuevoTitulo):
        self._ = nuevoTitulo

    def setAutor(self, nuevoAutor):
        self._ = nuevoAutor

    def setContenido(self, nuevoContenido):
        self._ = nuevoContenido

    def setConfirmado(self, nuevoEstado):
        self._ = nuevoEstado


    # Métodos Operacionales
    def esConfidencial(self):
        if self._codSeguridad != 0:
            return True
        else:
            self._codSeguridad = 0
            return False

    def agregarContenido(self, frase):
        if not self._confirmado:
            self._contenido += " " + frase
            return True
        else:
            return False

    def eliminarContenido(self, frase):
        if not self._confirmado and frase in self._contenido:
            self._contenido = self._contenido.replace(frase,"")
            return True
        else:
            return False

    def mostrarDetalle(self,codigo):
        if self.esConfidencial() and codigo == self._codSeguridad:
            print(f'TITULO: {self._titulo}, AUTOR: {self._autor} CONTENIDO: {self._contenido}')
        else:
            print(f'TITULO: {self._titulo}, AUTOR: {self._autor}')


    def confirmarInforme(self):
        self._confirmado = True

