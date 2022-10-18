class Tienda():
    '''
    Doc String
    xxxxxxxxx
    '''
    def __init__(self, nombre, direccion, empleados, ventas, tipo="Electrodomésticos", abierta=True):
        self.phone = tipo
        self.abierta = abierta
        self.nombre = nombre
        self.direccion = direccion
        self.empleados = empleados
        self.ventas = ventas
        print("Clase Tienda inicializada correctamente!")

    def total_ventas (self):
        total = sum([i for i in self.ventas])
        self.total = total
        return total
    
    def media_ventas_empleado (self):
        return (sum(i for i in self.ventas)/len(self.ventas))/self.empleados

    def tienda_direccion (self):
        return "{} está en: {}".format(self.nombre, self.direccion)

    def ventas_ultimo_mes (self):
        return self.ventas[-1]

    def proyeccion_ventas (self, inversion):
        return self.total * 1.5 if inversion >= 1000 else self.total * 1.2



        