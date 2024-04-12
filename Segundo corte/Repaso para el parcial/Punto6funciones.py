def Contar_mayusculas_y_minusculas(Cadena_str):
    Contador_minusculas = 0
    Contador_mayusculas = 0
    Indice = 0
    while Indice < len(Cadena_str):

        if Cadena_str[Indice].isupper():
            Contador_mayusculas += 1

        elif Cadena_str[Indice].islower():
            Contador_minusculas += 1
        Indice += 1
        

    print("El número de caracteres en mayúscula es: " + str(Contador_mayusculas))
    print("El número de caracteres en minúscula es: " + str(Contador_minusculas))


Contar_mayusculas_y_minusculas("The quick Brown Fox")

#Otra forma de hacerlo: 

def Contar_mayusculas_y_minusculas(Cadena_str):
    Contador_minusculas = 0
    Contador_mayusculas = 0
    Indice = 0
    while Indice < len(Cadena_str):
        if Cadena_str[Indice].isupper():
            Contador_mayusculas += 1
        elif Cadena_str[Indice].islower():
            Contador_minusculas += 1
        Indice += 1

    print("El número de caracteres en mayúscula es:", Contador_mayusculas)
    print("El número de caracteres en minúscula es:", Contador_minusculas)

Contar_mayusculas_y_minusculas("The quick Brown Fox")