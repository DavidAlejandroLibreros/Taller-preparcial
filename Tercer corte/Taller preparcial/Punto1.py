class Coche:
    def __init__(self, matricula, marca, kilometros, gasolina):
        """
        Inicializa un nuevo objeto Coche con los atributos proporcionados.
        
        :param matricula: Matrícula del coche.
        :param marca: Marca del coche.
        :param kilometros: Kilómetros recorridos por el coche.
        :param gasolina: Cantidad de gasolina en el coche.
        """
        self.matricula = matricula
        self.marca = marca
        self.kilometros = kilometros
        self.gasolina = gasolina
    
    def avanzar(self, km):
        """
        Permite que el coche avance una cierta cantidad de kilómetros.
        Resta la cantidad de gasolina correspondiente según los kilómetros recorridos.
        Asumimos que el coche consume 1 litro de gasolina por cada 10 kilómetros.

        :param km: Kilómetros a recorrer.
        """
        consumo = km / 10  # Consumo de gasolina (1 litro por cada 10 km)
        
        if self.gasolina >= consumo:
            self.kilometros += km
            self.gasolina -= consumo
            print(f"El coche ha avanzado {km} kilómetros. Gasolina restante: {self.gasolina} litros.")
        else:
            print("No hay suficiente gasolina para avanzar. Repostar antes de intentar avanzar.")
    
    def repostar(self, litros):
        """
        Añade gasolina al coche.

        :param litros: Cantidad de litros de gasolina a añadir.
        """
        if litros > 0:
            self.gasolina += litros
            print(f"Se han añadido {litros} litros de gasolina. Gasolina total: {self.gasolina} litros.")
        else:
            print("La cantidad de gasolina a añadir debe ser positiva.")

# Ejemplo de uso:
mi_coche = Coche("ABC123", "Toyota", 50000, 10)

mi_coche.avanzar(50)  # Debería restar 5 litros de gasolina y aumentar los kilómetros recorridos a 50050.
mi_coche.repostar(10)  # Debería añadir 10 litros de gasolina.
mi_coche.avanzar(200)  # Debería restar 20 litros de gasolina y aumentar los kilómetros recorridos a 50250.
mi_coche.repostar(-5)  # Debería mostrar un mensaje de error.
mi_coche.avanzar(500)  # Debería mostrar un mensaje de error si no hay suficiente gasolina.
