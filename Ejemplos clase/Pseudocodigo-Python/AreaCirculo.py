import math

# Entrada
radio = float(input("Ingrese el radio en cm: "))
altura = float(input("Ingrese la altura en cm: "))

# Cálculos
area = 2 * math.pi * radio * (radio + altura)  # cm²
volumen_cm3 = math.pi * radio**2 * altura      # cm³
volumen_litros = volumen_cm3 / 1000            # litros

# Salida
print(f"Área del cilindro: {area:.2f} cm²")
print(f"Volumen del cilindro: {volumen_litros:.2f} litros")
