class GeneradorSubconjuntos:
    def __init__(self):
        """
        Inicializa un nuevo objeto GeneradorSubconjuntos.
        """
        self.subconjuntos = []

    def generar_subconjuntos(self, conjunto):
        """
        Genera todos los subconjuntos únicos del conjunto dado utilizando técnicas de recursión.
        
        :param conjunto: Lista de elementos del conjunto.
        """
        self.subconjuntos = []  # Reiniciamos la lista de subconjuntos
        
        # Llamamos a la función recursiva para generar subconjuntos
        self._generar_subconjuntos_recursivo(conjunto, [], 0)
        
    def _generar_subconjuntos_recursivo(self, conjunto, actual, indice):
        """
        Función auxiliar recursiva para generar subconjuntos únicos.
        
        :param conjunto: Lista de elementos del conjunto.
        :param actual: Lista actual de elementos del subconjunto.
        :param indice: Índice actual en el conjunto.
        """
        # Añadimos el subconjunto actual a la lista de subconjuntos
        self.subconjuntos.append(actual)
        
        # Iteramos sobre los elementos restantes del conjunto
        for i in range(indice, len(conjunto)):
            # Generamos un nuevo subconjunto incluyendo el elemento en la posición i
            self._generar_subconjuntos_recursivo(conjunto, actual + [conjunto[i]], i + 1)

    def total_subconjuntos(self):
        """
        Calcula la cantidad total de subconjuntos generados.
        
        :return: La cantidad total de subconjuntos.
        """
        return len(self.subconjuntos)
    
    def longitud_promedio(self):
        """
        Calcula la longitud promedio de los subconjuntos generados.
        
        :return: La longitud promedio de los subconjuntos.
        """
        total_elementos = sum(len(subconjunto) for subconjunto in self.subconjuntos)
        return total_elementos / len(self.subconjuntos) if self.subconjuntos else 0

# Ejemplo de uso:
generador = GeneradorSubconjuntos()
generador
