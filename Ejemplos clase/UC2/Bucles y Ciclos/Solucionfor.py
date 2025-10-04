n = int(input("Ingresa un número entero positivo: "))

suma = 0
for i in range(1, n + 1):
    suma += i   # acumulador

print(f"La suma de los números de 1 a {n} es: {suma}")
