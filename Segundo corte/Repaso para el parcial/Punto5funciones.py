Numero = int(input("Ingrese un número para calcular su factorial(Debe ser entero y positivo): "))

def Calcular_factorial(Numero):
    multiplicación = 1
    for i in range(Numero,0,-1):
        multiplicación *= i 
    print(multiplicación)


Calcular_factorial(Numero)

