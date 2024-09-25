# EJERCICIO 13:

"""
Implementar una función contieneCifra(numero, cifra), que devuelva un valor booleano
indicando si la cifra aparece en el número dado.

Ejemplos: b = contieneCifra(123, 2) # True b = contieneCifra(123, 5) # False
"""

def contieneCifra(numero, cifra):
  """Verifica si una cifra está presente en un número.

  Args:
    numero: El número a evaluar.
    cifra: La cifra a buscar.

  Returns:
    True si la cifra está presente, False en caso contrario.
  """

  return str(cifra) in str(numero)

# Ejemplos:
print(contieneCifra(123, 2))  # True
print(contieneCifra(123, 5))  # False