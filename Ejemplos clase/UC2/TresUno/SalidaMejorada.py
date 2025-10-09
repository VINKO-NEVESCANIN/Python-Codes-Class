print("===========================================")
print("     🍽️  BIENVENIDO AL RESTAURANTE PYTHON  🍽️")
print("===========================================")

total = 0
orden = []  # Lista para guardar los pedidos

while True:
    print("\n----------- MENÚ DEL DÍA -----------")
    print("1. 🍔  Hamburguesa\t$120")
    print("2. 🍕  Pizza      \t$150")
    print("3. 🌮  Tacos      \t$80")
    print("4. 🥤  Refresco   \t$40")
    print("5. 🍰  Postre     \t$60")
    print("6. 🚪  Salir")
    print("------------------------------------")

    try:
        opcion = int(input("\nSelecciona una opción (1-6): "))
    except ValueError:
        print("⚠️ Por favor, ingresa un número válido.")
        continue

    if opcion == 6:
        print("\nSaliendo del menú...")
        break

    if opcion < 1 or opcion > 6:
        print("⚠️ Opción no válida. Intenta de nuevo.")
        continue

    try:
        cantidad = int(input("¿Cuántos deseas?: "))
    except ValueError:
        print("⚠️ Ingresa una cantidad numérica.")
        continue

    if cantidad <= 0:
        print("⚠️ La cantidad debe ser mayor a cero.")
        continue

    # Asignar precios y nombres según la opción
    if opcion == 1:
        nombre, precio = "Hamburguesa", 120
    elif opcion == 2:
        nombre, precio = "Pizza", 150
    elif opcion == 3:
        nombre, precio = "Tacos", 80
    elif opcion == 4:
        nombre, precio = "Refresco", 40
    elif opcion == 5:
        nombre, precio = "Postre", 60

    subtotal = precio * cantidad
    total += subtotal
    orden.append((nombre, cantidad, precio, subtotal))

    print(f"✅ Agregado: {cantidad} x {nombre} = ${subtotal:.2f}")

# === RESUMEN DE LA COMPRA ===
print("\n\n===========================================")
print("🧾             RESUMEN DE LA COMPRA           ")
print("===========================================")
print(f"{'Producto':<15}{'Cant.':<8}{'P.Unit':<10}{'Subtotal'}")
print("-------------------------------------------")

for item in orden:
    nombre, cantidad, precio, subtotal = item
    print(f"{nombre:<15}{cantidad:<8}{precio:<10}${subtotal:.2f}")

print("-------------------------------------------")
print(f"{'Subtotal:':<33}${total:.2f}")

# Descuento del 15% si supera $500
if total > 500:
    descuento = total * 0.15
    total -= descuento
    print(f"{'Descuento (15%):':<33}-${descuento:.2f}")
else:
    print(f"{'Descuento:':<33}No aplica")

print("-------------------------------------------")
print(f"{'TOTAL A PAGAR:':<33}${total:.2f}")
print("===========================================")
print("🍴 Gracias por su compra. ¡Buen provecho! 🍴")
print("===========================================")


