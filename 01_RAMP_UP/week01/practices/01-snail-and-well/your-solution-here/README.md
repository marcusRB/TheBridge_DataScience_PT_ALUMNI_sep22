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
 
##Bonus
avance_cm=[30,21,33,77,44,45,23,45,12,55]

min(avance_cm)

max(avance_cm)

sum(avance_cm)

len(avance_cm)

sum(avance_cm)/len(avance_cm)

from math import sqrt
from multiprocessing.resource_sharer import stop
from unittest import result
 
def media(avance_cm):
  s = 0
  for elemento in avance_cm:
    s += elemento
  return s / float(len(avance_cm))


altura_max = 125
avance_diario = 30 
retroceso_noche = -20 
distancia_acumulada = 0
dias = 0 

while distancia_acumulada < altura_max:
  distancia_acumulada += avance_diario
  dias +=1
  print(dias)
  print(distancia_acumulada)
while distancia_acumulada < altura_max:
   distancia_acumulada += retroceso_noche
   dias +=1
   print(dias) 
   print(distancia_acumulada)




##No consigo meter la segunda variable de que cada vez que suba 30 y no haya salido del pozo reste 20
 ## pero seguiria así, siempre que sume 30 y no supere la altura del pozo que le reste 20, una vez que la altura inicial sea mayor que la del pozo que rompa el bucle


