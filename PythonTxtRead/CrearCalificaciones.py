with open("calificaciones.txt", "w") as archivo:
    for i in range(3):
        nombre = input("Alumno: ")
        calif = input("Calificación: ")
        archivo.write(f"{nombre},{calif}\n")

print("✅ Calificaciones guardadas.")
