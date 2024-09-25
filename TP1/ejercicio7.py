# EJERCICIO 7:

"""
En una aplicación para generar una cuenta de usuario, se aplica una serie de controles
para que el usuario ingrese su nombre de usuario de manera correcta, teniendo en cuenta
que debe respetar las siguientes condiciones:

a) Debe contener al menos 6 caracteres.
b) Debe comenzar con una letra mayúscula y todas las demás en minúsculas.
c) No debe tener espacios al comienzo ni al final.
d) No puede contener números.

Indicar las expresiones necesarias para realizar cada uno de los controles sobre la
variable nombreUsuario. Luego implementar un programa que permita al usuario ingresar
el nombre deseado e indicar si es correcto o no cumple alguna de las condiciones
solicitadas.
Agregar al menos dos condiciones más (a elección) e implementarlas junto a las anteriores.
"""

"""import re

def validarUsuario(nombreUsuario):
    Valida un nombre de usuario según las condiciones establecidas.

    Args:
        nombreUsuario: El nombre de usuario a validar.

    Returns:
        True si el nombre es válido, False en caso contrario.
    

    # Expresiones regulares para las validaciones (regex)
    patron_longitud = r".{6,}"  # Al menos 6 caracteres
    patron_mayuscula = r"^[A-Z][a-z]+$"  # Comienza con mayúscula, resto minúsculas
    patron_espacios = r"^\S+\s*$"  # Sin espacios al principio ni al final
    patron_numeros = r"^[^0-9]+$"  # Sin números
    patron_especial = r"[^a-zA-Z0-9\s].+"  # Al menos un caracter especial
    patron_vocal = r"[aeiouAEIOU].+"  # Al menos una vocal en cualquier posición

    # Verificar todas las condiciones
    return (
            re.match(patron_longitud, nombreUsuario)
            and re.match(patron_mayuscula, nombreUsuario)
            and re.match(patron_espacios, nombreUsuario)
            and re.match(patron_numeros, nombreUsuario)
            and re.search(patron_especial, nombreUsuario)
            and re.search(patron_vocal, nombreUsuario)
    )"""

def validarUsuario(nombreUsuario):
    """Valida un nombre de usuario según las condiciones establecidas.

    Args:
        nombreUsuario: El nombre de usuario a validar.

    Returns:
        True si el nombre es válido, False en caso contrario.
    """

    # Condiciones de validación
    if len(nombreUsuario) < 6:
        return False  # Debe tener al menos 6 caracteres
    if not nombreUsuario[0].isupper() or not nombreUsuario[1:].islower():
        return False  # Debe comenzar con mayúscula y el resto minúsculas
    if nombreUsuario.startswith(' ') or nombreUsuario.endswith(' '):
        return False  # No debe tener espacios al principio ni al final
    if any(char.isdigit() for char in nombreUsuario):
        return False  # No puede contener números
    if not any(char.isalpha() for char in nombreUsuario):
        return False  # Debe contener al menos una letra
    if not any(char in 'aeiouAEIOU' for char in nombreUsuario):
        return False  # Debe contener al menos una vocal

    # Si todas las condiciones se cumplen, el nombre es válido
    return True




print("El nombre de usuario debe respetar las siguientes condiciones: \na) Debe contener al menos 6 caracteres.\nb) Debe comenzar con una letra mayúscula y todas las demás en minúsculas.\nc) No debe tener espacios al comienzo ni al final.\nd) No puede contener números.\ne) Debe contener al menos un caracter especial \nf) Debe contener al menos una vocal.")

nombreUsuario = input("Ingrese su nombre de usuario: ")
if validarUsuario(nombreUsuario):
    print("Nombre de usuario válido.")
else:
    print("Nombre de usuario inválido. Por favor, verifique las condiciones.")

