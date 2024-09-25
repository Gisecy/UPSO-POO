# PRUEBAS DE CLASES COMERCIO Y CLIENTE:

from TP3ejercicio2A import *

# Creo un nuevo cliente y un nuevo comercio
cliente1 = Cliente("Gisela Yede", "12345678", "Mi Casita 123", "2932111111")
comercio1 = Comercio("SuperChino", "Los Chinitos 123", "Almacén")

# Agrego cliente1 a comercio1
comercio1.agregarCliente(cliente1)

# Creo cliente2 y lo agrego al mismo comercio1
cliente2 = Cliente("Juanita Jo", "87654321", "La Callecita 123", "2932123456")
comercio1.agregarCliente(cliente2)

# Obtengo el nombre del primer cliente de comercio1
primerCliente = comercio1._clientes[0]
print("El primer cliente del comercio es: ",primerCliente.getNombre())

# Modifico la dirección de comercio1
comercio1.setDireccion("Av Arigato 123")
print("La dirección del comercio es: ",comercio1.getDireccion())

# Verifico si un cliente está en comercio1
if cliente1 in comercio1._clientes:
    print(f'{cliente1.getNombre()} es cliente de {comercio1.getNombre()}')