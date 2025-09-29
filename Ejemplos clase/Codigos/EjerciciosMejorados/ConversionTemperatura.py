# Conversión de temperaturas

print("=== Conversión de Temperaturas ===")
celsius = float(input("Ingresa la temperatura en °C: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius} °C = {fahrenheit:.2f} °F")
print(f"{celsius} °C = {kelvin:.2f} K")
