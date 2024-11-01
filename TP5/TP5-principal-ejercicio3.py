# PRUEBAS DE EJERCICIO 3:

from TP5ejercicio3 import *

p1 = Precio(1000)
p1.mostrarOpcionesPago()  # Salida esperada: El precio de lista es $1000 - No hay descuento por pago efectivo - No hay opción de pago en cuotas

p2 = Precio(1000, 10)
p2.mostrarOpcionesPago()  # Salida esperada: El precio de lista es $1000 - Descuento de 10% por pago efectivo - No hay opción de pago en cuotas

p3 = Precio(1000, (10, 25))
p3.mostrarOpcionesPago()  # Salida esperada: El precio de lista es $1000 - Descuento de 10% por pago efectivo - Recargo de 25% por pago en 3 cuotas
