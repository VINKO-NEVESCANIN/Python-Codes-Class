estudiante = {
    "nombre": input("Nombre: "),
    "edad": int(input("Edad: ")),
    "carrera": "Ingeniería en Software"
}

print(f"\nEstudiante: {estudiante['nombre']} ({estudiante['edad']} años)")
print(f"Carrera: {estudiante['carrera']}")
print("\nInformación completa del estudiante:")
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")