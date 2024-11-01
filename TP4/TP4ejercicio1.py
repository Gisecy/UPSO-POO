'''Ejercicio 1
Implementar una clase Caja, con atributos correspondientes a su material y sus medidas de ancho,
largo (profundidad) y alto. Generar métodos de clase para constructores específicos de cajaGrande,
cajaChica, cajaCarton, cajaPlastica y definir al menos dos opciones más.
Implementar además un método estático, que permita determinar si una caja entra o no en una
estantería de 50cm de ancho, 40cm de profundidad y 30cm de alto.'''


class Caja:
    def __init__(self, material, ancho, largo, alto):
        self._material = material
        self._ancho = ancho
        self._largo = largo
        self._alto = alto


     #Getters:
    def getMaterial(self):
        return self._material

    def getAncho(self):
        return self._ancho

    def getLargo(self):
        return self._largo

    def getAlto(self):
        return self._alto

    # Setters:
    def setMaterial(self, nuevo):
        self._material = nuevo

    # Métodos mágicos:
    def __str__(self):
        return f'Caja de {self._material} de {self._ancho} de ancho, {self._largo} de largo y {self._alto} de alto'

    # Meétodos de clase para constructores específicos
    @classmethod
    def cajaGrande(cls):
        return cls("cartón", 50, 40, 30)

    @classmethod
    def cajaChica(cls):
        return cls("pvc", 10, 10, 10)

    # Métodos de clases para constructores no específicos
    @classmethod
    def cajaCarton(cls, ancho, largo, alto):
        return cls("cartón", ancho, largo, alto)

    @classmethod
    def cajaPlastica(cls, ancho, largo, alto):
        return cls("plástico", ancho, largo, alto)

    # Otros métodos de clase (2 ejemplos solicitados)
    @classmethod
    def cajaRigida(cls, material, ancho, largo, alto):
        return cls(material, ancho, largo, alto)

    @classmethod
    def cajaPersonalizada(cls, material, ancho, largo, alto):
        return cls(material, ancho, largo, alto)

    # Metodo estático para ver si la caja cabe en la estantería.
    @staticmethod
    def cabeEnEstanteria(caja, anchoEstanteria=50, largoEstanteria=40, altoEstanteria=30):
        if caja.getAncho() <= anchoEstanteria and caja.getLargo() <= largoEstanteria and caja.getAlto() <= altoEstanteria:
            return f'La {caja} entra en la estantería.'
        else:
            return f'La {caja} no entra en la estantería.'




