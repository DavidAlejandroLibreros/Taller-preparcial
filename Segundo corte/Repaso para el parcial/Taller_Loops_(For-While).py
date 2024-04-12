8# `EJERCICIO 6:`
print("EJERCICIO 6")
'''Un usuario necesita generar una contraseña segura para su cuenta en línea. 
Utiliza un bucle WHILE para generar una contraseña aleatoria que cumpla con ciertos 
criterios de seguridad. Este ejercicio muestra cómo utilizar un bucle WHILE para 
generar contraseñas seguras que cumplan con requisitos específicos, como longitud 
mínima y uso de caracteres especiales.'''

#Aquí se importan los módulos o librerias necesarias para usaar los methodos
import random as r  #Se apoda con un alias el módulo random
import string as s  #Se apoda con un alias el módulo string

'''
Se define la variable -caracteres_permitidos- con una cadena de caractes, los cuales 
son los caracteres permitidos para la contraseña (letras, dígitos y signos de puntuación):
( abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ )
'''
caracteres_permitidos = s.ascii_letters + s.digits + s.punctuation 

#Se solicitar al usuario la longitud de la contraseña
longitud = int(input('Ingresa el número de caracteres de tu contraseña: '))

# Inicializar la contraseña como una cadena vacía
contrasena = ''

#Generara la contraseña hasta que tenga la longitud especificada
while len(contrasena) < longitud:
    #Genera un carácter aleatorio a partir de los caracteres permitidos
    caracter_aleatorio = r.choice(caracteres_permitidos)
    #Agrega el carácter aleatorio a la variable contraseña
    contrasena += caracter_aleatorio

print("\n¡Tu contraseña de longitud ", longitud, "es: ", contrasena)



# `EJERCICIO 8:`
print("\n\nEJERCICIO 8")
'''Un gerente de ventas necesita calcular las estadísticas de ventas de su equipo. 
Utiliza un bucle FOR para calcular el total de ventas, la venta más alta y la 
venta más baja. Aquí se presenta una situación empresarial donde se utiliza 
un bucle FOR para analizar datos de ventas y calcular estadísticasimportantes.'''

A = [32, 5, 87, 55, 12, 4, 23, 0, 65, 17];
print('\n'+'A =', A, '\n')

tamaño_lista = len(A)
mayor = A[0];
menor = A[0];

for i in range(0, tamaño_lista):
    if (A[i] > mayor): 
        mayor = A[i];
    if (A[i] < menor): 
        menor = A[i];

'''Puse str para convertir el numero almacenado en la variable menor a tipo string, 
y así luego poder concatenar la cadena de texto con el contenido de menor''' 
print("El menor del vector es: "  + str(menor))
print("El mayor del vector es: " + str (mayor))

'''Aquí no puse str y por eso no concatene, por eso solo puse la variable 
separada con coma''' 
print("La cantiad de ventas fue:" , tamaño_lista) 



# `EJERCICIO 31:`
print("\n\nEJERCICIO 31")
'''Escribe un programa para mostrar el patrón como una pirámide usando asteriscos, con cada fila
conteniendo un número impar de asteriscos.
  *
 ***
*****
'''

#Se solicita al usuario que ingrese un número impar
n = int(input("Ingrese un número impar: "))

#Aquí se verifica si el número ingresado es par
if n % 2 == 0:
    #Y si el número ingresado es par, se muestra un mensaje de error y solicita un número impar
    print("El número ingresado es par. Por favor ingrese un número impar para la pirámide.")
else:
    #Si el número ingresado es impar, procede a construir la pirámide
    #El bucle for se encarga de iterar sobre los valores de i desde 1 hasta n, con un paso de 2 en 2.
    #Esto significa que i tomará valores que son impares, ya que comienza en 1 y se incrementa en 2 en cada iteración.
    for i in range(1, n + 1, 2):
        #En cada iteración del bucle, se imprime una cadena que representa una fila de la pirámide.
        #La cadena se compone de espacios en blanco y asteriscos (" " y "*"), donde el número de asteriscos en cada fila es igual al valor de i.
        #Además, se agrega un cierto número de espacios en blanco al principio de cada fila para centrar las filas de la pirámide.
        #La cantidad de espacios en blanco se calcula utilizando la expresión ((n - i) // 2), donde n es el número total de filas de la pirámide.
        #El operador de división entera (//) se utiliza para asegurar que la cantidad de espacios en blanco sea un número entero.
        #En resumen, se imprimen espacios en blanco seguidos de asteriscos para formar la pirámide.
        print(" " * ((n - i) // 2) + "*" * i)



# `EJERCICIO 32:`
print("\n\nEJERCICIO 32")
'''Escribe un programa para mostrar un patrón como un diamante usando asteriscos. 
El resultado esperado del programa debe ser similar al siguiente:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
n = int(input("Ingrese un número impar: "))  # Se solicita al usuario que ingrese un número impar

if n % 2 == 0:  # Verifica si el número ingresado es par
    print("El número ingresado es par. Por favor ingrese un número impar para el diamante.")
else:  # Si el número ingresado es impar, procede a construir el diamante
    
# Parte superior del diamante    
    for i in range(1, n+1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    
        # Parte inferior del diamante
    for j in range(n-2, 0, -2):
        print(" " * ((n - j) // 2) + "*" * j)
        
'''Este es parecido al anterior solo que en el segundo for se hace el proceso a la inverasa, 
y antes de iniciar se elimina el prceso de la fila que más astericos tiene para que no se imprima algo asi    
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''




import math as m

m.sqrt(30)

from math import sqrt, b

sqrt(30)

import math

math.sqrt(30)



