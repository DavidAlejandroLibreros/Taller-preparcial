# Solicitar al usuario el número de filas para el triángulo de Pascal
numero_filas = int(input("¿Hasta qué fila quieres que se imprima el triángulo de Pascal? "))

# Inicializar la lista que contendrá el triángulo de Pascal
triangulo = []

# Generar el triángulo de Pascal
for _ in range(numero_filas):
    # En cada iteración del bucle creamos una nueva lista que representa una fila del triángulo
    # Inicializamos cada fila con un solo elemento, que siempre es 1
    fila = [1]
    # Añadimos la fila recién creada a la lista del triángulo
    triangulo.append(fila)

# Generar el resto del triángulo de Pascal
for i in range(1, numero_filas):
    # Iteramos sobre cada fila del triángulo, empezando desde la segunda fila (índice 1)
    for j in range(1, i):
        # Calculamos el valor del elemento actual sumando los elementos correspondientes de la fila anterior
        valor = triangulo[i - 1][j] + triangulo[i - 1][j - 1]
        # Añadimos el valor calculado a la fila actual del triángulo
        triangulo[i].append(valor)
    
    # Añadimos el último elemento (siempre es 1) a la fila actual del triángulo
    triangulo[i].append(1)

# Calcular la cantidad máxima de espacios necesarios para centrar el triángulo de Pascal
# La máxima cantidad de espacios es igual al doble del número de filas menos 1
espacios_maximos = numero_filas * 2 - 1

# Imprimir el triángulo de Pascal en forma de pirámide
for i in range(len(triangulo)):
    # Calcular la cantidad de espacios antes de cada fila para centrar la pirámide
    # La cantidad de espacios es igual a la mitad de los espacios máximos menos la mitad del tamaño de la fila actual, redondeado hacia abajo
    espacios = " " * ((espacios_maximos - (i * 2 - 1)) // 2)
    
    # Imprimir los espacios antes de los números de la fila para centrar la pirámide
    print(espacios, end="")
    
    # Iterar sobre los números de la fila actual del triángulo
    for j in range(len(triangulo[i])):
        # Imprimir cada número de la fila actual seguido de un espacio en blanco
        print(triangulo[i][j], end=" ")
    
    # Salto de línea al final de cada fila del triángulo para pasar a la siguiente fila
    print()