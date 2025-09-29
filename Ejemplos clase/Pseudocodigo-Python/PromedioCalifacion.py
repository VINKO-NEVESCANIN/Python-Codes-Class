# Inicializamos acumulador
total_calificaciones = 0

# Pedir cuántos alumnos se van a promediar
alumnos = int(input("¿Cuántos alumnos promediarás? "))

# Contador
cont = 0

# Bucle para leer las calificaciones
while cont < alumnos:
    calificacion = float(input(f"Ingresa la calificación del alumno {cont + 1}: "))
    total_calificaciones += calificacion
    cont += 1

# Calcular promedio (correcto: dividir entre alumnos)
promedio = total_calificaciones / alumnos

# Mostrar resultado
print(f"El promedio de calificaciones es: {promedio:.2f}")
