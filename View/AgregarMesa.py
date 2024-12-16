import tkinter as tk
from tkinter import messagebox
from Controller.Registrador import Registrador

class AgregarMesa:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        self.master.withdraw()

        # Crear una nueva ventana
        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Registrar Mesero")
        self.nueva_ventana.geometry("400x300")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Evento para mostrar la ventana principal al cerrar
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Centrar el título "Registrar Chef"
        titulo = tk.Label(self.nueva_ventana, text="Registrar Mesa", font=("Helvetica", 16))
        titulo.pack(pady=10)

        # Crear un frame para el formulario
        frame_form = tk.Frame(self.nueva_ventana)
        frame_form.pack(pady=10)

        # Crear y colocar los widgets del formulario en una cuadrícula
        tk.Label(frame_form, text="IdMesa*").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_IdMesa = tk.Entry(frame_form)
        self.entry_IdMesa.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="CantidadComensales*").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_CantidadComensales = tk.Entry(frame_form)
        self.entry_CantidadComensales.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Estado*").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_Estado = tk.Entry(frame_form)
        self.entry_Estado.grid(row=2, column=1, padx=5, pady=5)
        self.entry_Estado.insert(0, "libre")
        self.entry_Estado.config(state="disabled")

        # Crear un frame para los botones
        frame_buttons = tk.Frame(self.nueva_ventana)
        frame_buttons.pack(pady=10)

        # Botón Guardar
        btn_guardar = tk.Button(frame_buttons, text="Guardar", command=self.guardar_Mesa)
        btn_guardar.grid(row=0, column=0, padx=10)

        # Botón Salir
        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.on_close)
        btn_salir.grid(row=0, column=1, padx=10)

        self.nueva_ventana.bind("<Return>", self.enter_pressed)

    def enter_pressed(self, event):
        if self.entry_IdMesa.get() and self.entry_CantidadComensales.get() and self.entry_Estado.get():  # Si los campos están llenos
            self.guardar_Mesa(event)

    def guardar_Mesa(self, event=None):
        # Obtener valores de los campos de entrada
        IdMesa = self.entry_IdMesa.get()
        CantidadComensales = self.entry_CantidadComensales.get()
        Estado = self.entry_Estado.get()

        # Validar que los campos no estén vacíos
        if not IdMesa or not CantidadComensales or not Estado:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        # Validar que la id sea un número entero positivo
        try:
            id_int = int(IdMesa)
            if id_int <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El id debe ser un número entero positivo")
            return

        # Validar que los comensales no sean más de 6
        try:
            comensales_int = int(CantidadComensales)
            if comensales_int <= 0 or comensales_int > 6:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "La cantidad de comensales debe ser un número entero positivo y no mayor a 6")
            return

        # Validar que el IdMesa no se repita
        registrador = Registrador()
    
        # Registrar la mesa
        registrador.AgregarMesa(IdMesa, CantidadComensales, Estado)
        

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual
