import tkinter as tk
from tkinter import messagebox

# ====== Configuración de colores y estilo ======
BG_COLOR = "#2C3E50"       # Fondo principal
BTN_COLOR = "#3498DB"      # Azul botones
BTN_HOVER = "#2980B9"      # Azul más oscuro hover
TEXT_COLOR = "white"       # Texto blanco
ACCENT_COLOR = "#1ABC9C"   # Verde acento

# ====== Funciones de hover para botones ======
def on_enter(e):
    e.widget['background'] = BTN_HOVER

def on_leave(e):
    e.widget['background'] = BTN_COLOR

def crear_boton(parent, texto, comando):
    btn = tk.Button(parent, text=texto, command=comando, 
                    bg=BTN_COLOR, fg=TEXT_COLOR, 
                    activebackground=BTN_HOVER, activeforeground=TEXT_COLOR,
                    font=("Arial", 11, "bold"), width=30, relief="flat", padx=5, pady=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

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

    ventana = tk.Toplevel(root, bg=BG_COLOR)
    ventana.title("Conversión de Temperaturas")
    tk.Label(ventana, text="Temperatura en °C:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11)).pack(pady=5)
    entry = tk.Entry(ventana, font=("Arial", 11))
    entry.pack(pady=5)
    crear_boton(ventana, "Convertir", calcular).pack(pady=10)

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

    ventana = tk.Toplevel(root, bg=BG_COLOR)
    ventana.title("Promedio de Calificaciones")

    tk.Label(ventana, text="Ingresa calificación:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11)).pack(pady=5)
    entry = tk.Entry(ventana, font=("Arial", 11))
    entry.pack(pady=5)
    crear_boton(ventana, "Agregar", agregar).pack(pady=5)
    crear_boton(ventana, "Calcular Promedio", calcular_promedio).pack(pady=5)
    lista = tk.Listbox(ventana, font=("Arial", 11))
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

    ventana = tk.Toplevel(root, bg=BG_COLOR)
    ventana.title("Pago Semanal")

    tk.Label(ventana, text="Horas trabajadas:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11)).pack(pady=5)
    entry_horas = tk.Entry(ventana, font=("Arial", 11))
    entry_horas.pack(pady=5)

    tk.Label(ventana, text="Pago por hora:", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 11)).pack(pady=5)
    entry_pago = tk.Entry(ventana, font=("Arial", 11))
    entry_pago.pack(pady=5)

    crear_boton(ventana, "Calcular Pago", calcular_pago).pack(pady=10)

# ====== Ventana Principal ======
root = tk.Tk()
root.title("Menú de Ejercicios en Python")
root.geometry("400x350")
root.config(bg=BG_COLOR)

tk.Label(root, text="Selecciona un ejercicio", bg=BG_COLOR, fg=ACCENT_COLOR, 
         font=("Arial", 14, "bold")).pack(pady=20)

crear_boton(root, "Conversión de Temperaturas", convertir_temp).pack(pady=5)
crear_boton(root, "Promedio de Calificaciones", promedio_calificaciones).pack(pady=5)
crear_boton(root, "Pago Semanal de un Trabajador", pago_semanal).pack(pady=5)

btn_salir = tk.Button(root, text="Salir", command=root.quit,
                      bg="red", fg=TEXT_COLOR,
                      font=("Arial", 11, "bold"), width=30, relief="flat", padx=5, pady=5)
btn_salir.pack(pady=20)

root.mainloop()
