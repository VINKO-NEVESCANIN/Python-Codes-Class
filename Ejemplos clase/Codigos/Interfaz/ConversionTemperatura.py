import tkinter as tk
from tkinter import messagebox

def convertir():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        messagebox.showinfo("Resultado",
                            f"{celsius} °C = {fahrenheit:.2f} °F\n"
                            f"{celsius} °C = {kelvin:.2f} K")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido")

ventana = tk.Tk()
ventana.title("Conversión de Temperaturas")

tk.Label(ventana, text="Temperatura en °C:").pack(pady=5)
entry = tk.Entry(ventana)
entry.pack(pady=5)

tk.Button(ventana, text="Convertir", command=convertir).pack(pady=10)

ventana.mainloop()
