# --- Crear lista y guardar en archivo ---
videojuegos = []

print("🎮 Ingresa tus 5 videojuegos favoritos:\n")
for i in range(5):
    nombre = input(f"Videojuego {i+1}: ")
    consola = input("Plataforma (PC, PS5, Xbox, Switch, etc.): ")
    videojuegos.append(f"{nombre},{consola}\n")

with open("videojuegos.txt", "w") as archivo:
    archivo.writelines(videojuegos)

print("\n✅ Lista guardada correctamente en 'videojuegos.txt'\n")

# --- Leer y mostrar ordenados ---
lista_ordenada = []
with open("videojuegos.txt", "r") as archivo:
    for linea in archivo:
        lista_ordenada.append(linea.strip())

lista_ordenada.sort()  # Ordenar alfabéticamente

print("🎯 Tus videojuegos favoritos ordenados:\n")
for juego in lista_ordenada:
    nombre, consola = juego.split(",")
    print(f"- {nombre} ({consola})")
