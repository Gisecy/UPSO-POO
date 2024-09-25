# PRUEBAS DE CLASES TEMA Y ALBUMMUSICAL:

from TP3ejercicio2B import *

# Creo un album musical(album1) y dos temas (tema1 y tema2)
tema1 = Tema("Princes of the universe", 3)
tema2 = Tema("Who wants to live forever", 5.15)

# Agrego los temas al album1
album1 = AlbumMusical("A kind of Magic", "Queen", 1986)
album1.agregarTema(tema1)
album1.agregarTema(tema2)

# Cambio el titulo de album1 y la duracion del tema1
album1.setTitulo("Queen: Greatest Hits I")
tema1.setDuracion(3.32)

# Obtengo la informacion de album1 y sus temas
print(f"El álbum {album1.getTitulo()} tiene {len(album1._temas)} temas.")
for tema in album1._temas:
    print(f"* {tema.getTitulo()} / Duración: {tema.getDuracion()} mins")