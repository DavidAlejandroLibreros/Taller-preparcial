Altura = int(input("Ingrese el ancho que quiere que tenga su figura: "))
for i in range(0, Altura): 
    print(" " * ((Altura - 1) - i) + "*" * (i + 1))
print()



