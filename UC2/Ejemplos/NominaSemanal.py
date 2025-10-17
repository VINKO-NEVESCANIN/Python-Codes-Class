# --- Entrada ---
trabajador = input("Nombre del trabajador: ")
horas = float(input("Horas trabajadas en la semana: "))
pago_hora = float(input("Pago por hora: "))

# --- Proceso ---
sueldo_bruto = horas * pago_hora
isr = sueldo_bruto * 0.10   # 10% de retención
sueldo_neto = sueldo_bruto - isr

# --- Salida ---
print("\n===== RECIBO DE NÓMINA =====")
print(f"Trabajador: {trabajador}")
print(f"Horas trabajadas: {horas}")
print(f"Pago por hora: ${pago_hora:.2f}")
print(f"Sueldo bruto: ${sueldo_bruto:.2f}")
print(f"Retención ISR (10%): ${isr:.2f}")
print(f"Sueldo neto a pagar: ${sueldo_neto:.2f}")
print("=============================")
