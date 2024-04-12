import random
import string

Longitud_contraseña = int(input("Ingrese la longitud que desea que tenga su contraseña(Debe ser mayor a 10): "))

caracteres = string.ascii_letters + string.digits + string.punctuation

Contraseña = " "
while len(Contraseña) < Longitud_contraseña:
    Contraseña += random.choice(caracteres)


print("La contraseña segurida es: ", Contraseña )