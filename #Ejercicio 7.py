#Ejercicio 7

#7. Pedir el nivel del agua en metros de una cisterna

"""
Nivel del agua (m)       Estado de la cisterna

Evento 
menos a 0                  Fuga en la cisterna
Nivel de 0           Encender la bomba de agua
Entre 0 y 2 m             Acelerar bomba de agua
Entre 2 y 4 m         bomba trabajando
entre 4 y 6 m         Desacelerar bomba de agua
Nivel de 6 m          Apagar bomba de agua
Si llega a más de 6 m       Desbordamiento de la cisterna
"""

#ENTRADA 
nivel_agua =float (input("Ingrese el nivel de agua en metros: "))

#VARIABLES
m = "metros"

#PROCESO 
#CONDICIONALES

if nivel_agua < 0: 
    print("Fuga en la cisterna")
elif nivel_agua == 0:
    print("Encender la bomba de agua")
elif nivel_agua > 0 and nivel_agua < 2:
    print("Acelerar bomba de agua")
elif nivel_agua >=2 and nivel_agua < 4:
    print("Bomba trabajando")
elif nivel_agua >=4 and nivel_agua <6:
    print("Desacelerar bomba de agua")
elif nivel_agua == 6:
    print("Apagar bomba de agua")
elif nivel_agua > 6:
    print("Desbordamiento de la cisterna")

#SALIDA DE DATOS
#print("El nivel de agua es de: ", nivel_agua, m)


