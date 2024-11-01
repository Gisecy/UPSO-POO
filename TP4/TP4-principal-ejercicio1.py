# PRUEBAS DE EJERCICIO 1:

from TP4ejercicio1 import *

## Creo una caja grande
cajaG = Caja.cajaGrande()
print(cajaG)

# Creo una caja de plástico
cajaPvc = Caja.cajaPlastica(20, 30, 15)
print(cajaPvc)

# Creo una caja rígida
cajaR = Caja.cajaRigida("metal",35, 25, 20)
print(cajaR)

# Creo una caja personalizada
cajaPer = Caja.cajaPersonalizada("madera",40, 30, 25)
print(cajaPer)

# Consulto el material de una caja
print(cajaG.getMaterial())

# Cambio el material de caja plástica
cajaPvc.setMaterial("cartón")
print(cajaPvc)

# Verifico si caja grande cabe en la estantería
resultado = Caja.cabeEnEstanteria(cajaG)
print(resultado)

