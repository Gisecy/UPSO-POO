'''Ejercicio 3
Crear una clase Precio, que modele los diferentes valores de venta
de un producto teniendo en cuenta su precio de lista, recargo por
pago en 3 cuotas y descuento por pago en efectivo. La clase debe
contener un constructor sobrecargado para poder instanciar objetos
con las siguientes opciones:

a) p1 = Precio(1000) # asigna $1000 al precio de lista, no hay
descuentos y no se permite pago en cuotas

b) p2 = Precio(1000, 10 ) # asigna $1000 al precio de lista,
un descuento del 10% por pago efectivo, no se permite pago en cuotas,

c) p3 = Precio(1000, (10, 25) ) # asigna $1000 al precio de lista,
un descuento del 10% por pago efectivo, y opciones de pago en 3 cuotas
con 25% de recargo.

Agregar un método mostrarOpcionesPago, que imprima un mensaje con el
siguiente formato de acuerdo a la información del objeto creado:
p1.mostrarOpcionesPago() # salida esperada: ‘El precio de lista
es $1000 - No hay descuento por pago efectivo - No hay opción de pago
en cuotas.
p2.mostrarOpcionesPago() # salida esperada: ‘El precio de lista
es $1000 - Descuento de 10% por pago efectivo - No hay opción de pago
en cuotas.
p3.mostrarOpcionesPago() # salida esperada: ‘El precio de lista
es $1000 - Descuento de 10% por pago efectivo - Recargo de 25% por
pago en 3 cuotas.'''


class Precio:
    def __init__(self, precioLista, descuento=None):
        self._precioLista = precioLista
        if isinstance(descuento, tuple):
            self._descuento = descuento[0]  # El primer elemento es el descuento
            self._recargoCuotas = descuento[1]  # El segundo elemento es el recargo
        else:
            self._descuento = descuento
            self._recargoCuotas = None

    def mostrarOpcionesPago(self):
        # Mensaje del precio de lista
        mensaje = f"El precio de lista es ${self._precioLista}"

        # Agrego al mensaje de precio de lista, la información sobre el descuento
        if self._descuento is not None:
            mensaje += f" - Descuento de {self._descuento}% por pago efectivo"
        else:
            mensaje += " - No hay descuento por pago efectivo"

        # Agrego al mensaje del precio de lista, la información sobre el recargo de cuotas
        if self._recargoCuotas is not None:
            mensaje += f" - Recargo de {self._recargoCuotas}% por pago en 3 cuotas"
        else:
            mensaje += " - No hay opción de pago en cuotas"

        print(mensaje)


