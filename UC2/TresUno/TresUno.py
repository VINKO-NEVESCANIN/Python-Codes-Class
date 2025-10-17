saldo = 1000
pin_correcto = 1234

pin = int(input("Ingrese su PIN: "))

if pin == pin_correcto:
    while True:
        print("\n--- CAJERO AUTOMÁTICO ---")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Saldo actual: ${saldo:.2f}")
        elif opcion == "2":
            deposito = float(input("Ingrese cantidad a depositar: "))
            saldo += deposito
            print(f"Nuevo saldo: ${saldo:.2f}")
        elif opcion == "3":
            retiro = float(input("Ingrese cantidad a retirar: "))
            if retiro <= saldo:
                saldo -= retiro
                print(f"Nuevo saldo: ${saldo:.2f}")
            else:
                print("Fondos insuficientes.")
        elif opcion == "4":
            print("Gracias por usar el cajero.")
            break
        else:
            print("Opción no válida.")
else:
    print("PIN incorrecto. Acceso denegado.")


