print("=== MINI CARRITO DE COMPRAS ===")

productos = ["Pizza", "Refresco", "Postre"]
precios = [150, 40, 60]
total = 0

while True:
    print("\n--- MENÚ ---")
    for i in range(len(productos)):
        print(f"{i+1}. {productos[i]} - ${precios[i]}")

    print("4. Finalizar compra")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 4:
        break
    elif opcion < 1 or opcion > 4:
        print("Opción inválida.")
        continue

    cantidad = int(input("Cantidad: "))
    subtotal = precios[opcion-1] * cantidad
    total += subtotal
    print(f"Agregado: {cantidad} x {productos[opcion-1]} = ${subtotal:.2f}")

if total > 500:
    total *= 0.85
    print("\nDescuento del 15% aplicado!")

print(f"\nTotal a pagar: ${total:.2f}")
print("Gracias por su compra 🛒")
