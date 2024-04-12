Altura = int(input("Ingrese la altura que quiere que tenga su rectángulo: "))
Ancho = 10

for i in range(0,Altura):
    if i == 0 or i == (Altura - 1):
        print("*" * Ancho)
    else:
        print("*" + " " * (Ancho - 2) + "*")
