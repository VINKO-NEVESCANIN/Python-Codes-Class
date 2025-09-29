import pandas as pd

# Inicialización de datos
alumnos_data = []

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

    promedio_alumno = suma_calificaciones / materias

    alumnos_data.append({
        "Alumno": f"Alumno {i+1}",
        "Materias": materias,
        "Calificaciones": calificaciones_alumno,
        "Promedio": promedio_alumno
    })

# Convertimos a DataFrame
df = pd.DataFrame(alumnos_data)

# Mostramos en formato tabla
print("\n--- Tabla de Resultados ---")
print(df)

# Promedio general
promedio_general = df["Promedio"].mean()
print(f"\nEl promedio general de los {alumnos} alumnos es: {promedio_general:.2f}")
