#EJERCICIO 4
#4. Pedir la cantidad de grados y convertirlos a °C, °F y K.

#ENTRADA
grados = float( input( "ingrese la cantidad de grados a convertir: "))
escala = input( "ingrese la escala de los grados (C para Celsius, F para Farenheit, K para Kelvin): ").strip().upper()

#PROCESO
CERO_ABSOLUTO = 273.15
DESPLAZAMIENTO = 32

kelvin_celsius = grados - CERO_ABSOLUTO
kelvin_farenheit = ((9 * (grados - CERO_ABSOLUTO) / 5) + 32)
farenheit_celsius = (5 * (grados - 32 ) / 9 + CERO_ABSOLUTO)
farenheit_kelvin = (5 * (grados - 32 ) / 9 + CERO_ABSOLUTO) + 32
celsius_kelvin = CERO_ABSOLUTO - grados
celsius_farenheit = 9 *grados / 5 + 32
	


#SALIDA
print("La conversión de grados a celsius es: ", kelvin_celsius)
print("La conversión de grados a farenheit es: ", kelvin_farenheit)
print("La conversión de grados a kelvin es: ", farenheit_celsius )
print("La conversión de grados a kelvin es: ", farenheit_kelvin)
print("La conversión de grados a kelvin es: ", celsius_kelvin )
print("La conversión de grados a kelvin es: ", celsius_farenheit )

#Reviar F
