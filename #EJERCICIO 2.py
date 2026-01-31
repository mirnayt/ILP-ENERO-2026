#EJERCICIO 2

#Calcular el área y perímetro de un círculo.

#ENTRADA
import math 

#Declaración de variables 
radio = float(input("Ingrese el radio del círculo: "))

#PROCESO

perímetro = 2 * math.pi * radio
área = math.pi * radio ** 2


#SALIDA

print("El perímetro del círculo es: ", round(perímetro, 2))
print("El área del círculo es: ", round(área, 2))