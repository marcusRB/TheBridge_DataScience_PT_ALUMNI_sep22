# YOUR SOLUTION HERE

Instrucciones para las prácticas

## MAIN TASK
- Actualiza tu repositorio remoto *upstream/master* sincronizado con el *original/master* que hiciste el fork
- Actualiza tu repositorio local o en caso que sea CLONE ya viene actualizado
- crea tu código o ficheros en la misma carpeta <your-code> o <your-solution-here> con Visual Studio Code u otro editor (Jupyter)
- es aconsejable crear una rama DEV, sucesivamente sube el contenido (sin modificar el resto de carpetas)
- realizar un **MERGE** con tu rama *master*
- solicita un **PULL REQUEST** al principal y deja un comentario

## EVALUATION

La práctica será verificada y se dejará un feedback. Finalmente se enviará una notificación de:

- ACEPTADA
- REQUEST CHANGES
- COMMENTS
- APPROVE 0REVIEW

según la situación que sea no se aceptará una **PULL REQUEST** para no alterar la estructura del repositorio original, por lo tanto se procederá con el cierre!
 
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