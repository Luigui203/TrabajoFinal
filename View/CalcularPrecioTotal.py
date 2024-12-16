import tkinter as tk
from tkinter import messagebox as mb
from Controller.Registrador import Registrador

class CalcularPrecioTotal:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        self.master.withdraw()  # Ocultar la ventana principal

        # Crear una nueva ventana
        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Calcular Precio Total")
        self.nueva_ventana.geometry("400x300")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Evento para mostrar la ventana principal al cerrar
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Centrar el título "Calcular Precio Total"
        titulo = tk.Label(self.nueva_ventana, text="Calcular Precio Total", font=("Helvetica", 16))
        titulo.pack(pady=10)

        # Crear un frame para el formulario
        frame_form = tk.Frame(self.nueva_ventana)
        frame_form.pack(pady=10)

        # Crear y colocar los widgets del formulario en una cuadrícula
        tk.Label(frame_form, text="ID Comanda*").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_comanda = tk.Entry(frame_form)
        self.entry_id_comanda.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Precio Total*").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.label_precio_total = tk.Label(frame_form, text="0.00")  # Mostrar el precio total aquí
        self.label_precio_total.grid(row=1, column=1, padx=5, pady=5)

        # Crear un frame para los botones
        frame_buttons = tk.Frame(self.nueva_ventana)
        frame_buttons.pack(pady=10)

        # Botón Calcular
        btn_calcular = tk.Button(frame_buttons, text="Calcular Total", command=self.calcular_precio_total)
        btn_calcular.grid(row=0, column=0, padx=10)

        # Botón Salir
        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.on_close)
        btn_salir.grid(row=0, column=1, padx=10)

        self.registrador = Registrador()

        self.nueva_ventana.bind("<Return>", self.enter_pressed)

    def enter_pressed(self, event):
        if self.entry_id_comanda.get(): 
            self.calcular_precio_total(event)

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual

    def calcular_precio_total(self, event=None):
        """Calcular el precio total de la comanda y mostrarlo."""
        id_comanda = self.entry_id_comanda.get()
        if not id_comanda:
            mb.showwarning("Advertencia", "Por favor ingrese el ID de la comanda.")
            return

        try:
            # Consultar el precio total de la comanda usando el mesero
            precio_total = self.registrador.calcular_precio_total(id_comanda)
            if precio_total is None:
                mb.showerror("Error", "Comanda no encontrada o sin platos asociados.")
            else:
                # Mostrar el precio total en la interfaz
                self.label_precio_total.config(text=f"{precio_total:.2f}")
        except Exception as e:
            mb.showerror("Error", f"Error al calcular el precio total: {e}")
