def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

def sumar(a, b):
    return a + b

while True:
    menu()
    opcion = int(input("Opción: "))
    if opcion == 3:
        break
    x = int(input("Número 1: "))
    y = int(input("Número 2: "))
    print("Resultado:", sumar(x, y))
