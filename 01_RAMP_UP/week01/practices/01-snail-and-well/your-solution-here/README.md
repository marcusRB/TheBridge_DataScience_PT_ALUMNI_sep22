# YOUR SOLUTION HERE

#EJERCICIO 1
altura=125
a_diario=30
r_nocturno=20

dias=0
distancia=0
while distancia<altura:
    distancia=distancia+a_diario
    
    if distancia<altura:
        distancia=distancia-r_nocturno
    
    dias=dias+1
    
print('Dias =', dias)



#BONUS
altura=125
avance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
r_nocturno=20

dias=0
distancia=0
i=0
while distancia<altura:
    distancia=distancia+avance_cm[i]
    
    if distancia<altura:
        distancia=distancia-r_nocturno
    i=i+1
    dias=dias+1
    
print('Dias =', dias)
print('Max desplaamiento =', max(avance_cm))
print('Min desplaamiento =', min(avance_cm))


suma=0
cont=0
for a in avance_cm:
    suma=suma+a
    cont=cont+1
media=suma/cont
print("Media de avance =", media)



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
 
