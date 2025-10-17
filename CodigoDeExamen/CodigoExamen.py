def calcular_beneficio(saldo_inicial, deposito):
    if deposito > 0.2 * saldo_inicial:
        return deposito * 0.05
    return 0

n = int(input("Ingrese número de clientes: "))

total_depositos = 0
total_retiros = 0
total_beneficio = 0
clientes_con_beneficio = 0

for i in range(1, n + 1):
    print(f"\nCliente {i}:")
    cuenta = input("Número de cuenta: ")
    saldo_inicial = float(input("Saldo inicial: $"))

    deposito = float(input("Cantidad a depositar: $"))
    retiro = float(input("Cantidad a retirar: $"))

    beneficio = calcular_beneficio(saldo_inicial, deposito)
    if beneficio > 0:
        clientes_con_beneficio += 1

    saldo_final = saldo_inicial + deposito + beneficio - retiro

    # Acumular totales
    total_depositos += deposito
    total_retiros += retiro
    total_beneficio += beneficio

    print(f"Cuenta: {cuenta}")
    print(f"Saldo inicial: ${saldo_inicial:.2f}")
    print(f"Saldo final: ${saldo_final:.2f}")

# Resultados finales
print("\n--- Resultados del día ---")
print(f"Clientes atendidos: {n}")
print(f"Total depósitos: ${total_depositos:.2f}")
print(f"Total retiros: ${total_retiros:.2f}")
print(f"Total beneficio: ${total_beneficio:.2f}")
print(f"Promedio de depósitos: ${total_depositos / n:.2f}")
print(f"Porcentaje de clientes con beneficio: {(clientes_con_beneficio / n) * 100:.2f}%")
