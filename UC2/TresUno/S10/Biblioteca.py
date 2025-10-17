print("=== BIBLIOTECA DIGITAL PYTHON ===")

# --- Estructura base: Diccionario para guardar libros ---
biblioteca = {
    "Cien años de soledad": "Gabriel García Márquez",
    "Don Quijote de la Mancha": "Miguel de Cervantes",
    "El Principito": "Antoine de Saint-Exupéry"
}

# --- Menú principal ---
while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar libros")
    print("2. Agregar libro")
    print("3. Eliminar libro")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Mostrar catálogo
        print("\n📚 CATÁLOGO DE LIBROS:")
        if biblioteca:
            for titulo, autor in biblioteca.items():
                print(f"- {titulo} ({autor})")
        else:
            print("La biblioteca está vacía.")

    elif opcion == "2":
        # Agregar libro
        titulo = input("Título del libro: ")
        autor = input("Autor del libro: ")
        biblioteca[titulo] = autor
        print(f"✅ '{titulo}' agregado correctamente.")

    elif opcion == "3":
        # Eliminar libro
        titulo = input("Título del libro a eliminar: ")
        if titulo in biblioteca:
            del biblioteca[titulo]
            print(f"❌ '{titulo}' eliminado correctamente.")
        else:
            print("⚠️ Ese libro no se encuentra en la biblioteca.")

    elif opcion == "4":
        print("\nSaliendo del sistema...")
        break

    else:
        print("⚠️ Opción no válida. Intenta de nuevo.")
