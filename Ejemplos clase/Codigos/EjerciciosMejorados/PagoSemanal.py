# Pago semanal de un trabajador

print("=== Cálculo de Pago Semanal ===")
horas = float(input("Ingresa el número de horas trabajadas: "))
pago_hora = float(input("Ingresa el pago por hora: "))

# Si trabaja más de 40 horas, se paga tiempo extra (1.5 veces más)
if horas > 40:
    horas_extra = horas - 40
    pago = (40 * pago_hora) + (horas_extra * pago_hora * 1.5)
else:
    pago = horas * pago_hora

print(f"El pago semanal es: ${pago:.2f}")
