# Defnimos la función 
def simple_calculator():

# Validamos las entradas numéricas, y volvemos a pedir las entradas hasta que sean números válidos
    a = input("Seleccione su primer entrada ")
    while a.isnumeric() == False:
        a = input("Por favor seleccione un número válido ")
    b = input("Seleccione su segunda entrada ")
    while b.isnumeric() == False:   
        b = input("Por favor seleccione un número válido ")

# Una vez que las entraddas son válidas, comenzamos con las operaciones de la calculadora
    if a.isnumeric() == True:
        if b.isnumeric() == True:
            operadores = ["+", "-", "*", "/", "//", "%"]
            a = float(a)
            b = float(b)
            operacion = input("Elija su operación ")
            resultado = 0

# Validamos la entrada de la operación, y volvemos a pedir la entrada hasta que sea una operación válida
            while operacion not in operadores:
                print("Operación no reconocida")
                operacion = input("Seleccione una operación válida ")

# Definimos la operación y los resultados 
            if operacion == "+":
                resultado = a + b
            elif operacion == "*":
                resultado = a * b
            elif operacion == "-":
                resultado = a - b
            elif operacion == "/":
                resultado = a / b

# Imprimimos el resultado
            print("El resultado es " + str(resultado))

simple_calculator()