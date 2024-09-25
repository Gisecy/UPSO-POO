# EJERCICIO 14:

"""
a) Implementar una función de devuelva el mayor de dos números reales.

b) Utilizando la solución del inciso anterior, implementar una función que devuelva el
mayor de tres números reales.
"""

# a) Encontrar el mayor de dos numeros reales:

def mayorDosNumeros(num1, num2):
  """Devuelve el mayor de dos números reales.

  Args:
    num1: Primer número.
    num2: Segundo número.

  Returns:
    El mayor de los dos números.
  """

  if num1 > num2:
    return num1
  else:
    return num2

# Ejemplo de uso:
resultado = mayorDosNumeros(5.2, 3.8)
print("El mayor de los dos números es:", resultado)

# b) Encontrar el mayor de tres numeros reales:

def mayorTresNumeros(num1, num2, num3):
  """Devuelve el mayor de tres números reales.

  Args:
    num1: Primer número.
    num2: Segundo número.
    num3: Tercer número.

  Returns:
    El mayor de los tres números.
  """

  # Utilizo la función mayor_dos_numeros para comparar los números de a pares
  mayor_de_dos = mayorDosNumeros(num1, num2)
  mayor_final = mayorDosNumeros(mayor_de_dos, num3)

  return mayor_final

# Ejemplo de uso:
resultado = mayorTresNumeros(2.5, 7.1, 4.3)
print("El mayor de los tres números es:", resultado)