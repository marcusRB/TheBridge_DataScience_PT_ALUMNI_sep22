class Tienda():
    '''
    Crea instancias de tipo tienda
    Métodos:
        total_ventas: Total ventas de cada tienda
        media_ventas_empleado: Media de ventas de cada empleado por tienda
        tienda_direccion: Datos básicos con nombre y dirección
        ventas_ultimo_mes: Ventas realizadas en el último mes
        proyeccion_ventas: Predicción ventas en función de una inversion dada

    Atributos:
        nombre: str
        direccion: str
        empleados: int
        ventas: list
    Atributos opcionales:
        tipo: str -> Electrodomesticos
        abierta: bool -> True

    Date: 18/10/2022
    Author: Cisco Calero

    '''
    def __init__(self, nombre, direccion, empleados, ventas, tipo="Electrodomésticos", abierta=True):
        # Hacemos globales los argumentos de creación de la instancia
        self.tipo = tipo
        self.abierta = abierta
        self.nombre = nombre
        self.direccion = direccion
        self.empleados = empleados
        self.ventas = ventas
        print("Clase Tienda inicializada correctamente!")

    # Método para el cálculo del total de ventas del último trimestre
    def total_ventas (self):
        total = sum([i for i in self.ventas])
        self.total = total
        return total

    # Método para el cálculo de ventas media por empleado
    def media_ventas_empleado (self):
        return (sum(i for i in self.ventas)/len(self.ventas))/self.empleados

    # Método que devuelve el nombre y la dirección de una instancia tienda
    def tienda_direccion (self):
        return "{} está en: {}".format(self.nombre, self.direccion)

    # Método que devuelve las ventas del último mes
    def ventas_ultimo_mes (self):
        return self.ventas[-1]

    # Método que calcula la proyección de ventas en función d
    # de la inversión que se hace en acciones de marketing
    def proyeccion_ventas (self, inversion):
        return self.total * 1.5 if inversion >= 1000 else self.total * 1.2



        