# EJERCICIO 15:

"""
Implementar las funciones necesarias para realizar las siguientes operaciones de un
software que permite trabajar con polinomios cuadráticos.
a. A partir de los coeficientes de la forma polinómica, implementar una función que
genere una cadena de caracteres con la expresión correspondiente.
Ejemplo: si a=2,b=4,c=5, generar la cadena “P(x)=2*x^2 + 4*x + 5”.

b. A partir de los coeficientes de la forma polinómica, determinar si tiene raíces
reales y en caso afirmativo calcularlas.

c. Usando el subprograma del inciso anterior, generar una cadena de caracteres con la
formafactorizada.

Ejemplo: si a=6 y las raíces son x1=2, x2=5, generar la cadena “P(x)=6(x-2)(x-5)”
d. Implementar una función que permita evaluar el polinomio en un valor de x dado.
d. Utilizando la función del inciso anterior, implementar un subprograma para determinar
el punto x de un intervalo dado donde el polinomio toma el menor valor. Los extremos del
intervalo [ xmin , xmax ] deben ser recibidos por parámetro, además de un parámetro
adicional maxdif , que indicará la distancia entre dos puntos de evaluación consecutivos.
Ejemplos:
Si el intervalo es [1,4] y maxdif es 0.1, el polinomio se deberá evaluar en los
puntos 1; 1.1;1.2; 1.3; …; 3.8; 3.9; 4. En cambio, si maxdif es 1, el polinomio se
deberá evaluar en los puntos 1; 2; 3; 4.
"""

import math

def polinomioACadena(a, b, c):
  """Convierte un polinomio cuadrático a una cadena de caracteres.

  Args:
    a: Coeficiente cuadrático.
    b: Coeficiente lineal.
    c: Término independiente.

  Returns:
    Una cadena representando el polinomio.
  """

  return f"P(x)={a}*x^2 + {b}*x + {c}"

def tieneRaicesReales(a, b, c):
  """Determina si un polinomio cuadrático tiene raíces reales y las calcula.

  Args:
    a: Coeficiente cuadrático.
    b: Coeficiente lineal.
    c: Término independiente.

  Returns:
    Una tupla (tiene_raices, x1, x2), donde tiene_raices es un booleano y x1, x2 son las raíces.
  """

  discriminante = b**2 - 4*a*c
  if discriminante < 0:
    return False, None, None
  else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    return True, x1, x2

def polinomioFactorizado(a, b, c):
  """Devuelve una cadena con la forma factorizada del polinomio.

  Args:
    a: Coeficiente cuadrático.
    b: Coeficiente lineal.
    c: Término independiente.

  Returns:
    Una cadena representando el polinomio factorizado.
  """

  tiene_raices, x1, x2 = tieneRaicesReales(a, b, c)
  if tiene_raices:
    return f"P(x)={a}(x-{x1})(x-{x2})"
  else:
    return "El polinomio no tiene raíces reales"

def evaluarPolinomio(a, b, c, x):
  """Evalúa un polinomio cuadrático en un punto x.

  Args:
    a: Coeficiente cuadrático.
    b: Coeficiente lineal.
    c: Término independiente.
    x: Valor en el que evaluar el polinomio.

  Returns:
    El valor del polinomio en x.
  """

  return a*x**2 + b*x + c

def encontrarMinimo(a, b, c, xmin, xmax, maxdif):
  """Encuentra el punto x de un intervalo donde el polinomio toma el menor valor.

  Args:
    a: Coeficiente cuadrático.
    b: Coeficiente lineal.
    c: Término independiente.
    xmin: Extremo izquierdo del intervalo.
    xmax: Extremo derecho del intervalo.
    maxdif: Distancia máxima entre dos puntos de evaluación consecutivos.

  Returns:
    Una tupla (x_min, y_min), donde x_min es el punto donde se alcanza el mínimo e y_min es el valor mínimo.
  """

  # Ensure xmin and xmax are integers for the range function
  xmin = int(xmin)
  xmax = int(xmax)

  # Option 1: Adjust maxdif for very small values (might lead to slightly larger steps)
  # maxdif = 0.01 + maxdif  # Add a small offset to avoid zero step size

  # Option 2: Calculate step size based on interval (more precise control)
  num_points = int((xmax - xmin) / maxdif) + 1  # Ensure at least one point per unit
  step_size = (xmax - xmin) / (num_points - 1)  # Calculate actual step size
  puntos_evaluacion = [xmin + i * step_size for i in range(num_points)]  # Generate evaluation points

  x_min = xmin
  y_min = evaluarPolinomio(a, b, c, xmin)

  for x in puntos_evaluacion:
    y = evaluarPolinomio(a, b, c, x)
    if y < y_min:
      x_min = x
      y_min = y

  return x_min, y_min
a = 2
b = -5
c = 3

print(polinomioACadena(a, b, c))
tiene_raices, x1, x2 = tieneRaicesReales(a, b, c)
print(f"Tiene raíces reales: {tiene_raices}")
if tiene_raices:
  print(f"Raíces: x1={x1}, x2={x2}")
  print(polinomioFactorizado(a, b, c))

# Evaluo en x=2
valor = evaluarPolinomio(a, b, c, 2)
print(f"P(2) = {valor}")

# Encuentro el mínimo en el intervalo [1, 4] con maxdif=0.1
xmin = 1
xmax = 4
maxdif = 0.1

x_min, y_min = encontrarMinimo(a, b, c, xmin, xmax, maxdif)
print(f"El mínimo se alcanza en x={x_min} y su valor es {y_min}")