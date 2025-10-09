total = 0
while True:
    producto = input("Nombre del producto (o 'fin' para terminar): ")
    if producto.lower() == 'fin':
        break
    precio = float(input("Precio: $"))
    total += precio

print(f"\nTotal sin descuento: ${total:.2f}")

if total > 1000:
    descuento = total * 0.10
    total -= descuento
    print(f"Descuento aplicado: ${descuento:.2f}")
else:
    print("No aplica descuento.")

print(f"Total a pagar: ${total:.2f}")
