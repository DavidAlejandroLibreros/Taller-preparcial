def Pot2(n):
    if n == 0:
        return 1
    else:
        return 2 * Pot2(n -1)
    

n = input("Ingrese un número: ")
n = int(n)

print("La potencia es: ",  Pot2(n))    