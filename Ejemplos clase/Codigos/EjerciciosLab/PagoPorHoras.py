# Cálculo del salario semanal

horas = float(input("Ingresa las horas trabajadas en la semana: "))
pago_hora = float(input("Ingresa el pago por hora: "))

salario = horas * pago_hora

print(f"El salario semanal es: ${salario:.2f}")
