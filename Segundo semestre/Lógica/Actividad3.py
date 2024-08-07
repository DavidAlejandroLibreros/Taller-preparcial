def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
n = input("Ingrese un número: ")
n = int(n)

print("El factorial es: ",  factorial(n))