num_filas = int(input("Ingresa el número de filas: "))


for i in range(1, num_filas + 1):

    print(" " * (num_filas - i), end="")

    for j in range(i, i * 2):

        print(j % 10, end="")
    
    for j in range(i * 2 - 2, i - 1, -1):

        print(j % 10, end="")
    
    print()