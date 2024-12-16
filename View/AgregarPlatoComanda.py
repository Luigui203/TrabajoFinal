import tkinter as tk
from tkinter import messagebox
from Controller.Mesero import Mesero


class AgregarPlatoComanda:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        self.master.withdraw()

        # Crear una nueva ventana
        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Agregar Plato a Comanda")
        self.nueva_ventana.geometry("400x300")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Evento para mostrar la ventana principal al cerrar
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Título de la ventana
        titulo = tk.Label(self.nueva_ventana, text="Agregar Plato a Comanda", font=("Helvetica", 16))
        titulo.pack(pady=10)

        # Frame para el formulario
        frame_form = tk.Frame(self.nueva_ventana)
        frame_form.pack(pady=10)

        # Etiqueta y entrada para el ID de la comanda
        tk.Label(frame_form, text="ID Comanda*").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_comanda = tk.Entry(frame_form)
        self.entry_id_comanda.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y entrada para el ID del plato
        tk.Label(frame_form, text="ID Plato*").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_plato = tk.Entry(frame_form)
        self.entry_id_plato.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y entrada para la cantidad de platos
        tk.Label(frame_form, text="Cantidad*").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_cantidad = tk.Entry(frame_form)
        self.entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

        # Botones de Guardar y Salir
        frame_buttons = tk.Frame(self.nueva_ventana)
        frame_buttons.pack(pady=10)

        btn_guardar = tk.Button(frame_buttons, text="Agregar Plato", command=self.agregar_plato)
        btn_guardar.pack(side=tk.LEFT, padx=10)

        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.on_close)
        btn_salir.pack(side=tk.RIGHT, padx=10)

        self.mesero = Mesero()

        self.nueva_ventana.bind("<Return>", self.enter_pressed)

    def enter_pressed(self, event):
        if self.entry_id_comanda.get() and self.entry_id_plato.get() and self.entry_cantidad.get():  # Si los campos están llenos
            self.agregar_plato(event)

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual

    def agregar_plato(self):
        """Agregar un plato a la comanda."""
        id_comanda = self.entry_id_comanda.get()
        id_plato = self.entry_id_plato.get()
        cantidad = self.entry_cantidad.get()

        # Validar campos obligatorios
        if not id_comanda or not id_plato or not cantidad:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos obligatorios marcados con *.")
            return

        # Validar que la cantidad sea un número positivo
        if not cantidad.isdigit() or int(cantidad) <= 0:
            messagebox.showwarning("Advertencia", "La cantidad debe ser un número positivo.")
            return

        # Llamar al método del mesero para agregar el plato a la comanda
        resultado = self.mesero.agregar_plato_comanda(id_comanda, id_plato, cantidad)

        if resultado:
            messagebox.showinfo("Éxito", "Plato agregado a la comanda correctamente.")
            self.on_close()  # Cerrar la ventana


