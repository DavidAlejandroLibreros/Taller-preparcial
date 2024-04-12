n = 5
for i in range(0, n): # Bucle externo
    for j in range(i+1): # Bucle interno
        print("*", end="")
    print() # Nueva l´ınea despu´es de cada fila del patr´o
for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("Otra forma de hacerlo:")

n = 5

for i in range(-(n-1), n):  # Rango desde -(n-1) hasta n-1
    num_asteriscos = n - abs(i)  # Calcular el número de asteriscos en la fila actual
    print("*" * num_asteriscos)  # Imprimir asteriscos