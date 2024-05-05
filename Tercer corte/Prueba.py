import random

class Guerrero:
    def __init__(self, nombre, vida, fuerza, precision, velocidad, defensa):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.precision = precision
        self.velocidad = velocidad
        self.defensa = defensa

    def golpear(self, g):
        # Comprueba si el golpe acierta
        if random.random() <= (self.precision - g.velocidad) / 100:
            # En caso de acertar, resta vida al oponente
            g.vida -= max([(self.fuerza - g.defensa) + random.randrange(-10, 11), 1])
            print("Golpe certero de", self.nombre)
        else:
            print(g.nombre, "esquiva el golpe!")

# Función que simula la batalla entre dos guerreros
def simular_batalla(j1, j2):
    # Comienza el jugador más veloz
    golpeador, receptor = j1, j2
    if j1.velocidad < j2.velocidad:
        golpeador, receptor = j2, j1
    # Se golpean hasta que alguno tenga vida cero
    while j1.vida > 0 and j2.vida > 0:
        print("\n" + j1.nombre, j1.vida, "vs", j2.vida, j2.nombre)
        golpeador.golpear(receptor)
        # Cambio de turnos
        golpeador, receptor = receptor, golpeador
    # Fin de la batalla
    print("\n" + j1.nombre, j1.vida, "vs", j2.vida, j2.nombre)
    print("Ganador:", receptor.nombre)

# Creamos objetos y simulamos una batalla
superman = Guerrero('Superman', 100, 50, 80, 30, 20)
goku = Guerrero('Gokú', 100, 60, 80, 40, 20)
chuck = Guerrero('Chuck Norris', 200, 99, 99, 99, 99)

# Simulamos la batalla entre Goku y Chuck Norris
simular_batalla(goku, chuck)
