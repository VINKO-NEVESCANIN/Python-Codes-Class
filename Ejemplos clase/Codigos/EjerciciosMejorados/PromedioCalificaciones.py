# Promedio de calificaciones

print("=== Promedio de Calificaciones ===")
n = int(input("¿Cuántos alumnos quieres promediar?: "))

total = 0
for i in range(n):
    calificacion = float(input(f"Ingrese la calificación del alumno {i+1}: "))
    total += calificacion

promedio = total / n
print(f"El promedio del grupo es: {promedio:.2f}")
