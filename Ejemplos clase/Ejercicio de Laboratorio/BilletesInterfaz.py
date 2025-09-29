def mostrar_menu():
    print("===================================")
    print("      CAJERO AUTOMATICO VIRTUAL    ")
    print("===================================")
    print("1. Retirar dinero")
    print("2. Salir")
    print("===================================")

def calcular_billetes(retiro):
    if retiro % 50 != 0:
        print("\n⚠️ Error: La cantidad debe ser multiplo de 50.\n")
        return

    denominaciones = [1000, 500, 200, 100, 50]
    resultado = {}

    for billete in denominaciones:
        cantidad = retiro // billete
        retiro = retiro % billete
        if cantidad > 0:
            resultado[billete] = cantidad

    print("\n💵 Se deben entregar:")
    for billete, cantidad in resultado.items():
        print(f"{cantidad} billete(s) de ${billete}")
    print("\nGracias por usar el cajero.\n")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        try:
            monto = int(input("Ingrese la cantidad a retirar (multiplo de 50): "))
            calcular_billetes(monto)
        except ValueError:
            print("\n⚠️ Error: Debe ingresar un numero entero.\n")
    elif opcion == "2":
        print("Saliendo del cajero. Hasta luego!")
        break
    else:
        print("\n⚠️ Opción invalida. Intente nuevamente.\n")
