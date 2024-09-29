class Cliente():
    def __init__(self, nombre, cuil):
        self._nombre = nombre
        self._cuil = cuil

    # Getters
    def getNombre(self):
        return self._nombre

    def getCuil(self):
        return self._cuil

    # Setters
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def setCuil(self, nuevoCuil):
        self._cuil = nuevoCuil


class Producto():
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    # Getters
    def getNombre(self):
        return self._nombre

    def getPrecio(self):
        return self._precio

    # Setters
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def setPrecio(self, nuevoPrecio):
        self._precio = nuevoPrecio


class Factura():
    def __init__(self, cliente, productos):
        self._cliente = cliente
        self._listaProductos = []
        self._montoTotal = 0

    # Getters
    def getCliente(self):
        return f"Cliente: {self._cliente.getNombre()}, CUIL: {self._cliente.getCuil()}"

    def getMontoTotal(self):
        return self._montoTotal

    # Setters
    def setCliente(self, nuevoCliente):
        if isinstance(nuevoCliente, Cliente):
            self._cliente = nuevoCliente

    # Metodos Operacionales
    def detallarProductos(self):
        for producto in self._listaProductos:
            print(f'{producto.getNombre()} cuesta: {producto.getPrecio()}')

    def agregarProducto(self, producto):
        if isinstance(producto, Producto):
            self._listaProductos.append(producto)

    def quitarProducto(self, producto):
        if isinstance(producto, Producto) and (producto in self._listaProductos):
            self._listaProductos.remove(producto)

    def productoMasCaro(self):
        if len(self._listaProductos) > 0:
            productoCaro = self._listaProductos[0]
            for producto in self._listaProductos:
                if producto.getPrecio() > productoCaro.getPrecio():
                    productoCaro = producto
        return productoCaro



