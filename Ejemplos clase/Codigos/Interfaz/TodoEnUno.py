import tkinter as tk
from tkinter import messagebox

# ====== Conversión de Temperaturas ======
def convertir_temp():
    def calcular():
        try:
            celsius = float(entry.get())
            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15
            messagebox.showinfo("Resultado",
                                f"{celsius} °C = {fahrenheit:.2f} °F\n"
                                f"{celsius} °C = {kelvin:.2f} K")
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido")

    ventana = tk.Toplevel(root)
    ventana.title("Conversión de Temperaturas")
    tk.Label(ventana, text="Temperatura en °C:").pack(pady=5)
    entry = tk.Entry(ventana)
    entry.pack(pady=5)
    tk.Button(ventana, text="Convertir", command=calcular).pack(pady=10)

# ====== Promedio de Calificaciones ======
def promedio_calificaciones():
    calificaciones = []

    def agregar():
        try:
            cal = float(entry.get())
            calificaciones.append(cal)
            lista.insert(tk.END, cal)
            entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido")

    def calcular_promedio():
        if calificaciones:
            promedio = sum(calificaciones) / len(calificaciones)
            messagebox.showinfo("Resultado", f"Promedio: {promedio:.2f}")
        else:
            messagebox.showwarning("Aviso", "No hay calificaciones registradas")

    ventana = tk.Toplevel(root)
    ventana.title("Promedio de Calificaciones")

    tk.Label(ventana, text="Ingresa calificación:").pack(pady=5)
    entry = tk.Entry(ventana)
    entry.pack(pady=5)
    tk.Button(ventana, text="Agregar", command=agregar).pack(pady=5)
    tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio).pack(pady=5)
    lista = tk.Listbox(ventana)
    lista.pack(pady=5)

# ====== Pago Semanal de un Trabajador ======
def pago_semanal():
    def calcular_pago():
        try:
            horas = float(entry_horas.get())
            pago_hora = float(entry_pago.get())

            if horas > 40:
                horas_extra = horas - 40
                pago = (40 * pago_hora) + (horas_extra * pago_hora * 1.5)
            else:
                pago = horas * pago_hora

            messagebox.showinfo("Resultado", f"Pago semanal: ${pago:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos")

    ventana = tk.Toplevel(root)
    ventana.title("Pago Semanal")

    tk.Label(ventana, text="Horas trabajadas:").pack(pady=5)
    entry_horas = tk.Entry(ventana)
    entry_horas.pack(pady=5)

    tk.Label(ventana, text="Pago por hora:").pack(pady=5)
    entry_pago = tk.Entry(ventana)
    entry_pago.pack(pady=5)

    tk.Button(ventana, text="Calcular Pago", command=calcular_pago).pack(pady=10)

# ====== Ventana Principal ======
root = tk.Tk()
root.title("Menú de Ejercicios en Python")
root.geometry("300x250")

tk.Label(root, text="Selecciona un ejercicio", font=("Arial", 12, "bold")).pack(pady=15)

tk.Button(root, text="Conversión de Temperaturas", command=convertir_temp, width=30).pack(pady=5)
tk.Button(root, text="Promedio de Calificaciones", command=promedio_calificaciones, width=30).pack(pady=5)
tk.Button(root, text="Pago Semanal de un Trabajador", command=pago_semanal, width=30).pack(pady=5)

tk.Button(root, text="Salir", command=root.quit, width=30, bg="red", fg="white").pack(pady=15)

root.mainloop()
