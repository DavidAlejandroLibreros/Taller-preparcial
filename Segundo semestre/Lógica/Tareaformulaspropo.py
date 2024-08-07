class Formula:
    def __str__(self):
        raise NotImplementedError("Subclasses must implement this method")

    def num_conec(self):
        raise NotImplementedError("Subclasses must implement this method")

    def num_Negacion(self):
        raise NotImplementedError("Subclasses must implement this method")

    def num_letras(self):
        raise NotImplementedError("Subclasses must implement this method")

    def num_parentesis(self):
        raise NotImplementedError("Subclasses must implement this method")

    def num_binarios(self):
        raise NotImplementedError("Subclasses must implement this method")

class Letra(Formula):
    def __init__(self, letra: str):
        self.letra = letra

    def __str__(self):
        return self.letra

    def num_conec(self):
        return 0

    def num_Negacion(self):
        return 0

    def num_letras(self):
        return 1

    def num_parentesis(self):
        return 0

    def num_binarios(self):
        return 0

class Negacion(Formula):
    def __init__(self, subf: Formula):
        self.subf = subf

    def __str__(self):
        return '-' + str(self.subf)

    def num_conec(self):
        return 1 + self.subf.num_conec()

    def num_Negacion(self):
        return 1 + self.subf.num_Negacion()

    def num_letras(self):
        return self.subf.num_letras()

    def num_parentesis(self):
        return 1 + self.subf.num_parentesis()

    def num_binarios(self):
        return self.subf.num_binarios()

class Binario(Formula):
    def __init__(self, conectivo: str, left: Formula, right: Formula):
        assert conectivo in ['Y', 'O', '>', '=']
        self.conectivo = conectivo
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + self.conectivo + str(self.right) + ")"

    def num_conec(self):
        return 1 + self.left.num_conec() + self.right.num_conec()

    def num_Negacion(self):
        return self.left.num_Negacion() + self.right.num_Negacion()

    def num_letras(self):
        return self.left.num_letras() + self.right.num_letras()

    def num_parentesis(self):
        return 1 + self.left.num_parentesis() + self.right.num_parentesis()

    def num_binarios(self):
        return 1 + self.left.num_binarios() + self.right.num_binarios()

# Prueba del código
p = Letra("p")
q = Letra("q")
r = Letra("r")

A1 = Binario(">", q, r)
A15 = Negacion(A1)
A2 = Binario("O", p, A15)

B1 = Negacion(Negacion(Negacion(A1)))
B2 = Negacion(A2)

C1 = Binario("=", B2, B1)

print(C1)  # Muestra la fórmula como cadena

print(C1.num_binarios())  # Cuenta los binarios en C1
