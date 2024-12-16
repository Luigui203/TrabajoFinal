import tkinter as tk
from tkinter import messagebox
from Controller.Registrador import Registrador  # Asegúrate de tener la clase Cajero en la carpeta Controller.
from Controller.Chef import Chef  # Asegúrate de tener la clase Chef en la carpeta Controller.

class AgregarChef:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario  # El usuario que es el Cajero

        self.master.withdraw()

        # Crear una nueva ventana
        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Registrar Chef")
        self.nueva_ventana.geometry("400x300")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Evento para mostrar la ventana principal al cerrar
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Centrar el título "Registrar Chef"
        titulo = tk.Label(self.nueva_ventana, text="Registrar Chef", font=("Helvetica", 16))
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
        btn_guardar = tk.Button(frame_buttons, text="Guardar", command=self.guardar_chef)
        btn_guardar.grid(row=0, column=0, padx=10)

        # Botón Salir
        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.on_close)
        btn_salir.grid(row=0, column=1, padx=10)

        self.nueva_ventana.bind("<Return>", self.enter_pressed)

    def enter_pressed(self, event):
        if self.entry_cedula.get() and self.entry_nombre.get() and self.entry_apellido.get() and self.entry_telefono.get() and self.entry_email.get():  # Si los campos están llenos
            self.guardar_chef(event)

    def mostrar_mensaje_error(self, mensaje):
        """Mostrar un mensaje de error."""
        messagebox.showerror("Error", mensaje)

    def validar_campos(self):
        """Validar todos los campos antes de proceder con la operación."""
        # Obtener valores de los campos de entrada
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        telefono = self.entry_telefono.get()
        email = self.entry_email.get()

        # Validar que los campos no estén vacíos
        if not cedula or not nombre or not apellido or not telefono or not email:
            self.mostrar_mensaje_error("Todos los campos son obligatorios")
            return False

        # Validar que la cédula sea un número entero positivo y tenga al menos 5 dígitos
        try:
            cedula_int = int(cedula)
            if cedula_int <= 0 or len(cedula) < 5:
                raise ValueError
        except ValueError:
            self.mostrar_mensaje_error("La cédula debe ser un número entero positivo con al menos 5 dígitos")
            return False

        # Validar que el teléfono sea numérico
        if not telefono.isdigit():
            self.mostrar_mensaje_error("El teléfono debe contener solo números")
            return False

        # Validar que el nombre y apellido contengan solo letras
        if not nombre.isalpha() or not apellido.isalpha():
            self.mostrar_mensaje_error("El nombre y el apellido deben contener solo letras")
            return False

        if len(nombre) < 5:
            self.mostrar_mensaje_error("El nombre debe tener al menos 5 letras")
            return False

        # Validar el formato del correo electrónico
        if "@" not in email or "." not in email:
            self.mostrar_mensaje_error("El correo no es válido.")
            return False

        return True

    def guardar_chef(self, event=None):
        """Guardar un nuevo chef, si los campos son válidos."""
        if not self.validar_campos():
            return

        # Obtener valores de los campos
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        telefono = self.entry_telefono.get()
        email = self.entry_email.get()

        cajero = Registrador()

        cajero.AgregarChef(cedula, nombre, apellido, telefono, email)


    def actualizar_chef(self, cedula):
        """Actualizar los datos del chef con la cédula proporcionada."""
        if not self.validar_campos():
            return

        # Obtener los nuevos datos
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        telefono = self.entry_telefono.get()
        email = self.entry_email.get()

        # Crear el chef y actualizar sus datos
        chef = Chef(cedula, nombre, apellido, telefono, email)
        chef.actualizar_chef()  # Método que maneja la actualización en la base de datos

        messagebox.showinfo("Éxito", "Chef actualizado exitosamente.")

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual
