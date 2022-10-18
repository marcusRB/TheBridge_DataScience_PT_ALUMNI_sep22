import utils

gonzalez = utils.Tienda ("Hermanos González", "c/ Argumosa, 10. Madrid", 3, [12000, 6000, 32432])
maricarmen = utils.Tienda ("Electro Mari Carmen", "Avenida Grande, 4. Bollullos de la Mitación", 8, [23176, 2134, 70375])
cari = utils.Tienda ("Carimesticos", "Plaza de Enmedio, s/n. Teruel", 2, [6578, 1200, 19456])

print(cari.total_ventas())
print(cari.media_ventas_empleado())
print(cari.tienda_direccion())
print(cari.ventas_ultimo_mes())
print(cari.proyeccion_ventas (500))