# Importa la función choice del módulo random
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
from random import choice

def combate(pc:str, player:str):
    if pc == 'piedra':
        if player == 'piedra':
            return 0
        elif player == 'papel':
            return 2
        elif player == 'tijeras':
            return 1
    elif pc == 'papel':
        if player == 'piedra':
            return 1
        elif player == 'papel':
            return 0
        elif player == 'tijeras':
            return 2
    elif pc == 'tijeras':
        if player == 'piedra':
            return 2
        elif player == 'papel':
            return 1
        elif player == 'tijeras':
            return 0

def opcionPC(listaOpciones:list):
    return choice(listaOpciones)

def opcionJugador(listaOpciones:list):
    opcionPlayer = input("Elija opción entre piedra, papel o tijeras:")
    while opcionPlayer not in listaOpciones:
        print("La elección no está entre las posibles.")
        opcionPlayer = input("Elija opción entre piedra, papel o tijeras: ")
    return opcionPlayer

def estadoPartida(eleccMaquina, eleccUsuario, result):
    global partidasJugadas, ganadasMaquina, ganadasUsuario
    if result == 0:
        partidasJugadas += 1
        print("La máquina eligió: ", eleccMaquina, ". El jugador eligió: ", eleccUsuario, ". El resultado es: EMPATE")
        print("El estado de la partida es Máquina: ", ganadasMaquina, ". Jugador: ", ganadasUsuario)
    elif result == 1:
        partidasJugadas += 1
        ganadasMaquina += 1
        print("La máquina eligió: ", eleccMaquina, ". El jugador eligió: ", eleccUsuario, ". El resultado es: GANA LA MÁQUINA")
        print("El estado de la partida es Máquina: ", ganadasMaquina, ". Jugador: ", ganadasUsuario)
    elif result == 2:
        partidasJugadas += 1
        ganadasUsuario += 1 
        print("La máquina eligió: ", eleccMaquina, ". El jugador eligió: ", eleccUsuario, ". El resultado es: GANA EL USUARIO")
        print("El estado de la partida es Máquina: ", ganadasMaquina, ". Jugador: ", ganadasUsuario)
    return 0
        
# Asigna a una lista las 3 posibles opciones: 'piedra', 'papel' o 'tijeras'. 

# Asigna una variable al número de partidas máxima: 1, 3, 5, etc...

# Asigna una variable al número de partidas que debe ganar un jugador para ganar. 
# Preferiblemente el valor será en función de el número de partidas máximas

# Define una función que devuelva aleatoriamente una de las 3 opciones. 
# Esto corresponderá a la jugada de la máquina. Totalmente aleatoria. 

# Define una función que pregunte tu elección: 'piedra', 'papel' o 'tijeras'
# sólo debe permitir una de las 3 opciones. Esto es programación defensiva. 
# Si no es piedra, papel o tijeras sigue preguntando hasta que lo sea. 

# Define una función que resuelva un combate. 
# Devuelve 0 si hay empate, 1 si gana la máquina, 2 si gana el jugador humano 

# Define una función que muestre la elección de cada jugador y el estado de la partida
# Esta función debe utilizarse cada vez que se actualicen los puntos acumulados

# Crea dos variables que acumulen las partidas ganadas de cada participante

# Crea un bucle que itere mientras ningún jugador alcance el mínimo de victorias
# necesarias para ganar. Dentro del bucle resuelve la jugada de la
# máquina y pregunta la del jugador. Comparalas y actualiza el valor de las variables
# que acumulen las partidas ganadas de cada participante. 

# Anuncia por consola el ganador del juego en función de quién tiene más victorias 
# aculumadas

opciones = ['piedra', 'papel', 'tijeras']
partidasJugadas = 0
ganadasMaquina = 0
ganadasUsuario = 0

numPartidas = input("Introduzca nº de partidas. Debe ser impar: ")
## Comprobamos que el valor introducido es un número, entero e impar.
while True:
    try:
        partidas = int(numPartidas)
        if partidas%2 == 0:
            numPartidas = input("ERROR. Introduzca un nº impar de partidas: ")
        else:
            break
    except ValueError:
        numPartidas = input("ERROR. Introduzca un número entero impar de partidas: ")

## Se deben ganar la mitad de las partidas más una.
numVictorias = round(int(numPartidas)/2,0)+1

while (ganadasMaquina<numVictorias) and (ganadasUsuario<numVictorias) and (partidasJugadas<int(numPartidas)):
    
    jugadaMaquina = opcionPC(opciones)
    jugadaUsuario = opcionJugador(opciones)
    resultado = combate(jugadaMaquina, jugadaUsuario) 
    estadoPartida(jugadaMaquina, jugadaUsuario, resultado)

if ganadasMaquina > ganadasUsuario:
    print("GANA LA MÁQUINA")
elif ganadasUsuario > ganadasMaquina:
    print("GANA EL USUARIO")
else:
    print("EMPATE")