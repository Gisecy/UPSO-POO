# PRUEBAS DE CLASE COMPUTADORA, MONITOR Y TECLADO:

from TP3ejercicio1 import *

# Creo los  objetos
monitor1 = Monitor("Samsung", 27, "LED", "HDMI")
teclado1 = Teclado("Logitech", "Español", True, True)
computadora1 = Computadora("Dell", "XPS 13", "Intel Core i7", 16, 512, "Windows 11", monitor1, teclado1)

print(monitor1.__dict__)
print(teclado1.__dict__)
print(computadora1.__dict__)

# Obtengo  información de computadora1(marca y tamaño del monitor)
print("La marca de computadora1 es: ", computadora1.getMarca())

# Obtengo el tamaño del monitor de computadora1
tamanioComputadora1 = computadora1.obtenerTamanioMonitor()
print("El tamaño del monitor de la computadora1 es: ",tamanioComputadora1)

# Obtengo el tamaño del monitor de computadora1
tamanioComputadora1 = computadora1.obtenerMarcaTeclado()
print("La marca del teclado de la computadora1 es: ",tamanioComputadora1)

# Modifico la memoria RAM de computadora1
computadora1.setMemoriaRam(32)
print("La memoria RAM nueva es: ", computadora1.getMemoriaRam())

