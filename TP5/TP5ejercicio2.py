'''Ejercicio 2
Crear una clase abstracta A, que especifique dos métodos abstractos
incrementarValor(cantidad) y reducirValor(cantidad). Luego utilizar
a A como padre para crear una clase B y completar la implementación.
B debe tener un atributo _valor, que se pueda incrementar o reducir
en una cantidad determinada utilizando los métodos indicados.'''

from abc import ABC, abstractmethod

# Clase abstracta A
class A(ABC):
    def __init__(self, valor):
        self._valor = valor

    @abstractmethod
    def incrementar_valor(self, cantidad):
        pass

    @abstractmethod
    def reducir_valor(self, cantidad):
        pass


# Clase B que hereda de clase A
class B(A):
    def __init__(self, valor):
        super().__init__(valor)

    def incrementar_valor(self, cantidad):
        self._valor += cantidad
        print(f"Valor incrementado en {cantidad}. Nuevo valor: {self._valor}")

    def reducir_valor(self, cantidad):
        self._valor -= cantidad
        print(f"Valor reducido en {cantidad}. Nuevo valor: {self._valor}")



