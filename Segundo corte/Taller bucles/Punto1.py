Ovejas = [ "Oveja1", "Oveja2", "Oveja3", "Oveja4", "Oveja5"]

Contador_oveja = 1
while Contador_oveja < 5 :
    Nombre_oveja = Ovejas[Contador_oveja - 1] 
    print (f"La oveja número: {Contador_oveja} llamada {Nombre_oveja} se encuentra aquí")
    Contador_oveja += 1

print("Todas las ovejas han sido contadas y no falta ninguna")

