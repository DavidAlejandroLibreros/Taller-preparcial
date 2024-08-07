class Tree(object):
    def __init__(self, iz,der):
        self.left = iz
        self.right = der

Hoja = Tree(None, None)
Rama = Tree(Hoja, Hoja)

Arb1 = Tree(Rama, Hoja)
Arb2 = Tree(Hoja,Rama)
Arb3 = Tree(Rama, Rama)



def NumAristas(Arb1):
    if Arb1.left == None:
        return 0
    else:
        return 2 + NumAristas(Arb1.left) + NumAristas(Arb1.right)



def NumHojas(Arb):
    if Arb.left == None:
        return 1
    else:
        return NumHojas(Arb.left) + NumHojas(Arb.right)
    

def  NumNodos(Arb):
    if Arb.left == None:
        return 1
    else:
        return 1 + NumNodos(Arb.left) + NumNodos(Arb.right)
    
A = Tree(Tree(Tree(Tree(None, None), Tree(None, None)), Tree(Tree(None, None), Tree(None, None))), Tree(Tree(Tree(None, None), Tree(None, None)), Tree(None, None)))

print(NumNodos(A))