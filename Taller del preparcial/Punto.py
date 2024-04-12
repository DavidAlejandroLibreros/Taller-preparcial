a = int(input("Introduzca: a "))
b = int(input("Introduzca: b "))
c = int(input("Introduzca: c "))

if b**2 - 4*a*c < 0:
    print("La ecuación no tiene solución")
elif b**2 - 4*a*c > 0:
    x =  b**2
    y = 4*a*c
    z = x - y
    w = z** 0.5

    print("La ecuación tiene dos soluciones")
    Sol1 = (-b + w) / (2*a)
    Sol2 = (-b - w) / (2*a)
    print("Si tomamos a " + str(w) + " como positivo") 
    print("entonces la solución de la ecuación es: " + str(Sol1))
    print("Si tomamos a " + str(w) + " como negativo") 
    print("entonces la solución de la ecuación es: " + str(Sol2)) 
else: 
    Sol3 = -b/(2*a)
    print("La ecuación tiene solo una solución y es: " + str(Sol3))