# Imprimir un patr´on simple
n = 5
for i in range(n): # Bucle externo
    for j in range(i+1): # Bucle interno
        print("* ", end="")
    print() # Nueva l´ınea despu´es de cada fila del patr´on