from EjParcialejercicio2 import *

# Creo un cliente y lo meustro por consola
cliente1 = Cliente("Juan Pérez", "20-3456789-1")
print(f'El cliente1 es : {cliente1.getNombre()} y su cuil: {cliente1.getCuil()} ')

# Creo productos y los meustro por consola
producto1 = Producto("Camiseta", 1500)
producto2 = Producto("Pantalón", 2000)
print(f'Producto: {producto1.getNombre()} Precio: ${producto1.getPrecio()}')
print(f'Producto: {producto2.getNombre()} Precio: ${producto2.getPrecio()}')

# Creo una factura
factura1 = Factura(cliente1, [])  # Sin productos inicialmente

print("El cliente de factura1 es: ", factura1.getCliente())

# Agrego productos a la factura
factura1.agregarProducto(producto1)
factura1.agregarProducto(producto2)

# Obtengo el producto más caro
productoMasCaro = factura1.productoMasCaro()
print(f"El producto más caro es: {productoMasCaro.getNombre()} con un precio de {productoMasCaro.getPrecio()}")

# Detallo los productos de la factura
print("Los productos de factura1 son: ")
factura1.detallarProductos()