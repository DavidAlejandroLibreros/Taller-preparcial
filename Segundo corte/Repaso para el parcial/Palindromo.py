print("Verificador de Palindromo ")

palabra = input("Verificador de Palindromo ")


palabra_inversa = ""

for i in range(len(palabra)-1,-1,-1):
    palabra_inversa = palabra_inversa + palabra[i]


if palabra_inversa == palabra:
    print(True)
else:
    print(False)
    