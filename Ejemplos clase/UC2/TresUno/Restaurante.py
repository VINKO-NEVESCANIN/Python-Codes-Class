print("=== BIENVENIDO AL RESTAURANTE PYTHON ===")

# --- Datos base ---
menu = {
    1: {"nombre": "Hamburguesa", "precio": 120},
    2: {"nombre": "Pizza", "precio": 150},
    3: {"nombre": "Tacos", "precio": 80},
    4: {"nombre": "Refresco", "precio": 40},
    5: {"nombre": "Postre", "precio": 60},
    6: {"nombre": "Salir", "precio": 0}
}

total = 0  # Acumulador del total de la orden

# --- Ciclo principal ---
while True:
    print("\n--- MENÚ ---")
    for clave, item in menu.items():
        print(f"{clave}. {item['nombre']} - ${item['precio']}")

    opcion = int(input("\nElige una opción (1-6): "))

    if opcion == 6:
        print("\nSaliendo del menú...")
        break

    if opcion not in menu:
        print("Opción no válida, intenta de nuevo.")
        continue

    cantidad = int(input(f"¿Cuántos {menu[opcion]['nombre']} deseas?: "))
    subtotal = menu[opcion]['precio'] * cantidad
    total += subtotal

    print(f"Agregado: {cantidad} x {menu[opcion]['nombre']} = ${subtotal:.2f}")

# --- Aplicar descuento si supera $500 ---
print("\n=== RESUMEN DE LA ORDEN ===")
print(f"Subtotal: ${total:.2f}")

if total > 500:
    descuento = total * 0.15
    total -= descuento
    print(f"Descuento del 15% aplicado: -${descuento:.2f}")
else:
    print("No aplica descuento.")

print(f"TOTAL FINAL A PAGAR: ${total:.2f}")
print("Gracias por su compra. ¡Buen provecho!")
