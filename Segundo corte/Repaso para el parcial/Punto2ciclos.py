parrafo = "Hola mundo"

# Inicializamos el contador de palabras
contador_palabras = 0

# Inicializamos el índice para recorrer el párrafo
indice = 0

# Mientras haya caracteres en el párrafo
while indice < len(parrafo):
    # Ignoramos los espacios en blanco al inicio de una palabra
    while indice < len(parrafo) and parrafo[indice] == ' ':
        indice += 1
    
    # Si todavía hay caracteres en el párrafo, aumentamos el contador de palabras
    if indice < len(parrafo):
        contador_palabras += 1
    
    # Avanzamos al siguiente espacio en blanco o al final del párrafo
    while indice < len(parrafo) and parrafo[indice] != ' ':
        indice += 1

# Imprimimos el número total de palabras
print("El número total de palabras en el párrafo es:", contador_palabras)
print(indice)
