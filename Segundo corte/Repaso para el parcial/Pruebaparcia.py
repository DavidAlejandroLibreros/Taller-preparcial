def calcular_similitud(cadena1, cadena2):
    # Inicializar contadores
    letras_repetidas = 0
    letras_misma_posicion = 0
    
    # Recorrer cada letra de la segunda cadena
    for letra in cadena2:
        # Si la letra está en la primera cadena, aumentar el contador de letras repetidas
        if letra in cadena1:
            letras_repetidas += 1
            # Si la letra está en la misma posición en ambas cadenas, aumentar el contador de letras en la misma posición
            if cadena1.index(letra) == cadena2.index(letra):
                letras_misma_posicion += 1
    
    # Calcular la similitud
    if letras_repetidas == 0:
        similitud = 0
    else:
        similitud = letras_misma_posicion / letras_repetidas
    print(letras_repetidas)
    print(letras_misma_posicion)
    return similitud

# Ejemplo de uso
cadena1 = "ATACGGCATTA"
cadena2 = "--TCGGGATA -"
similitud = calcular_similitud(cadena1, cadena2)
print("La similitud entre las cadenas es:", similitud)