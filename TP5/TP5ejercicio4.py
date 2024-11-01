'''Crear una clase Numeros, que pueda ser instanciada a
partir de una lista de valores numéricos reales. Luego
incorporar los métodos mágicos necesarios para poder iterar
un objeto extrayendo únicamente los valores positivos.
Ejemplo:
Si se crea el objeto
num1 = Numeros([3, 6, -2, 0.5, -103, -71.3, 12.34])
luego debe poder ejecutarse el código:
for positivo in num1:
print(positivo)
Salida esperada:
3
6
0.5
12.34'''

class Numeros:
    def __init__(self, listaReales):
        self._listaReales = listaReales

    '''def __iter__(self): # Consulta del yield como en el TP4, se puede desarrollar asi?
        for valor in self._listaReales:
            if valor > 0:
               yield valor'''

    def __iter__(self):
        self._ind = 0
        return self

    def __next__(self):
        while self._ind < len(self._listaReales):
            valor = self._listaReales[self._ind]
            self._ind += 1
            if valor > 0:
                return valor
        raise StopIteration
