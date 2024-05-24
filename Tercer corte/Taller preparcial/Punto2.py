class Alumno:
    def __init__(self, nombre, calificaciones):
        """
        Inicializa un nuevo objeto Alumno con su nombre y calificaciones.
        
        :param nombre: El nombre del alumno.
        :param calificaciones: Un diccionario donde las claves son los nombres de las asignaturas y los valores son las calificaciones.
        """
        self.nombre = nombre
        self.calificaciones = calificaciones

    def mostrar_datos(self):
        """
        Muestra el nombre del alumno y sus calificaciones.
        """
        print("Nombre del alumno:", self.nombre)
        print("Calificaciones:")
        for asignatura, calificacion in self.calificaciones.items():
            print(f"{asignatura}: {calificacion}")

    def calcular_nota_final(self):
        """
        Calcula la nota final del alumno basada en sus calificaciones.
        
        La nota final se calcula como el promedio de todas las calificaciones.
        """
        if not self.calificaciones:  # Si el alumno no tiene calificaciones
            return "No hay calificaciones para calcular la nota final"
        
        promedio = sum(self.calificaciones.values()) / len(self.calificaciones)
        
        if promedio >= 3.0:  # Si el promedio es mayor o igual a 3.0
            return "Aprobado"
        else:
            return "Reprobado"

# Ejemplo de uso:
calificaciones_juan = {"Matemáticas": 4.5, "Historia": 3.0, "Ciencias": 3.8}
juan = Alumno("Juan", calificaciones_juan)

juan.mostrar_datos()
print("Resultado:", juan.calcular_nota_final())
