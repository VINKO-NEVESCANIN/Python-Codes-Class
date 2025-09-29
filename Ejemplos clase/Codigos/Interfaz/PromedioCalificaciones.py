import tkinter as tk
from tkinter import messagebox

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

ventana = tk.Tk()
ventana.title("Promedio de Calificaciones")

tk.Label(ventana, text="Ingresa calificación:").pack(pady=5)
entry = tk.Entry(ventana)
entry.pack(pady=5)

tk.Button(ventana, text="Agregar", command=agregar).pack(pady=5)
tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio).pack(pady=5)

lista = tk.Listbox(ventana)
lista.pack(pady=5)

ventana.mainloop()
