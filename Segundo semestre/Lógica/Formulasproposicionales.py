class Formula :
    def __init__(self) :
        pass
class Letra(Formula) :
    def __init__ (self, letra:str) :
        self.letra = letra
class Negacion(Formula) :    
    def __init__(self, subf:Formula) : 
        self.subf = subf
class Binario(Formula) :
    def __init__(self, conectivo:str, left:Formula, right:Formula) :
        assert(conectivo in ['Y','O','>','='])
        self.conectivo = conectivo
        self.left = left
        self.right = right

def __str__(self) :
    if type(self) == Letra:
        return self.letra
    elif type(self) == Negacion:
        return '-' + str(self.subf)
    elif type(self) == Binario:
        return "(" + str(self.left) + self.conectivo + str(self.right) + ")"
    
setattr(Formula, "__str__", __str__)

def num_conec(self) :
    if type(self) == Letra:
        return 0
    elif type(self) == Negacion:
        return 1 + self.subf.num_conec()
    elif type(self) == Binario:
        return 1 + self.left.num_conec() + self.right.num_conec()

setattr(Formula, "num_conec", num_conec)

def num_Negacion(self):
    if type(self) == Letra:
        return 0
    elif type(self) == Negacion:
        return 1 + num_Negacion(self.subf)
    elif type(self) == Binario:
        return 0 + num_Negacion(self.left) + num_Negacion(self.right)

setattr(Formula, "Num_negacion", num_Negacion)

def num_letras(self):
    if type(self) == Letra:
        return 1
    elif type(self) == Negacion:
        return 0 + num_letras(self.subf)
    elif type(self) == Binario:
        return 0 + num_letras(self.left) + num_letras(self.right)
    
setattr(Formula, "num_letras", num_letras)
    
def num_parentesis(self):
    if type(self) == Letra:
        return 0
    elif type(self) == Negacion:
        return 1 + num_parentesis(self.subf)
    elif type(self) == Binario:
        return 1 + num_parentesis(self.left) + num_parentesis(self.right)
    
setattr(Formula, "num_parentesis", num_parentesis)
    
def num_binarios(self):
    if type(self) == Letra:
        return 0
    elif type(self) == Negacion:
        return 0 + num_binarios(self.subf)
    elif type(self) == Binario:
        return 1 + num_binarios(self.left) + num_binarios(self.right)

setattr(Formula, "num_binarios", num_binarios)
    

p = Letra("p")
q = Letra("q")
r = Letra("r")

A1 = Binario(">", q, r)
A15 = Negacion(A1)
A2 =  Binario("O", p , A15)

B1 = Negacion(Negacion(Negacion(A1)))
B2 = Negacion(A2)

C1 = Binario("=", B2, B1)

print(C1)

print(num_binarios(C1))
print(num_letras(C1))
