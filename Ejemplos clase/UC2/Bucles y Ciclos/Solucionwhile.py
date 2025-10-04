n = int(input("Ingresa un número entero positivo: "))

suma = 0
contador = 1

while contador <= n:
    suma += contador
    contador += 1

print(f"La suma de los números de 1 a {n} es: {suma}")
