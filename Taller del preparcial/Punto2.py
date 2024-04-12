Numero1 = int(input("Introduzca el primero número: "))
Numero2 = int(input("Introduzca el segundo número: "))
Numero3 = int(input("Introduzca el tercer número: "))

if Numero1 > Numero2 or Numero1 > Numero3:
    print(Numero1)
elif Numero2 > Numero3:
    print(Numero2)
else: 
    print(Numero3)