#COMENTARIOS:
#Son una descripción del programa o código 
# A los comentarios los imite  o no los coma en cuenta Python

#Importación de librerías:
#Mandar a llamar archivos de python para usar funciones y constantes especificas

import math
from colorama import Fore, Style

10


#ENTRADA DE DATOS
#DEclarar variables 
número_1= float(input("Ingrese un número: ")) #input siempre devuelve texto
número_2= float(input("Ingrese otro número: "))


#PROCESOS (Cálculo u operaciones)
suma = número_1 + número_2
resta = número_1 - número_2
multiplicación = número_1 * número_2
división = número_1 / número_2
potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2)
cuadrado = número_1 ** 2
cubo = número_2 ** 3
cubo_2 = pow(número_1, 3)
raíz_cuadrada = math.sqrt(9)
raíz_cuadrada_2 = pow(9, .5)
raíz_cubica = pow(27, 1/3)
# módulo =





print(Fore.GREEN + "Suma = ", suma) #Suma
print(Fore.RED + "Resta = ", número_1-número_2)
print("multiplicación = ", multiplicación) #multiplicación
print(f"División =  {división}")
print("potencia 1 = ", potencia_1)
print("potencia_2 = ", potencia_2)
print("cuadrado = ", cuadrado)
print("cubo = ", cubo)
print("cubo_2 = ", cubo_2)
print("raíz_cuadrada = ", raíz_cuadrada)
print("raíz_cuadrada_2 = ", raíz_cuadrada_2)
print("raíz_cubica = " , raíz_cubica)
print("Módulo = ", número_1 % número_2)
print (Style.RESET_ALL)

#comenar ctrl + k + c
#descomentar ctrl + k + u
