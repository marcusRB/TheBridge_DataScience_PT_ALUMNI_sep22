# Caracol y el pozo

Un caracol cae en el fondo de un pozo de 125 cm. Cada día el caracol sube 30 cm. pero por la noche, mientras duerme, resbala 20 cm debido a que las paredes son húmedas. ¿Cuantos días tarda en escapar del pozo?

https://www.vix.com/es/btg/curiosidades/59215/acertijos-matematicos-el-caracol-en-el-pozo-facil

## Objetivos

1. Tratamiento de variables
2. Uso de bucle **while**
3. Uso de condicionales **if-else**
4. Imprimir por consola

dia = 0
contador_cm = 0
alturapozo = 125
subidas =  30
bajadas =  20

while contador_cm < alturapozo:
  contador_cm += subidas
  contador_cm -= bajadas
  dia += 1
  print('El dia', dia, 'el caracol ha recorrido', contador_cm, 'cm')
  
  if (contador_cm + subidas)>= alturapozo:
   dia += 1
   print ('El dia', dia,'El caracol ha salido del pozo')
   break;




## Bonus
La distancia recorrida por el caracol viene ahora definida por una lista. 
```
avance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
```
¿Cuánto tarda en subir el pozo?

dia = 0
alturapozo = 125
suma = 0
lista = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]

for i in lista:
  suma = suma+i
  dia +=1
  print( "Dia",dia, ":Total de cm avanzados acumulados:", suma)
  if suma>= alturapozo:
   dia +=1
   print ("Dia",dia,':En este dia el caracol ha salido del pozo')
   break;

¿Cuál es su máximo de desplazamiento en un día? ¿Y su mínimo?

lista = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]

print("lo maximo que ha avanzado:",max(lista),"cm")
print("lo minimo que ha avanzado:",min(lista),"cm")


¿Cuál es su media de velocidad durante el día?

#calculo con Numpy
import numpy as np
lista = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
print("media: ", np.mean(lista))

#calculo manual:

sum(lista) / len(lista)

¿Cuál es la desviación típica de su desplazamiento durante el día?

import numpy as np
lista = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
print("Desviacion tipica: ", np.std(lista))
