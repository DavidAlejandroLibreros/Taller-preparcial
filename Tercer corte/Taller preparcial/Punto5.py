class Cuenta:
    def __init__(self, titular, saldo_inicial=0):
        """
        Inicializa una nueva cuenta bancaria con su titular y saldo inicial.
        
        :param titular: El titular de la cuenta.
        :param saldo_inicial: El saldo inicial de la cuenta (por defecto 0).
        """
        self.titular = titular
        self.saldo = saldo_inicial

    def ingresar(self, cantidad):
        """
        Ingresa una cantidad de dinero en la cuenta.
        
        :param cantidad: La cantidad a ingresar.
        """
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han ingresado {cantidad} unidades a la cuenta.")
        else:
            print("La cantidad ingresada debe ser positiva.")

    def mostrar(self):
        """
        Muestra el saldo actual de la cuenta.
        """
        print(f"El saldo actual de la cuenta de {self.titular} es: {self.saldo}")


# Ejemplo de uso:
cuenta1 = Cuenta("Juan Pérez", 1000)
cuenta1.mostrar()

cuenta1.ingresar(500)
cuenta1.mostrar()

cuenta1.ingresar(-200)  # Intentamos ingresar una cantidad negativa
cuenta1.mostrar()

cuenta1.ingresar(0)  # Intentamos ingresar una cantidad de 0
cuenta1.mostrar()
