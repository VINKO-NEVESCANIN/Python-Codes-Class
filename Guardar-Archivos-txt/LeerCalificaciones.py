with open("calificaciones.txt", "r") as archivo:
    for linea in archivo:
        nombre, calif = linea.strip().split(",")
        print(f"{nombre}: {calif}")