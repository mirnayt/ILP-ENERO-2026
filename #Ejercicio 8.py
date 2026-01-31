#Ejercicio 8
"""8. Calcular la nómina para un empleado en el mes de Enero del 2026 conociendo
su pago por día de $250"""

#ENTRADA
días_trabajados = int(input("Ingresa los días trabajados durante el mes de enero del 2026: "))


#PROCESO
#CONSTANTES
pago_por_día = 250
salario_base  = días_trabajados * pago_por_día  
iva_transalado = (0.16) *(salario_base)
iva_retenido = (2/3)* (iva_transalado)
isr = 0.10 * (salario_base)
subtotal = salario_base + iva_transalado

salario_neto = subtotal - iva_retenido - isr

#SALIDA DE DATOS 
print("El salario neto del empleado es: $", round(salario_neto, 2))