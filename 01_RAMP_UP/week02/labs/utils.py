def inputNumero (mensaje: str):
    '''
    Solicita al usuario la introducción de un número entero o float
    Args:
        mensaje: str
    '''
    while True:
        try:
            x = float (input (mensaje))
            isinstance(x, float)
            break
        except ValueError:
            input ("Debes introducir un número ")
    return x

def seleccionaOperador (operador: list):
    '''
    Solicita al usuario la introducción de un operador válido
    Args:
        operador: list
    '''
    x = input ("Operation? ")
    while True:
        try:
            operador.index(x)
            break
        except ValueError:
            input ("No es un operador válido + - / *. Introduce uno correcto")
    return x