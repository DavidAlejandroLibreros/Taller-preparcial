def similarity(Cadena1, Cadena2):
    Lista_mayusculas = ["T", "C", "G", "A"]
    # Calcular la longitud de la cadena más corta
    longitud_min = min(sum(1 for char in Cadena1 if char in Lista_mayusculas),
                       sum(1 for char in Cadena2 if char in Lista_mayusculas))
    
    # Contador para letras que coinciden en la misma posición en ambas cadenas
    coincidencias = sum(1 for char1, char2 in zip(Cadena1, Cadena2) if char1 == char2 and char1 in Lista_mayusculas)
    
    # Calcular el índice de similitud
    S = coincidencias / longitud_min 
    
    print("Índice de similitud:", S)

# Ejemplo de uso
Cadena1 = "ATACGGCATTA"
Cadena2 = "--TCGGGATA- "
similarity(Cadena1, Cadena2)


#Ahora con las otras cadenas:

Cadena1 = "ATACGGCATTA" 
Cadena2 = "TCGGGATA ---"

similarity(Cadena1, Cadena2)
