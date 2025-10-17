# Promedio, edad mayor y menor de 5 personas
suma_edades = 0
mayor = 0
menor = 1000  # un valor muy grande para empezar

for i in range(5):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    suma_edades += edad   # acumulador de edades
    
    if edad > mayor:
        mayor = edad
    if edad < menor:
        menor = edad

promedio = suma_edades / 5

print("\n===== RESULTADOS =====")
print(f"Promedio de edades: {promedio:.2f}")
print(f"Edad mayor: {mayor}")
print(f"Edad menor: {menor}")
