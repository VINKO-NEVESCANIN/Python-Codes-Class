import tkinter as tk
from tkinter import ttk, messagebox

class PromedioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Promedio de Alumnos")
        self.root.geometry("700x400")

        # Variables de control
        self.num_alumnos = tk.IntVar()
        self.num_materias = tk.IntVar()

        # Frame superior (entrada de alumnos y materias)
        frame_input = tk.Frame(root)
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Cantidad de alumnos:").grid(row=0, column=0, padx=5)
        tk.Entry(frame_input, textvariable=self.num_alumnos, width=5).grid(row=0, column=1, padx=5)

        tk.Label(frame_input, text="Cantidad de materias:").grid(row=0, column=2, padx=5)
        tk.Entry(frame_input, textvariable=self.num_materias, width=5).grid(row=0, column=3, padx=5)

        tk.Button(frame_input, text="Generar Tabla", command=self.generar_tabla, bg="lightblue").grid(row=0, column=4, padx=10)

        # Frame de tabla
        self.frame_tabla = tk.Frame(root)
        self.frame_tabla.pack(pady=10, fill="both", expand=True)

        # Botón calcular
        self.btn_calcular = tk.Button(root, text="Calcular Promedios", command=self.calcular_promedios, bg="lightgreen", state="disabled")
        self.btn_calcular.pack(pady=10)

    def generar_tabla(self):
        # Limpiar tabla previa si existe
        for widget in self.frame_tabla.winfo_children():
            widget.destroy()

        alumnos = self.num_alumnos.get()
        materias = self.num_materias.get()

        if alumnos <= 0 or materias <= 0:
            messagebox.showerror("Error", "Ingrese números válidos para alumnos y materias.")
            return

        # Crear Treeview (tabla)
        self.tree = ttk.Treeview(self.frame_tabla, columns=[f"Materia {j+1}" for j in range(materias)], show="headings", height=alumnos)
        self.tree.pack(fill="both", expand=True)

        # Definir encabezados
        for j in range(materias):
            self.tree.heading(f"Materia {j+1}", text=f"Materia {j+1}")
            self.tree.column(f"Materia {j+1}", width=100, anchor="center")

        # Insertar filas vacías
        for i in range(alumnos):
            self.tree.insert("", "end", values=[""] * materias, iid=f"Alumno {i+1}")

        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Activar botón calcular
        self.btn_calcular.config(state="normal")

    def calcular_promedios(self):
        alumnos = self.num_alumnos.get()
        materias = self.num_materias.get()

        resultados = []
        total_promedios = 0

        for i in range(alumnos):
            item_id = f"Alumno {i+1}"
            valores = self.tree.item(item_id, "values")

            try:
                calificaciones = [float(v) for v in valores]
                promedio_alumno = sum(calificaciones) / materias
                resultados.append(f"Alumno {i+1} → Calificaciones: {calificaciones} | Promedio: {promedio_alumno:.2f}")
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
