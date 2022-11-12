class Tienda:
    """Clase que devuelve información sobre la tienda instanciada"""
    tipo = "Electrodomésticos"
    abierta = True

    def __init__(self, nombre, direccion, n_empleados, ventas_3_meses):
        """
        Argumentos requeridos según parámetro:
            nombre: str (pos)
            direccion: str (pos)
            n_empleados: int (pos)
            ventas_3_meses: list of 3 int (pos)
        """
        self.nombre = nombre
        self.direccion = direccion
        self.n_empleados = n_empleados
        self.ventas_3_meses = ventas_3_meses
        self.marketing = False # Para señalar si el marketing afecta a las ventas de los últimos 3 meses, ver en proyecta_ventas()
        self.inversion_guardada = 0 # Para recordar la inversion de marketing hecha

    def calcula_ventas_totales(self):
        """Suma y devuelve las ventas de los últimos tres meses"""
        return sum(self.ventas_3_meses)

    def calcula_media_ventas(self):
        """Calcula la media de ventas por empleado de los últimos tres meses y la devuelve"""
        return round(self.calcula_ventas_totales()/self.n_empleados, 2)

    def da_nombre_y_direccion(self):
        """Devuelve una string con el nombre y la dirección de la tienda"""
        return f"{self.nombre}, en {self.direccion}"

    def calcula_ultimas_ventas(self):
        """Devuelve las ventas del último mes"""
        return self.ventas_3_meses[-1]

    def proyecta_ventas(self, inversion):
        """Requiere pasar un argumento integer o float. Calcula y devuelve cómo una inversión en marketing cambia las ventas de los últimos 3 meses"""
        if self.marketing == False:
            if inversion < 1000:
                self.ventas_3_meses = list(map(lambda x: int(x * 1.2), self.ventas_3_meses))
            else:
                self.ventas_3_meses = list(map(lambda x: int(x * 1.5), self.ventas_3_meses))
            self.inversion_guardada = inversion
            self.marketing = True
            return self.ventas_3_meses
