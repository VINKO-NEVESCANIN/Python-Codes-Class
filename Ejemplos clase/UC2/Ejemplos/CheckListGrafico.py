import matplotlib.pyplot as plt

tareas = [
    "Tipos de datos",
    "Expresiones aritméticas",
    "Funciones aritméticas",
    "Analizar problema",
    "Codificar y probar"
]

completadas = 3  # Cambia este valor para simular avance
total = len(tareas)

# Crear gráfico de progreso
fig, ax = plt.subplots(figsize=(6, 3))
ax.barh(["Progreso"], completadas, color="green")
ax.barh(["Progreso"], total - completadas, left=completadas, color="lightgray")

ax.set_xlim(0, total)
ax.set_title("Checklist de aprendizaje", fontsize=14)
ax.text(completadas/2, 0, f"{completadas}/{total} completadas", ha='center', va='center', color='white', fontsize=12)

plt.show()
