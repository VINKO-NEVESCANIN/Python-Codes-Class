tareas = [
    "Revisar tipos de datos en Python",
    "Hacer ejercicios de expresiones aritméticas",
    "Estudiar funciones aritméticas",
    "Analizar un problema antes de programar",
    "Codificar y probar un programa en Python"
]

completadas = []

while True:
    print("\n=== CHECKLIST ===")
    for i, tarea in enumerate(tareas, start=1):
        status = "✔" if i in completadas else " "
        print(f"[{status}] {i}. {tarea}")

    print("\nEscribe el número de la tarea para marcarla como hecha (0 para salir):")
    opcion = input("> ")

    if opcion == "0":
        break
    if opcion.isdigit() and 1 <= int(opcion) <= len(tareas):
        num = int(opcion)
        if num in completadas:
            completadas.remove(num)
        else:
            completadas.append(num)
    else:
        print("⚠️ Opción no válida.")
