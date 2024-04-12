print("Verificador de Palindromo ")

palabra = input("Verificador de Palindromo ")


palabra_inversa = ""

for i in range(len(palabra)-1,-1,-1):
    palabra_inversa = palabra_inversa + palabra[i]

if palabra_inversa == palabra:
    print(True)
else:
    print(False)



#Otra forma:

def es_palindromo(cadena):
    # Convertir la cadena a minúsculas y eliminar espacios y signos de puntuación
    cadena_procesada = ''.join(caracter.lower() for caracter in cadena if caracter.isalnum())

    # Verificar si la cadena procesada es igual a su inversa
    return cadena_procesada == cadena_procesada[::-1]

# Ejemplos de uso
cadena1 = "Anita lava la tina"
cadena2 = "12321"
cadena3 = "Hola Mundo"

print(es_palindromo(cadena1))  # True
print(es_palindromo(cadena2))  # True
print(es_palindromo(cadena3))  # False