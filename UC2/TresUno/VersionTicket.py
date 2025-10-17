print("=" * 40)
print("     RESTAURANTE PYTHON DEL SABOR".center(40))
print("=" * 40)

# --- Menú base ---
menu = {
    1: {"nombre": "Hamburguesa", "precio": 120},
    2: {"nombre": "Pizza", "precio": 150},
    3: {"nombre": "Tacos", "precio": 80},
    4: {"nombre": "Refresco", "precio": 40},
    5: {"nombre": "Postre", "precio": 60},
    6: {"nombre": "Salir", "precio": 0}
}

# --- Variables acumuladoras ---
orden = []   # lista para guardar los pedidos
total = 0

# --- Ciclo principal ---
while True:
    print("\n--- MENÚ DEL DÍA ---")
    for clave, item in menu.items():
        print(f"{clave}. {item['nombre']:<15} ${item['precio']:>6}")

    opcion = int(input("\nSeleccione una opción (1-6): "))

    if opcion == 6:
        print("\nGenerando ticket...\n")
        break

    if opcion not in menu:
        print("⚠️ Opción no válida. Intente de nuevo.")
        continue

    cantidad = int(input(f"¿Cuántos {menu[opcion]['nombre']} desea?: "))
    subtotal = menu[opcion]['precio'] * cantidad
    total += subtotal
    orden.append((menu[opcion]['nombre'], cantidad, subtotal))
    print(f"✅ {cantidad} x {menu[opcion]['nombre']} agregado(s) (${subtotal:.2f})")

# --- Cálculo del descuento ---
descuento = 0
if total > 500:
    descuento = total * 0.15
    total -= descuento

# --- Impresión del ticket ---
print("=" * 40)
print("       TICKET DE COMPRA FINAL".center(40))
print("=" * 40)
print("{:<20}{:<8}{:>10}".format("Producto", "Cant.", "Subtotal"))
print("-" * 40)

for nombre, cantidad, subtotal in orden:
    print(f"{nombre:<20}{cantidad:<8}{subtotal:>10.2f}")

print("-" * 40)
print(f"{'Descuento 15%:' if descuento > 0 else 'Descuento:' :<28}${descuento:>10.2f}")
print(f"{'TOTAL A PAGAR:' :<28}${total:>10.2f}")
print("=" * 40)
print("¡Gracias por su visita! 🍽️".center(40))
print("Vuelva pronto a RESTAURANTE PYTHON".center(40))
print("=" * 40)
