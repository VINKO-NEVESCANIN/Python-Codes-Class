# --- Entrada ---
litros = float(input("Cantidad de litros cargados: "))
precio_litro = float(input("Precio por litro: $"))

# --- Proceso ---
total = litros * precio_litro

# --- Salida ---
print("\n===== RECIBO DE GASOLINA =====")
print(f"Litros cargados: {litros:.2f}")
print(f"Precio por litro: ${precio_litro:.2f}")
print("----------------------------")
print(f"TOTAL A PAGAR: ${total:.2f}")
print("============================")
