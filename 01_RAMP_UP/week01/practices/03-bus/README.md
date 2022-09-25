# Bus

Este bus tiene un sistema de control de subida y bajada de pasajeros para monitorizar el número de ocupantes que lleva y así detectar cuando hay un aforo demasiado alto. 

En cada parada la subida y bajada de pasajeros se representa por una tupla compuesta por dos números enteros. 
```
bus_stop = (in, out)
```
La sucesión de paradas se representa con una lista estas tuplas.
```
stops = [(in1, out1), (in2, out2), (in3, out3), (in4, out4)]
```

## Objetivos: 
* listas, tuplas
* bucles while/for
* mínimo, máximo, longitud
* media, desviación estandard

## Tareas
1. Calcula el número de paradas. 
2. Asigna a una variable una lista cuyos elementos sean el número de pasajeros en cada parada (in-out), 
3. Halla el máximo de ocupación del autobús. 
4. Calcula la media de la ocupación. Y la desviación estandard. 


stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]

numeor_paradas = len (stops)
print(numeor_paradas)

pasajeros = 0 
pasajeros_stops= []

for i in stops:
    pasajeros = pasajeros + i[0] - i[1]
    pasajeros_stops.append(pasajeros)
print ( pasajeros)
print ( pasajeros_stops)
print(max(pasajeros_stops))


