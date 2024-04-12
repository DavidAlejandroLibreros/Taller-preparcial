def Funcion_para_hallar_máximo_de_tres_numeros():
    Num_1 = int(input("Ingrese el primer número: "))
    Num_2 = int(input("Ingrese el segundo número: "))
    Num_3 = int(input("Ingrese el tercer número: "))
    if Num_1 > Num_2 and Num_1 > Num_3 :
        print("El número más grande es: " + str(Num_1))
    elif Num_2 > Num_1 and Num_2 > Num_3:
        print("El número mas grande es: " + str(Num_2))
    else:
        print("El número mas grande es: " + str(Num_3))


Funcion_para_hallar_máximo_de_tres_numeros()