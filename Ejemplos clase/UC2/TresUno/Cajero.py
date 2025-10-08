saldo = 1000
pin_correcto = 1234
pin = int(input("Ingrese su PIN: "))

if pin == pin_correcto:
    while True:
        print("\n1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print(f"Saldo: ${saldo:.2f}")
        elif opcion == "2":
            deposito = float(input("Monto a depositar: "))
            saldo += deposito
        elif opcion == "3":
            retiro = float(input("Monto a retirar: "))
            if retiro <= saldo:
                saldo -= retiro
            else:
                print("Fondos insuficientes.")
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
else:
    print("PIN incorrecto.")
