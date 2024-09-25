# PRUEBAS DE CLASES DE EJERCICIO 1:

from TP2ejercicio1 import *

# Prueba de Clase Monitor:

# Creo un monitor (monitor1) y muestro por consola la marca:
monitor1 = Monitor("Samsung", 24, "LED", "HDMI")
print(monitor1)
print(monitor1.getMarca())

# Cambio el tipo de pantalla de monitor1 y lo muestro por consola:
monitor1.setTipoPantalla("LCD")
print(monitor1.getTipoPantalla())


# Prueba de Clase Teclado:

# Creo un teclado (teclado1) y muestro por consola el lenguaje:
teclado1 = Teclado("Logitech", "Español", True, True)
print(teclado1.getLenguaje())

# Cambio la retroiluminación del teclado a falso:
teclado1.setRetroiluminacion(False)
print(teclado1.getRetroiluminacion())

