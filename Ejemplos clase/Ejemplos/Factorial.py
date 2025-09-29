# Pedimos un número al usuario
num = int(input("Ingresa un número: "))

factorial = 1  # Empezamos en 1 porque multiplicar por 0 siempre da 0

# Recorremos desde 1 hasta num (incluido)
for i in range(1, num + 1):
    factorial = factorial * i   # Multiplicamos el valor actual

print(f"El factorial de {num} es: {factorial}")
