# --- Función para mostrar el menú ---
def mostrar_menu():
    print("\n🎮 === MENÚ DE VIDEOJUEGOS ===")
    print("1. Agregar videojuego")
    print("2. Mostrar lista")
    print("3. Buscar por consola")
    print("4. Salir")

# --- Función para agregar videojuego ---
def agregar_videojuego():
    nombre = input("Nombre del videojuego: ")
    consola = input("Plataforma (PC, PS5, Xbox, Switch, etc.): ")

    # Guardar en archivo
    with open("videojuegos.txt", "a") as archivo:
        archivo.write(f"{nombre},{consola}\n")

    print(f"✅ '{nombre}' agregado correctamente.\n")

# --- Función para mostrar lista completa ---
def mostrar_lista():
    try:
        with open("videojuegos.txt", "r") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            print("📂 No hay videojuegos registrados.")
            return

        print("\n🎯 LISTA DE VIDEOJUEGOS:")
        for linea in lineas:
            nombre, consola = linea.strip().split(",")
            print(f"- {nombre} ({consola})")
    except FileNotFoundError:
        print("⚠️ No existe el archivo todavía. Agrega un videojuego primero.")

# --- Función para buscar por consola ---
def buscar_por_consola():
    buscar = input("Ingrese el nombre de la consola: ").lower()
    encontrados = []

    try:
        with open("videojuegos.txt", "r") as archivo:
            for linea in archivo:
                nombre, consola = linea.strip().split(",")
                if consola.lower() == buscar:
                    encontrados.append(nombre)

        if encontrados:
            print(f"\n🎮 Juegos para {buscar.upper()}:")
            for juego in encontrados:
                print(f"- {juego}")
        else:
            print(f"❌ No se encontraron juegos para {buscar.upper()}.")

    except FileNotFoundError:
        print("⚠️ No existe el archivo todavía. Agrega un videojuego primero.")

# --- Programa principal ---
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_videojuego()
    elif opcion == "2":
        mostrar_lista()
    elif opcion == "3":
        buscar_por_consola()
    elif opcion == "4":
        print("👋 Saliendo del programa... ¡Hasta pronto!")
        break
    else:
        print("❌ Opción no válida. Intenta de nuevo.")
