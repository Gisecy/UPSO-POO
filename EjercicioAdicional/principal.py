from definicionClases import *

# Creamos a los equipos
equipoLocal = Equipo('Equipo 1')
equipoLocal.setListaDeJugadores(['nombre A1','nombre A2','nombre A3','nombre A4','nombre A5'])

equipoVisitante = Equipo('Equipo 2')
equipoVisitante.setListaDeJugadores(['nombre B1','nombre B2','nombre B3','nombre B4','nombre B5'])

# Creamos un clima agradable ¿que pasa si le ponemos false?
elClima = Clima(True)

# Creamos el partido
laFinal = PartidoDeFutbol(equipoLocal, equipoVisitante)

# Comprobamos si hace un buen clima
laFinal.comprobarSiSePuedeJugar(elClima)

if laFinal.getSePuedeJugar():
    # el equipo local anoto los goles en el min 15, min 50 y min 89 <===============
    laFinal.nuevoGol(laFinal.getLosEquipos()[0].getNombreEquipo(), 15)
    laFinal.nuevoGol(laFinal.getLosEquipos()[0].getNombreEquipo(), 50)
    laFinal.nuevoGol(laFinal.getLosEquipos()[0].getNombreEquipo(), 89)
    # el equipo visitante anoto dos goles en el minuto 20 y 45      <===============
    laFinal.nuevoGol(laFinal.getLosEquipos()[1].getNombreEquipo(), 20)
    laFinal.nuevoGol(laFinal.getLosEquipos()[1].getNombreEquipo(), 45)

    # ahora quiero saber el ganador del partido suponiendo que ya finalizo
    print(f'El ganador es {laFinal.ganador().getNombreEquipo()}')
else:
    print('El partido no se puede jugar debido al clima')