# PRUEBAS DE CLASES ARCHIVO E IMPRESORA:

from TP3ejercicio3 import *

# Creo un archivo(archivo1) y una impresora(impresora1)
archivo1 = Archivo("Trabajo Práctico Nro. 3", 10, "Programación Orientada a Objetos - Ejercicio de relación de dependencia entre clases. ")
impresora1 = Impresora("Pantum", "P2500W")

# Enciendo la impresora1 e imprimo el archivo1
impresora1.encender()
resultado = impresora1.imprimirArchivo(archivo1)
print(resultado)

# Cambio el título de archivo1 y la cantidad de páginas
archivo1.setTitulo("POO - TP3")
archivo1.setCantidadPaginas(20)

# Imprimo de mnuevo archivo1 con el nuevo título
print(impresora1.imprimirArchivo(archivo1))