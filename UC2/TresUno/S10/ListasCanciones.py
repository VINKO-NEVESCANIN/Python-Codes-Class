canciones = []

for i in range(5):
    cancion = input(f"Ingrese la canción #{i+1}: ")
    canciones.append(cancion)

print("\n🎵 Tus canciones favoritas:")
for i, c in enumerate(canciones, start=1):
    print(f"{i}. {c}")
