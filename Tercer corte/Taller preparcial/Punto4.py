class Persona:
    def __init__(self, nombre, edad, genero):
        """
        Inicializa un nuevo objeto Persona con su nombre, edad y género.
        
        :param nombre: El nombre de la persona.
        :param edad: La edad de la persona.
        :param genero: El género de la persona.
        """
        self.__nombre = nombre
        self.__edad = self.__validar_edad(edad)
        self.__genero = genero

    def __validar_edad(self, edad):
        """
        Valida que la edad sea un número positivo.
        
        :param edad: La edad a validar.
        :return: La edad si es válida, o 0 si no lo es.
        """
        if edad >= 0:
            return edad
        else:
            return 0

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = self.__validar_edad(edad)

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def esMayorDeEdad(self):
        """
        Determina si la persona es mayor de edad (mayor de 18 años).
        
        :return: True si la persona es mayor de edad, False en caso contrario.
        """
        return self.__edad > 18


# Ejemplo de uso:
persona1 = Persona("Juan", 25, "Masculino")
print("Nombre:", persona1.get_nombre())
print("Edad:", persona1.get_edad())
print("Género:", persona1.get_genero())
print("¿Es mayor de edad?:", persona1.esMayorDeEdad())

# Intentamos establecer una edad negativa
persona1.set_edad(-5)
print("Nueva edad:", persona1.get_edad())  # Debería ser 0 debido a la validación de datos
