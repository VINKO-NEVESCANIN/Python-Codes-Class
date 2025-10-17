def mostrar_menu():
    print("\n=== MENÚ CALIFICACIONES ===")
    print("1. Agregar alumno")
    print("2. Mostrar lista")
    print("3. Buscar alumno")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Opción: ")

    if opcion == "1":
        with open("calificaciones.txt", "a") as f:
            nombre = input("Nombre: ")
            calif = input("Calificación: ")
            f.write(f"{nombre},{calif}\n")
        print("✅ Alumno agregado.")
    elif opcion == "2":
        with open("calificaciones.txt", "r") as f:
            for linea in f:
                nombre, calif = linea.strip().split(",")
                print(f"{nombre}: {calif}")
    elif opcion == "3":
        buscar = input("Nombre a buscar: ")
        encontrado = False
        with open("calificaciones.txt", "r") as f:
            for linea in f:
                nombre, calif = linea.strip().split(",")
                if nombre.lower() == buscar.lower():
                    print(f"{nombre}: {calif}")
                    encontrado = True
        if not encontrado:
            print("❌ Alumno no encontrado.")
    elif opcion == "4":
        print("👋 Saliendo del programa...")
        break
    else:
        print("Opción no válida.")
