# Importamos el módulo con los métodos para los input del usuario
import utils

print("Simple calculator!")
# Creamos la variable con las opciones posibles de cálculo
operadores = ["+", "-", "*", "/"]

# Solicitamos al usuario que introduzca el prime3r número, el operador y el segundo número
a = utils.inputNumero ("Introduce el primer número: ")
o = utils.seleccionaOperador (operadores)
b = utils.inputNumero ("Introduce el segundo número: ")

# Inicializamos la variable que almacenará el resultado de la operación
resultado = 0

# Realiza el cálculo e imprime por pantalla el resultado
if o == "+":
    resultado = a+b
    print(f"El resultado de {a} mas {b} es: {resultado}")
elif o == "-":
    resultado = a-b
    print(f"El resultado de {a} menos {b} es: {resultado}")
elif o == "*":
    resultado = a*b
    print(f"El resultado de {a} por {b} es: {resultado}")
else:
    resultado = a/b
    print(f"El resultado de {a} dividido entre {b} es: {resultado}")

