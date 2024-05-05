import random

class Pokemon:
    def __init__(self, Nombre, Puntos_de_salud, Ataque, Defensa, Ataque_especial, Defensa_especial, Velocidad, Tipo):
        self.Nombre = Nombre
        self.Puntos_de_salud = Puntos_de_salud
        self.Ataque = Ataque
        self.Defensa = Defensa
        self.Ataque_especial = Ataque_especial
        self.Defensa_especial = Defensa_especial
        self.Velocidad = Velocidad
        self.Tipo = Tipo

    def golpear(self, P):
        if (random.random() <= (self.Velocidad - P.Velocidad) / 100):
            P.Puntos_de_salud -= max([(self.Ataque - P.Defensa) + random.randrange(-10, 11), 1])
            print("Golpe certero de", self.Nombre)
        else:
            print(P.Nombre, "esquiva el golpe!")

def Simular_batalla_pokemon(j1, j2):
    # Comprueba el Pokémon con mayor velocidad
    Atacante, Receptor = j1, j2
    if j1.Velocidad < j2.Velocidad:
        Atacante, Receptor = j2, j1
    # Realiza el combate hasta que alguno se quede sin vida
    while j1.Puntos_de_salud > 0 and j2.Puntos_de_salud > 0:
        print("\n" + j1.Nombre, j1.Puntos_de_salud, "vs", j2.Puntos_de_salud, j2.Nombre)
        Atacante.golpear(Receptor)
        # Cambio de turnos
        Atacante, Receptor = Receptor, Atacante
    # Fin de los turnos
    print("\n" + j1.Nombre, j1.Puntos_de_salud, "vs", j2.Puntos_de_salud, j2.Nombre)
    print(Atacante.Nombre + " está fuera de combate. El ganador es: " + Receptor.Nombre)

Bulbasaur = Pokemon("Bulbasaur", 45, 49, 49, 65, 65, 45, "Planta")
Charmander = Pokemon("Charmander", 39, 52, 43, 60, 50, 65, "Fuego")
Squirtle = Pokemon("Squirtle", 44, 48, 65, 50, 64, 43, "Agua")
Pikachu = Pokemon("Pikachu", 35, 55, 40, 50, 50, 90, "Eléctrico")
Metapod = Pokemon("Metapod", 50, 20, 55, 25, 25, 30, "Bicho")

Simular_batalla_pokemon(Charmander, Pikachu)

