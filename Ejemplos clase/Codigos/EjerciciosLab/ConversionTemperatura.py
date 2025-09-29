# Conversión de Celsius a Fahrenheit y Kelvin

celsius = float(input("Ingresa la temperatura en °C: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Temperatura en Fahrenheit: {fahrenheit:.2f} °F")
print(f"Temperatura en Kelvin: {kelvin:.2f} K")
