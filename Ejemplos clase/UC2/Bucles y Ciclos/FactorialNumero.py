n = int(input("Ingresa un número para calcular su factorial: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"El factorial de {n} es: {factorial}")

# Alternativa usando while
n = int(input("Ingresa un número: "))

contador = 1
pares = 0

while contador <= n:
    if contador % 2 == 0:
        pares += 1
    contador += 1

print(f"Cantidad de números pares entre 1 y {n}: {pares}")
