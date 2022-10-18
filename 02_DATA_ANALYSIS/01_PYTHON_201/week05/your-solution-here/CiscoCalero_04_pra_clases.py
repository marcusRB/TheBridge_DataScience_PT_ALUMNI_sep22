import utils

gonzalez = utils.Tienda ("Hermanos González", "c/ Argumosa, 10. Madrid", 3, [12000, 6000, 32432])
maricarmen = utils.Tienda ("Electro Mari Carmen", "Avenida Grande, 4. Bollullos de la Mitación", 8, [23176, 2134, 70375])
cari = utils.Tienda ("Carimesticos", "Avenida de Enmedio, s/n. Teruel", 2, [6578, 1200, 19456])

print(cari.total_ventas())
print(cari.media_ventas_empleado())
print(cari.tienda_direccion())
print(cari.ventas_ultimo_mes())
print(cari.proyeccion_ventas (500))


tiendas = [gonzalez, maricarmen, cari]

total_ventas = 0
for i in range(len(tiendas)):
    total_ventas += tiendas[i].ventas_ultimo_mes()
print("El total de ventas del último mes es de: {}".format (total_ventas))

for i in range(len(tiendas)):
    if "Avenida" in tiendas[i].direccion:
        print("La tienda {} está en una avenida".format(tiendas[i].nombre))
