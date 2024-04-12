lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elemento_a_buscar = 5


for sublista in lista_anidada: # Bucle externo
    if elemento_a_buscar in sublista: # B´usqueda en el bucle interno
        print(f"Encontrado {elemento_a_buscar} en {sublista}")