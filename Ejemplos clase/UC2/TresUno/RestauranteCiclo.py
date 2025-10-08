print("=== BIENVENIDO AL RESTAURANTE PYTHON ===")

total = 0  # acumulador de total

while True:
    print("\n--- MENÚ ---")
    print("1. Hamburguesa  $120")
    print("2. Pizza         $150")
    print("3. Tacos         $80")
    print("4. Refresco      $40")
    print("5. Postre        $60")
    print("6. Salir")

    opcion = int(input("\nSelecciona una opción (1-6): "))

    if opcion == 6:
        print("\nSaliendo del menú...")
        break

    if opcion < 1 or opcion > 6:
        print("⚠️ Opción no válida. Intenta de nuevo.")
        continue

    cantidad = int(input("¿Cuántos deseas?: "))

    # Determinar el precio según la opción
    if opcion == 1:
        precio = 120
        nombre = "Hamburguesa"
    elif opcion == 2:
        precio = 150
        nombre = "Pizza"
    elif opcion == 3:
        precio = 80
        nombre = "Tacos"
    elif opcion == 4:
        precio = 40
        nombre = "Refresco"
    elif opcion == 5:
        precio = 60
        nombre = "Postre"

    subtotal = precio * cantidad
    total += subtotal

    print(f"Agregado: {cantidad} x {nombre} = ${subtotal:.2f}")

# Aplicar descuento si el total supera $500
print("\n=== RESUMEN DE LA COMPRA ===")
print(f"Subtotal: ${total:.2f}")

if total > 500:
    descuento = total * 0.15
    total -= descuento
    print(f"Descuento del 15% aplicado: -${descuento:.2f}")
else:
    print("No aplica descuento.")

print(f"TOTAL A PAGAR: ${total:.2f}")
print("Gracias por su compra. ¡Buen provecho!")
