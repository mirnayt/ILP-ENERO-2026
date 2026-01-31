#EJERICICIO 5
#Obtener valores para: a, b y c. Calcular la fórmula general.

#ENTRADA

import math
import cmath


#PROCESO
#declaración de variables

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))


r = b**2 - 4*a*c
x1 = (-b + math.sqrt(r)) / (2*a)
x2 = (-b - math.sqrt(r)) / (2*a)


#SALIDA

print("El valor de X1 es:", round(x1,2))
print("El valor de X2 es:", round(x2,2))