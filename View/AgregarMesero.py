import tkinter as tk
from tkinter import messagebox
from Controller.Registrador import Registrador

class AgregarMesero:
    def __init__(self, master,usuario):
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
        titulo = tk.Label(self.nueva_ventana, text="Registrar Mesero", font=("Helvetica", 16))
        titulo.pack(pady=10)

        # Crear un frame para el formulario
        frame_form = tk.Frame(self.nueva_ventana)
        frame_form.pack(pady=10)

        # Crear y colocar los widgets del formulario en una cuadrícula
        tk.Label(frame_form, text="Cédula*").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_cedula = tk.Entry(frame_form)
        self.entry_cedula.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Nombre*").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame_form)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Apellido*").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_apellido = tk.Entry(frame_form)
        self.entry_apellido.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Teléfono*").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_telefono = tk.Entry(frame_form)
        self.entry_telefono.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Email*").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = tk.Entry(frame_form)
        self.entry_email.grid(row=4, column=1, padx=5, pady=5)

        # Crear un frame para los botones
        frame_buttons = tk.Frame(self.nueva_ventana)
        frame_buttons.pack(pady=10)

        # Botón Guardar
        btn_guardar = tk.Button(frame_buttons, text="Guardar", command=self.guardar_Mesero)
        btn_guardar.grid(row=0, column=0, padx=10)

        # Botón Salir
        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.on_close)
        btn_salir.grid(row=0, column=1, padx=10)

        self.nueva_ventana.bind("<Return>", self.enter_pressed)

    def enter_pressed(self, event):
        if self.entry_cedula.get() and self.entry_nombre.get() and self.entry_apellido.get() and self.entry_telefono.get() and self.entry_email.get():  # Si los campos están llenos
            self.guardar_Mesero(event)

    def guardar_Mesero(self, event=None):
        # Obtener valores de los campos de entrada
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        telefono = self.entry_telefono.get()
        email = self.entry_email.get()

        # Validar que los campos no estén vacíos
        if not cedula or not nombre or not apellido or not telefono or not email:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        # Validar que la cédula sea un número entero positivo y tenga al menos 5 dígitos
        try:
            cedula_int = int(cedula)
            if cedula_int <= 0 or len(cedula) < 5:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "La cédula debe ser un número entero positivo con al menos 5 dígitos")
            return

        # Validar que el teléfono sea numérico
        if not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono debe contener solo números")
            return

        # Validar que el nombre y apellido contengan solo letras y que el nombre tenga al menos 5 letras
        if not nombre.isalpha() or not apellido.isalpha():
            messagebox.showerror("Error", "El nombre y el apellido deben contener solo letras")
            return

        if len(nombre) < 5:
            messagebox.showerror("Error", "El nombre debe tener al menos 5 letras")
            return

        # Validar el formato del correo electrónico
        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "El correo no es válido.")
            return

        cajero = Registrador()

        cajero.AgregarMesero(cedula, nombre, apellido, telefono, email)

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual    

