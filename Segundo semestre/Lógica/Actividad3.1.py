def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n -1)
    

n = input("Ingrese un número: ")
n = int(n)

print("El suma es: ",  suma(n))    