class Tienda:
    """
    Descripcion
        Clase tienda.
    Attribs:
        tipo:       str   = 'Electrodomesticos'
        abierta:    bool  = True
        
        nombre:     str     pos Nombre de la tienda
        direccion:  str     pos Direccion de la tienda
        empleados:  int     pos Nº empleados
        ventas:     list    pos Lista 3 valores float
        
    """
    
    def __init__(self,nombre:str, direccion:str, empleados:int, ventas:list):
        self.tipo = 'Electrodomesticos'
        self.abierta = True
        
        self.nombre = nombre
        self.direccion = direccion
        self.empleados = empleados
        self.ventas = ventas

    def ventas_meses(self):
        """Calcula la suma de las ventas

        Returns:
            Suma de ventas
        """
        return sum([cantidad for cantidad in self.ventas])
    
    def ventas_meses_empleado(self):
        """Calcula la media de ventas por empleado

        Returns:
            sum(ventas)/empleados
        """
        return sum([cantidad for cantidad in self.ventas])/self.empleados
    
    def nombre_direccion(self):
        """Muestra nombre y dirección de la tienda

        Returns:
            String nombre + dirección
        """
        return self.nombre + ' ' + self.direccion
    
    def ventas_ult_mes(self):
        """Muestra ventas del último mes

        Returns:
            float: Ventas del último mes
        """
        return self.ventas[-1]
    
    def proyeccion_ventas(self, inversion:float):
        """Calcula la proyección de las ventas
        basada en una inversión en marketing

        Args:
            inversion (float): pos - Cantidad invertida

        Returns:
            list: Lista con los valores de las ventas modificados
        """
        if inversion < 1000:
            self.ventas = [cantidad*1.2 for cantidad in self.ventas]
            return self.ventas
            
        else:
            self.ventas = [cantidad*1.5 for cantidad in self.ventas]
            return self.ventas