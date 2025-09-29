# Pedir datos al usuario
sueldo = float(input("¿Cuál es el sueldo del empleado? "))
años_trabajando = int(input("¿Tiempo laborando en la empresa (en años)? "))

# Condición para incentivo
if sueldo < 5000 or años_trabajando >= 5:
    incentivo = sueldo * 0.10   # 10%
else:
    incentivo = 0

# Calcular sueldo total
sueldo_a_pagar = sueldo + incentivo

# Mostrar resultados
print("Sueldo base: ", sueldo)
print("Incentivo: ", incentivo)
print("Sueldo con incentivo: ", sueldo_a_pagar)
