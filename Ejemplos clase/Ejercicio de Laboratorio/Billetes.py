def calcular_billetes(retiro):
    if retiro % 50 != 0:
        print("La cantidad debe ser múltiplo de 50")
        return

    # Denominaciones disponibles
    denominaciones = [1000, 500, 200, 100, 50]
    resultado = {}

    for billete in denominaciones:
        cantidad = retiro // billete
        retiro = retiro % billete
        if cantidad > 0:
            resultado[billete] = cantidad

    # Mostrar resultado
    print("Se deben entregar:")
    for billete, cantidad in resultado.items():
        print(f"{cantidad} billete(s) de ${billete}")


# Ejemplo de uso
monto = int(input("Ingrese la cantidad a retirar (múltiplo de 50): "))
calcular_billetes(monto)
