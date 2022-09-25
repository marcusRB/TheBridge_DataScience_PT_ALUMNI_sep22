from random import choice

# Define una función que devuelva aleatoriamente una de las 3 opciones. 
def jugadaMaquina (opcionesAleatorias):
    """
    Devuelve un elemento aleatorio de una lista.

    Args: 
        opcionesAleatorias (List)

    Returns:
        string
    """
    tiro_maquina = choice(opcionesAleatorias)
    return tiro_maquina

# Define una función que pregunte tu elección: 'piedra', 'papel' o 'tijeras'
def jugadaHumano (opcionesAleatorias):
    """
    Solicita una entrada al usuario válida

    Args: 
        opcionesAleatorias (string)

    Returns:
        string
    """
    tiro_humano = input("Tu turno")
    while True:
        try:
            opcionesAleatorias.index(tiro_humano)
            break
        except ValueError:
            tiro_humano = input("Tu opción no es correcta, vuelva a introducirla: ")
    return tiro_humano

# Define una función que resuelva un combate
# Devuelve 0 si hay empate, 1 si gana la máquina, 2 si gana el jugador humano 
def combate (maquina, humano, combinaciones):
    """
    Resuelve el resultado de una partida entre dos opciones basado en una lista
    con las combinaciones ganadoras

    Args: 
        maquina: string
        humano: string
        combinaciones: list

    Returns:
        integer
    """
    combinacion_m_h = (maquina, humano)
    combinacion_h_m = (humano, maquina)
    if combinacion_m_h in combinaciones:
        return 1
    elif combinacion_h_m in combinaciones:
        return 2
    else:
        return 0

# Define una función que muestre la elección de cada jugador y el estado de la partida
def estadoPartida (maquina, humano):
    """
    Imprime por pantalla los argumentos de entrada

    Args: 
        maquina (string)
        humano (string)

    """
    print (f"La máquina ha seleccionado: {maquina}")
    print (f"Tu has seleccionado: {humano}")