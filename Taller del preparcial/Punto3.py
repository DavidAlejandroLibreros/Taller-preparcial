Numero_decimal= float(input("Introduce un número decimal: "))

Valor_a = abs(Numero_decimal)

if Numero_decimal == 0:
    print (0)
elif Numero_decimal > 0 :
    print("El número es positivo",end="")
    if Valor_a < 1:
        print(" y pequeño")
    elif Valor_a > 1000000:
        print(" y grande")
    else:
        print()
else: 
    print("El número es negativo",end="")
    if Valor_a < 1:
        print(" y pequeño")
    elif Valor_a > 1000000:
        print(" y grande")
    else:
        print()

