# PRUEBAS DE CLASE TELEVISOR:

from EjParcialejercicio1 import *

# Creo un televisor
televisor1 = Televisor("Samsung", 50, 1, 20, False)

# Enciendo el televisor
televisor1.encender()
print("El televisor está encendido:", televisor1.getEncendido())

# Apago el televisor
televisor1.apagar()
print("El televisor está encendido:", televisor1.getEncendido())

# Enciendo el televisor y pao al siguiente canal
televisor1.encender()
print("El televisor está encendido:", televisor1.getEncendido())
televisor1.canalSiguiente()
print("Canal actual:", televisor1.getCanalActual())

# Vuelvo al canal anterior
televisor1.canalAnterior()
print("Canal actual:", televisor1.getCanalActual())

# Vuelvo al canal visto antes del último cambio
televisor1.canalPrevio()
print("Canal actual:", televisor1.getCanalActual())

# Subo el volumen
televisor1.subirVolumen()
print("Volumen actual:", televisor1.getVolumen())

# Bajo el volumen
televisor1.bajarVolumen()
print("Volumen actual:", televisor1.getVolumen())

# Silencio el televisor(mute)
televisor1.silenciar()
print("Volumen actual:", televisor1.getVolumen())

# Creo un nuevo televisor y lo enciendo
televisor2 = Televisor("Noblex", 100, 1, 50, False)
televisor2.encender()

for i in range(televisor2.getTotalCanales()-1):
    televisor2.canalSiguiente()
    print("Canal actual:", televisor2.getCanalActual())


televisor2.canalPrevio()
print("Canal actual después de volver atrás:", televisor2.getCanalActual())