
Num_letras = 0
Num_digitos = 0
Num_espacios = 0
Num_letras_mayusculas = 0
Num_caracteres_especiales = 0

Inicio = print("Se va a calcular los caracteres de esta frase: This is w3resource.com")
cadena = "This is w3resource.com"
Num_caracteres_totales = len(cadena)
Numeros = ["1","2","3","4","5","6","7"]
Caracteres_especiales = ["!", ".", ",", "/","%", "&"]
for i in cadena:
    if i > "A":
        Num_letras_mayusculas += 1
    if i == " ":
        Num_espacios += 1
for i in cadena:
    if i in Numeros:
        Num_digitos +=1
    if i in Caracteres_especiales:
        Num_caracteres_especiales += 1

print(Num_letras_mayusculas)
print("El número de caracteres en la cadena es:" + str(Num_caracteres_totales))
print("El número de letras es:" + str(Num_letras_mayusculas))
print("El número de dígitos es:" + str(Num_digitos))
print("El número de espacios es:" + str(Num_espacios))
print("El número de otros caracteres es: " + str(Num_caracteres_especiales))
