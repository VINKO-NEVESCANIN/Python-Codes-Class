with open("calificaciones.txt", "a") as archivo:
    nombre = input("Nuevo alumno: ")
    calif = input("Calificación: ")
    archivo.write(f"{nombre},{calif}\n")
print("✅ Nuevo alumno agregado.")
