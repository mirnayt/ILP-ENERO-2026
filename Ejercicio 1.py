#1. Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

#ENTRADA DE DATOS 
calificacion_1 = float(input("ingrese la primera calificación: "))
calificacion_2 = float(input("ingreses la segunda calificación:"))
calificacion_3 = float(input("ingrese la tercera calificación: "))


#PROCESO
promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3

#CONDICIONALES
"""
APROBADO           Rango (6.1 y 10)    (mayorq que 6 y 10)
REPROBADO          Rango (0 y 5.9) ( 0 y menor que 6)
APENAS APROBADO    Equivalente a 6
CALIFIACIÓN INVÁLIDA  (menor que 0 y mayor que 10)
"""
if promedio >= 6.1 and promedio <= 10:
    print("APROBADO")
elif promedio >= 0 and promedio < 6:
    print("REPROBADO")
elif promedio == 6:
    print("APENAS APROBADO")
elif promedio < 0 or promedio > 10:
    print("CALIFIACIÓN INVÁLIDA")

print("Tu promedio es: ", promedio)

#SALIDA DE DATOS
