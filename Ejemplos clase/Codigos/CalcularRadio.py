import math

#Problema: Calcular el área de un círculo dado su radio
#Análisis: entrada = radio, salida = área
#Diseño: área = π * radio²
#Código en Python:

r = float(input("Radio: "))
area = math.pi * r ** 2
print(f"Área = {area:.2f}")
