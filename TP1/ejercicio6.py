# EJERCICIO 6:

"""
El lenguaje Pyhton provee diversas formas de utilizar cadenas para mostrar
resultados en la pantalla. Considerando que se tienen las variables marca = “Motorola”,
modelo = “G8”, memoria =“3”, indicar tres o más formas distintas de generar
la frase “Su celular es el modelo G8 de la marca Motorola y tiene 3GB de RAM”.
"""

marca = "Motorola"
modelo = "G8"
memoria = "3"

# Format String
print(f"Su celular es el modelo {modelo} de la marca {marca} y tiene {memoria}GB de RAM.")

# Format()
print("Su celular es el modelo {} de la marca {} y tiene {}GB de RAM.".format(modelo, marca, memoria))

# Concatenación Simple
print("Su celular es el modelo " + modelo + " de la marca " + marca + " y tiene " + memoria + "GB de RAM.")

