import tkinter as tk
from tkinter import messagebox

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

ventana = tk.Tk()
ventana.title("Pago Semanal")

tk.Label(ventana, text="Horas trabajadas:").pack(pady=5)
entry_horas = tk.Entry(ventana)
entry_horas.pack(pady=5)

tk.Label(ventana, text="Pago por hora:").pack(pady=5)
entry_pago = tk.Entry(ventana)
entry_pago.pack(pady=5)

tk.Button(ventana, text="Calcular Pago", command=calcular_pago).pack(pady=10)

ventana.mainloop()
