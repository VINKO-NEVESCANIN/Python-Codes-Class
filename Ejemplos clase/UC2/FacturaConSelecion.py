def conversion_temperatura():
    celsius = float(input("Ingresa la temperatura en °C: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")

def promedio_calificaciones():
    n = int(input("¿Cuántas calificaciones promediarás? "))
    suma = 0
    for i in range(n):
        calificacion = float(input(f"Calificación {i+1}: "))
        suma += calificacion
    promedio = suma / n
    print(f"El promedio de las {n} calificaciones es: {promedio:.2f}")

def nomina_trabajador():
    trabajador = input("Nombre del trabajador: ")
    horas = float(input("Horas trabajadas en la semana: "))
    pago_hora = float(input("Pago por hora: "))
    sueldo_bruto = horas * pago_hora
    isr = sueldo_bruto * 0.10
    sueldo_neto = sueldo_bruto - isr
    print("\n===== RECIBO DE NÓMINA =====")
    print(f"Trabajador: {trabajador}")
    print(f"Sueldo bruto: ${sueldo_bruto:.2f}")
    print(f"ISR (10%): ${isr:.2f}")
    print(f"Sueldo neto: ${sueldo_neto:.2f}")
    print("============================")

# --- Menú principal ---
while True:
    print("\n--- MENÚ DE PROGRAMAS ---")
    print("1. Conversión de temperaturas")
    print("2. Promedio de calificaciones")
    print("3. Nómina de trabajador")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        conversion_temperatura()
    elif opcion == "2":
        promedio_calificaciones()
    elif opcion == "3":
        nomina_trabajador()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
