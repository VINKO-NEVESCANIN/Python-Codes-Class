# Inicializamos acumulador y contador
total_calificaciones = 0
alumnos = 0

# Mientras alumnos < 2
while alumnos < 2:
    calificacion = float(input(f"Ingrese la calificación del alumno {alumnos + 1}: "))
    total_calificaciones += calificacion
    alumnos += 1

# Calcular promedio (dividido entre 2 porque son 2 alumnos)
promedio = total_calificaciones / 2

# Mostrar resultado
print(f"El promedio de calificaciones es: {promedio:.2f}")
