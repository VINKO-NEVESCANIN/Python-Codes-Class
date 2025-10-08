print("=== BIENVENIDO A AUTOS PYTHON ===")

# Datos base
autos = {
    1: {"modelo": "Mustang GT", "precio": 950000},
    2: {"modelo": "Toyota Supra", "precio": 1200000},
    3: {"modelo": "Nissan 370Z", "precio": 850000},
    4: {"modelo": "Salir", "precio": 0}
}

total_compras = 0

while True:
    print("\n--- MENÚ DE AUTOS DISPONIBLES ---")
    for clave, auto in autos.items():
        print(f"{clave}. {auto['modelo']} - ${auto['precio']:,}")

    opcion = int(input("Selecciona un auto (1-4): "))

    if opcion == 4:
        print("\nSaliendo del sistema de ventas...")
        break

    if opcion not in autos:
        print("Opción no válida, intenta de nuevo.")
        continue

    auto_seleccionado = autos[opcion]
    cantidad = int(input(f"¿Cuántos {auto_seleccionado['modelo']} deseas comprar?: "))

    subtotal = auto_seleccionado["precio"] * cantidad

    # Descuento condicional
    if subtotal > 1000000:
        descuento = subtotal * 0.10
        subtotal -= descuento
        print(f"✅ Descuento aplicado del 10% (${descuento:,.2f})")

    total_compras += subtotal
    print(f"Total por esta compra: ${subtotal:,.2f}")

print("\n--- RESUMEN FINAL ---")
print(f"Total de compras realizadas: ${total_compras:,.2f}")

# Condición final según el total
if total_compras >= 2000000:
    print("🎉 ¡Felicidades! Eres cliente Premium y obtienes mantenimiento gratis.")
elif total_compras > 0:
    print("Gracias por tu compra. ¡Vuelve pronto!")
else:
    print("No realizaste ninguna compra.")
