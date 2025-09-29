# Inicialización de variables
total_promedios = 0
lista_promedios = []
lista_calificaciones = []

# Pedimos la cantidad de alumnos
alumnos = int(input("Ingrese la cantidad de alumnos: "))

for i in range(alumnos):
    suma_calificaciones = 0
    calificaciones_alumno = []

    # Pedimos cuántas materias tiene el alumno
    materias = int(input(f"\nIngrese la cantidad de materias del alumno {i + 1}: "))

    for j in range(materias):
        calificacion = float(input(f"Ingrese la calificación de la materia {j + 1}: "))
        calificaciones_alumno.append(calificacion)
        suma_calificaciones += calificacion

    # Guardamos lista de calificaciones del alumno
    lista_calificaciones.append(calificaciones_alumno)

    # Calculamos y guardamos el promedio del alumno
    promedio_alumno = suma_calificaciones / materias
    lista_promedios.append(promedio_alumno)
    total_promedios += promedio_alumno

    print(f"El promedio del alumno {i + 1} es: {promedio_alumno:.2f}")

# Promedio general de todos los alumnos
promedio_general = total_promedios / alumnos
print(f"\nEl promedio general de los {alumnos} alumnos es: {promedio_general:.2f}")

# Mostrar detalle final
print("\n--- Detalle de calificaciones ---")
for i, califs in enumerate(lista_calificaciones):
    print(f"Alumno {i + 1}: Calificaciones = {califs}, Promedio = {lista_promedios[i]:.2f}")
