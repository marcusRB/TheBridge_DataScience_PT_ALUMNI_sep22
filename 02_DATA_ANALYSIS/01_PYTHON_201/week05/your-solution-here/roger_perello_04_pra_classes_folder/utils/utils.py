class Pruebas:
    """Esta clase sirve para extraer toda la informacion de una instancia de la clase Tienda, de config.py, y comprobar que es correcta"""
    marketing = " con marketing"
    sin_marketing = " sin marketing"
    
    def __init__(self, tienda):
        """Hay que incorporar como parámetro la tienda con la que queremos probar, que es una instancia de Tienda"""
        self.tienda = tienda

    def da_atributos_clase(self):
        """Imprime los atributos de la clase, que son los mismos para cualquier tienda"""
        print(f"Tipo de tienda: {self.tienda.tipo}")
        print(f"¿La tienda está abierta? {self.tienda.abierta}")
        print("\n")

    def da_atributos_instancia(self):
        """Imprime los atributos de la instancia, que varían en función de la tienda"""
        print(f"Nombre: {self.tienda.nombre}")
        print(f"Dirección: {self.tienda.direccion}")
        print(f"Número de empleados: {self.tienda.n_empleados}")
        print(f"Ventas de los últimos tres meses{self.marketing if self.tienda.marketing == True else self.sin_marketing}: {self.tienda.ventas_3_meses}")
        print("\n")

    def da_metodos_instancia(self, inversion):
        """Imprime los métodos de instancia, requiere la inversón elegida como parámetro (integer o float)"""
        print(f"Nombre y dirección: {self.tienda.da_nombre_y_direccion()}")
        print(f"Ventas totales de los últimos tres meses{self.marketing if self.tienda.marketing == True else self.sin_marketing}: {self.tienda.calcula_ventas_totales()}")
        print(f"Media de las ventas de los últimos tres meses por empleado{self.marketing if self.tienda.marketing == True else self.sin_marketing}: {self.tienda.calcula_media_ventas()}")
        print(f"Ventas del último mes{self.marketing if self.tienda.marketing == True else self.sin_marketing}: {self.tienda.calcula_ultimas_ventas()}")
        if self.tienda.inversion_guardada:
            self.tienda.proyecta_ventas(inversion)
            print(f"El marketing ya está activado, con una inversión de {self.tienda.inversion_guardada}")
        else:
            print(f"Ventas de los últimos tres meses (se activa el marketing): {self.tienda.proyecta_ventas(inversion)}")
        print("\n")

    def da_info_ultimo_mes(self, tienda_b, tienda_c):
        """"imprime la información sobre el último mes de la tienda elegida, junto a dos más (hay que incorporar las instancias como argumentos)"""
        print(f"Si comparamos el último mes de {self.tienda.nombre} con otras dos tiendas:")
        for tienda in (self.tienda, tienda_b, tienda_c):
            print(f"- {tienda.nombre} ha tenido unas ventas de {tienda.calcula_ultimas_ventas()}{self.marketing if tienda.marketing == True else self.sin_marketing}")
            if "avenida" in tienda.direccion.lower():
                print(f"Por cierto, {tienda.nombre} se encuentra en una avenida")
