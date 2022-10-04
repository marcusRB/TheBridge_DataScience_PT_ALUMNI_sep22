# Robin Hood: 
Estamos en plena competición para ganar el concurso de tiro con arco en Sherwood. Con nuestro arco y flechas disparamos sobre una diana e intentamos acertar lo más posible del centro. 

El centro de la diana viene representado por los valores (0, 0) en los ejes de coordenadas. 

## Objetivos: 
* estructuras de datos: listas, conjuntos, tuplas
* operadores lógicos: if-elif-else
* bucle: while/for
* cálculo de mínimo (sorting opcional)

## Descripción: 
En el espacio de 2 dimensiones un punto se puede definir por un par de valores que corresponden a la coordenada horizontal (x) y a la vertical (y). El espacio puede quedar dividido en 4 zonas (cuadrantes): Q1, Q2, Q3, Q4. Cuyo punto de unión único es el punto (0, 0). 

Si un punto se encuentra en Q1 tanto su coordenada x como la y son positivas. Te dejo un enlace a wikipedia para que te familiarices con estos cuadrantes. 

https://es.wikipedia.org/wiki/Coordenadas_cartesianas

https://es.wikipedia.org/wiki/Distancia_euclidiana

## Tareas
1. Robin Hood es famoso por acertar a una flecha con otra flecha. ¿Lo ha conseguido? 
2. Calcula cuántos flechazos han caido en cada cuadrante. 
3. Halla el punto más cercano al centro. Calcula su distancia al centro
4. Si la diana tiene un radio de 9, calcula el número de flechas que hay que recoger al bosque. 
puntos = [(4,5), (-0,2), (4,7), (1,-3), (3,-2), (4,5), 
          (3,2), (5,7), (-5,7), (2,2), (-4,5), (0,-2), 
          (-4,7), (-1,3), (-3,2), (-4,-5), (-3,2), 
          (5,7), (5,7), (2,2), (9, 9), (-8, -9)]
        

Q1 = []
Q2 = []
Q3 = []
Q4 = []
flechas_caidas = 0
distancias = []
tiros_cercanos = []

if len(set(puntos)) < len(puntos):
    acierto = "Robin Hood ha acertado una flecah contra otra."
else:
    acierto = "Robin Hood no ha acertado una flecha contra otra"

for tiro in puntos:
    if tiro [0] > 0 and tiro [1] > 0:
        Q1.append(tiro)
    elif tiro [0] < 0 and tiro [1] > 0:
        Q2.append(tiro)
    elif tiro [0] < 0 and tiro [1] < 0:
        Q3.append(tiro)
    elif tiro [0] < 0 and tiro [1] < 0:
        Q4.append(tiro)
    distancias.append((round((tiro[0] ** 2 *+ tiro[1]**2)**0.5, 2), tiro))

distancias.sort()
mejor_distancia = distancias [0][0]

for distancias_y_tiro in distancias:
    if distancias_y_tiro[0] == mejor_distancia:
        tiros_cercanos.append(distancias_y_tiro[1])
    if distancias_y_tiro[0] > 9:
        flechas_caidas += 1 
print(F"""{acierto}
Flechazos por cuadrante : Q1 = {len(Q1)}, Q2 = {len(Q2)}, Q3 = {len(Q3)}, Q4 = {len(Q4)}
Los puntos más cercanos al centro : {tiros_cercanos}, con una distancia de {mejor_distancia}
Un total de {flechas_caidas} flechas han caido uera de la diana
""")