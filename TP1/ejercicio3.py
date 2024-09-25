# EJERCICIO 3:

"""
Evaluar, si es posible, las siguientes expresiones lógicas. En los casos que no sea posible, explicar el
motivo. Responder considerando que las variables indicadas tienen los siguientes valores:
a = 5, b= 8, c = 1.5, d= True , e = ’10’.
a) a < 8
b) a < b
c) a <= b
d) (a-b) < c
e) c < e
f) not(d)
g) e > ‘4’
"""

def evaluar(a,b,c,d,e):
    print(a < 8)
    print(a < b)
    print(a <= b)
    # print((a-b) < c) # No se puede comparar un int con un string
    # print(c < e) # No se puede comparar un int con un string
    print(not(d))
    print(e > '4') # Se pueden comparar cadenas de texto pero me dio False

evaluar(5, 8, 1.5, True,'10')