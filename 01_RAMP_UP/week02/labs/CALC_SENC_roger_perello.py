"""Palabras de presentación"""
def saluda():
    print("¡Esta es una calculadora simple!")


"""Pregunta los números sin usar try-except"""
def pregunta():
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7" , "8", "9", "."]
    comprobacion = []
    while True:
        valor = input("Introduce un valor: ")
        for digit in valor:
            if digit not in numeros:
                comprobacion.append(digit)
            elif digit == ".":
                numeros.pop(-1)
        if len(comprobacion) == 1 or valor == ".":
            print("Se ha detectado un carácter erróneo")
        elif len(comprobacion) == 0:
            return valor
        else:
            print(f"Se han detectado {len(comprobacion)} caracteres erróneos: {''.join(comprobacion)}")
        comprobacion = []
        numeros = ["0", "1", "2", "3", "4", "5", "6", "7" , "8", "9", "."]


"""Pregunta por el operador"""
def pregunta_operador():
    operadores = ["+", "-", "*", "/", "//", "%"]
    while True:
        operador = input("¿Qué operación quieres realizar (+, -, *, /, // o %)? ")
        if operador in operadores:
            print("¿Con qué otro número deseas operar?")
            return operador
        else:
            print("Este no es un operador válido")


"""Empareja los números con su operador y devuelve una string"""
def calcula(simbolo):
    return f"float(a) {simbolo} float(b)"


"""Imprime el resultado final al evaluar la string de calcula()"""
def nombra(resultado, a, b, simb):
    print(f"{a} {simb} {b} es igual a {eval(resultado)}")


"""Agrupa todas demás las funciones"""
def inicia():
    saluda()
    val_a = pregunta()
    operad = pregunta_operador()
    val_b = pregunta()
    calculo = calcula(operad)
    nombra(calculo, val_a, val_b, operad)


"""Pone en marcha el programa"""
inicia()
