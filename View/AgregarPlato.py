import tkinter as tk
from tkinter import messagebox
from Controller.Chef import Chef  # Importamos la clase Chef

class AgregarPlato:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        self.master.withdraw()

        # Crear una nueva ventana
        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Agregar Plato")
        self.nueva_ventana.geometry("400x400")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Evento para mostrar la ventana principal al cerrar
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Centrar el título "Agregar Plato"
        titulo = tk.Label(self.nueva_ventana, text="Agregar Plato", font=("Helvetica", 16))
        titulo.pack(pady=10)

        # Crear un frame para el formulario
        frame_form = tk.Frame(self.nueva_ventana)
        frame_form.pack(pady=10)

        # Crear y colocar los widgets del formulario en una cuadrícula
        tk.Label(frame_form, text="ID*").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id = tk.Entry(frame_form)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Nombre*").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame_form)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Precio*").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_precio = tk.Entry(frame_form)
        self.entry_precio.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Cantidad Disponible*").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_cantidad = tk.Entry(frame_form)
        self.entry_cantidad.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Descripción*").grid(row=4, column=0, padx=5, pady=10, sticky="e")
        self.entry_descripcion = tk.Entry(frame_form)
        self.entry_descripcion.grid(row=4, column=1, padx=5, pady=10)

        # Crear un frame para los botones
        frame_buttons = tk.Frame(self.nueva_ventana)
        frame_buttons.pack(pady=10)

        # Botón Guardar
        btn_guardar = tk.Button(frame_buttons, text="Guardar", command=self.guardar_plato)
        btn_guardar.grid(row=0, column=0, padx=10)

        # Botón Salir
        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.on_close)
        btn_salir.grid(row=0, column=1, padx=10)

        self.nueva_ventana.bind("<Return>", self.enter_pressed)

    def enter_pressed(self, event):
        if self.entry_id.get() and self.entry_nombre.get() and self.entry_precio.get() and self.entry_cantidad.get() and self.entry_descripcion.get():  # Si los campos están llenos
            self.guardar_plato(event)

    def guardar_plato(self, event=None):
        # Recoger los datos ingresados por el usuario
        id_plato = self.entry_id.get()
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        cantidad = self.entry_cantidad.get()
        descripcion = self.entry_descripcion.get()

        # Validar que los campos no estén vacíos
        if not id_plato or not nombre or not precio or not cantidad or not descripcion:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Verificar que el ID sea un número entero positivo
        try:
            id_int = int(id_plato)
            if id_int <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número entero positivo")
            return

        # Verificar que el precio sea un número positivo
        try:
            precio_float = float(precio)
            if precio_float <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número positivo")
            return

        # Verificar que la cantidad sea un número entero positivo
        try:
            cantidad_int = int(cantidad)
            if cantidad_int <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero positivo")
            return

        # Verificar que el nombre contenga solo letras
        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El nombre del plato debe contener solo letras")
            return
        
        # Crear una instancia de Chef
        chef = Chef()
        
        # Llamar al método de agregar plato
        chef.agregar_plato(id_plato, nombre, precio, cantidad, descripcion)

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual    