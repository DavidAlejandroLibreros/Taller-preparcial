def similarity(Cadena1, Cadena2):
    Lista_mayusculas = ["T", "C", "G", "A"]
    letras_mayusculas_unicas = 0
    # Determinar la longitud de la cadena más pequeña
    min_longitud = min(len(letras_mayusculas_unicas), len(Cadena2))
    # Contador para letras que coinciden en la misma posición en ambas cadenas
    coincidencias = sum(1 for char1, char2 in zip(Cadena1, Cadena2) if char1 == char2)
    # Calcular el índice de similitud
    S = coincidencias / min_longitud
    print("Índice de similitud:", S)
    print(coincidencias)
    print(min_longitud)
# Ejemplo de uso
Cadena1 = "ATACGGCATTA"
Cadena2 = "--TCGGGATA- "
similarity(Cadena1, Cadena2)