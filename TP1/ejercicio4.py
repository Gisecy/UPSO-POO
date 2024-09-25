#EJERCICIO 4:

"""
El operador de módulo (%) permite obtener el resto de la división entera, y es útil en
muchas aplicaciones. En cada uno de los siguientes incisos, indicar cómo puede emplearse
para resolver el problema planteado:
a) Determinar si un número es par o impar.
b) Determinar si un valor ingresado por el usuario es múltiplo de 4.
c) Determinar si un valor ingresado por el usuario es múltiplo de 3 ó divisor de 36.
d) Determinar si un valor ingresado por el usuario es múltiplo de 3 y divisor de 36.
"""

#a)
def modulo(numero):
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

modulo(12)
modulo(13)

#b)
def multiplo(numero):
    if numero % 4 == 0:
        print(numero, "Es múltiplo de 4")
    else:
        print(numero, "No es múltiplo de 4")


numero = int(input("Ingrese un numero: "))
multiplo(numero)

#c)
def multiploODivisor(numero):
    if numero % 3 == 0 or 36 % numero == 0:
        print(f"El número {numero} es múltiplo de 3 o divisor de 36.")
    else:
        print(f"El número {numero} no es múltiplo de 3 ni divisor de 36.")


numero = int(input("Ingrese un numero: "))
multiploODivisor(numero)


#d)
def multiploYDivisor(numero):
    if numero % 3 == 0 and 36 % numero == 0:
        print(f"El número {numero} es múltiplo de 3 y divisor de 36.")
    else:
        print(f"El número {numero} no es múltiplo de 3 ni divisor de 36.")

numero = int(input("Ingrese un numero: "))
multiploYDivisor(numero)
