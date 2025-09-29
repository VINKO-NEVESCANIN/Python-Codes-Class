import tkinter as tk
from tkinter import simpledialog, messagebox

def calcular_promedio():
    try:
        alumnos = int(entry_alumnos.get())
        resultados = []
        total_promedios = 0

        for i in range(alumnos):
            # Pedimos cantidad de materias con ventana emergente
            materias = simpledialog.askinteger(
                "Materias",
                f"Ingrese la cantidad de materias del alumno {i+1}:",
                minvalue=1
            )

            suma_calificaciones = 0
            calificaciones = []

            for j in range(materias):
                calificacion = simpledialog.askfloat(
                    "Calificación",
                    f"Ingrese la calificación de la materia {j+1} del alumno {i+1}:",
                    minvalue=0, maxvalue=100
                )
                suma_calificaciones += calificacion
                calificaciones.append(calificacion)

            promedio_alumno = suma_calificaciones / materias
            resultados.append(f"Alumno {i+1} → Calificaciones: {calificaciones} | Promedio: {promedio_alumno:.2f}")
            total_promedios += promedio_alumno

        promedio_general = total_promedios / alumnos
        resultados.append(f"\n📊 Promedio general de {alumnos} alumnos: {promedio_general:.2f}")

        # Mostramos resultados en ventana emergente
        messagebox.showinfo("Resultados", "\n".join(resultados))

    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.")

# Interfaz principal
ventana = tk.Tk()
ventana.title("Promedio de Alumnos")
ventana.geometry("400x200")

label = tk.Label(ventana, text="Ingrese la cantidad de alumnos:")
label.pack(pady=10)

entry_alumnos = tk.Entry(ventana, justify="center", font=("Arial", 12))
entry_alumnos.pack(pady=5)

btn = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio, bg="lightblue", font=("Arial", 12))
btn.pack(pady=20)

ventana.mainloop()
