with open("calificaciones.txt", "w") as archivo:
    for i in range(3):
        nombre = input("Alumno: ")
        calif = input("Calificación: ")
        archivo.write(f"{nombre},{calif}\n")

with open("calificaciones.txt", "r") as archivo:
    for linea in archivo:
        nombre, calif = linea.strip().split(",")
        print(f"{nombre}: {calif}")
 