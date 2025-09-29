import tkinter as tk
from tkinter import messagebox

class PromedioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Promedio de Alumnos")
        self.root.geometry("700x400")

        # Variables de control
        self.num_alumnos = tk.IntVar()
        self.num_materias = tk.IntVar()

        # Frame superior
        frame_input = tk.Frame(root)
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Cantidad de alumnos:").grid(row=0, column=0, padx=5)
        tk.Entry(frame_input, textvariable=self.num_alumnos, width=5).grid(row=0, column=1, padx=5)

        tk.Label(frame_input, text="Cantidad de materias:").grid(row=0, column=2, padx=5)
        tk.Entry(frame_input, textvariable=self.num_materias, width=5).grid(row=0, column=3, padx=5)

        tk.Button(frame_input, text="Generar Tabla", command=self.generar_tabla, bg="lightblue").grid(row=0, column=4, padx=10)

        # Frame para la tabla
        self.frame_tabla = tk.Frame(root)
        self.frame_tabla.pack(pady=10)

        # Botón calcular
        self.btn_calcular = tk.Button(root, text="Calcular Promedios", command=self.calcular_promedios, bg="lightgreen", state="disabled")
        self.btn_calcular.pack(pady=10)

        # Matriz de entradas
        self.entries = []

    def generar_tabla(self):
        # Limpiar tabla previa
        for widget in self.frame_tabla.winfo_children():
            widget.destroy()
        self.entries.clear()

        alumnos = self.num_alumnos.get()
        materias = self.num_materias.get()

        if alumnos <= 0 or materias <= 0:
            messagebox.showerror("Error", "Ingrese números válidos para alumnos y materias.")
            return

        # Crear encabezados
        tk.Label(self.frame_tabla, text="Alumno", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
        for j in range(materias):
            tk.Label(self.frame_tabla, text=f"Materia {j+1}", font=("Arial", 10, "bold")).grid(row=0, column=j+1, padx=5, pady=5)

        # Crear celdas editables
        for i in range(alumnos):
            fila = []
            tk.Label(self.frame_tabla, text=f"Alumno {i+1}").grid(row=i+1, column=0, padx=5, pady=5)
            for j in range(materias):
                entry = tk.Entry(self.frame_tabla, width=10, justify="center")
                entry.grid(row=i+1, column=j+1, padx=5, pady=5)
                fila.append(entry)
            self.entries.append(fila)

        # Activar botón calcular
        self.btn_calcular.config(state="normal")

    def calcular_promedios(self):
        alumnos = self.num_alumnos.get()
        materias = self.num_materias.get()

        resultados = []
        total_promedios = 0

        for i in range(alumnos):
            calificaciones = []
            try:
                for j in range(materias):
                    valor = float(self.entries[i][j].get())
                    calificaciones.append(valor)
                promedio_alumno = sum(calificaciones) / materias
                resultados.append(f"Alumno {i+1} → {calificaciones} | Promedio: {promedio_alumno:.2f}")
                total_promedios += promedio_alumno
            except ValueError:
                messagebox.showerror("Error", f"Faltan calificaciones válidas en Alumno {i+1}.")
                return

        promedio_general = total_promedios / alumnos
        resultados.append(f"\n📊 Promedio general de {alumnos} alumnos: {promedio_general:.2f}")

        messagebox.showinfo("Resultados", "\n".join(resultados))


# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = PromedioApp(root)
    root.mainloop()
