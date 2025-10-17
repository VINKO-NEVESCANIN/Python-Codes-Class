def suma_for(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

def suma_while(n):
    suma = 0
    contador = 1
    while contador <= n:
        suma += contador
        contador += 1
    return suma

# --- Programa principal con menú ---
while True:
    print("\n=== MENÚ DE SUMA ===")
    print("1. Calcular suma con FOR")
    print("2. Calcular suma con WHILE")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        n = int(input("Ingresa un número: "))
        print(f"La suma de 1 a {n} con FOR es: {suma_for(n)}")
    elif opcion == "2":
        n = int(input("Ingresa un número: "))
        print(f"La suma de 1 a {n} con WHILE es: {suma_while(n)}")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
