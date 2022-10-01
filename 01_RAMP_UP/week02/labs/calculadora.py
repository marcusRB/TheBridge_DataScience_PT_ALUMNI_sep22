a=int(input(""))
operador=input(" ")
b=int(input(""))

operadores = ["+", "-", "*", "/", "//", "%" ]

def calculadora(a,b,operador,operadores):
    elif operador=="+":
        print(a+b)
    elif operador=="-":
        print(a-b)
    elif operador=="*":
        print(a*b)
    elif operador=="/":
        print(a/b)
    elif operador=="//":
        print(a//b)
    elif operador=="%":
        print(a%b)


calculadora(a,b,operador,operadores)
