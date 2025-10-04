n = int(input("Ingresa un número: "))

print(f"\nNúmeros primos hasta {n}:")
for num in range(2, n + 1):   # empezamos desde 2 porque 1 no es primo
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=" ")

# Alternativa usando while
n = int(input("Ingresa un número: "))

print(f"\nNúmeros primos hasta {n}:")
num = 2
while num <= n:
    es_primo = True
    i = 2
    while i < num:
        if num % i == 0:
            es_primo = False
            break
        i += 1
    if es_primo:
        print(num, end=" ")
    num += 1
