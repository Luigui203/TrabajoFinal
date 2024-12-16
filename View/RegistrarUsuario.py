import tkinter as tk
from tkinter import messagebox
from Controller.Usuario import Usuario
from Tooltip import Tooltip
import re

class RegistrarUsuario:
    def __init__(self, ventana_padre):
        self.ventana_padre = ventana_padre  # Guardamos la ventana padre (Login)
        self.ventana = tk.Toplevel(ventana_padre)  # Crear una nueva ventana sobre la ventana de login
        self.ventana.resizable(0, 0)
        self.ventana.config(width=440, height=350)
        self.ventana.title("Registro de Usuario")
        self.ventana.iconbitmap(r"iconos\valle.ico")
        
        # Etiquetas
        self.lblTitulo = tk.Label(self.ventana, text="Registro de Usuario", font=("Helvetica", 14, "bold"))
        self.lblTitulo.place(relx=0.5, y=30, anchor="center")

        self.lblCedula = tk.Label(self.ventana, text="Cédula*: ")
        self.lblCedula.place(x=100, y=75, width=70, height=25)

        self.lblNombre = tk.Label(self.ventana, text="Nombre*: ")
        self.lblNombre.place(x=100, y=125, width=70, height=25)

        self.lblApellido = tk.Label(self.ventana, text="Apellido*: ")
        self.lblApellido.place(x=100, y=175, width=70, height=25)

        self.lblTelefono = tk.Label(self.ventana, text="Teléfono*: ")
        self.lblTelefono.place(x=100, y=225, width=70, height=25)

        self.lblEmail = tk.Label(self.ventana, text="Email*: ")
        self.lblEmail.place(x=100, y=275, width=70, height=25)

        # Campos de entrada
        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(x=190, y=75, width=150, height=25)
        Tooltip(self.txtCedula, "Ingrese su número de cédula. Debe ser numérico y mínimo 5 caracteres.")

        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(x=190, y=125, width=150, height=25)
        Tooltip(self.txtNombre, "Ingrese su nombre. Mínimo 5 letras.")

        self.txtApellido = tk.Entry(self.ventana)
        self.txtApellido.place(x=190, y=175, width=150, height=25)
        Tooltip(self.txtApellido, "Ingrese su apellido. Solo letras.")

        self.txtTelefono = tk.Entry(self.ventana)
        self.txtTelefono.place(x=190, y=225, width=150, height=25)
        Tooltip(self.txtTelefono, "Ingrese su número de teléfono. Debe ser numérico.")

        self.txtEmail = tk.Entry(self.ventana)
        self.txtEmail.place(x=190, y=275, width=150, height=25)
        Tooltip(self.txtEmail, "Ingrese su correo electrónico en formato válido (ejemplo@correo.com).")

        # Botones
        self.btnRegistrar = tk.Button(self.ventana, text="Registrar", command=self.registrar_usuario)
        self.btnRegistrar.place(x=140, y=310, width=70, height=25)
        Tooltip(self.btnRegistrar, "Haz clic o pulsa (Enter) para registrar los datos del usuario.")

        self.btnCancelar = tk.Button(self.ventana, text="Cancelar", command=self.volver_a_login)
        self.btnCancelar.place(x=230, y=310, width=70, height=25)
        Tooltip(self.btnCancelar, "Haz clic para cancelar el registro y volver a la pantalla de inicio de sesión.")

        self.ventana.bind("<Return>", self.enter_pressed)

    def enter_pressed(self, event):
        if self.txtCedula.get() and self.txtNombre.get() and self.txtApellido.get() and self.txtTelefono.get() and self.txtEmail.get():  # Si los campos están llenos
            self.registrar_usuario(event)


    def volver_a_login(self):
        """Cerrar la ventana de registro y regresar al login"""
        self.ventana.destroy()
        self.ventana_padre.deiconify()  # Mostrar la ventana de login

    def validar_cedula(self, cedula):
        """Validar que la cédula sea numérica y tenga al menos 5 caracteres"""
        if not cedula.isdigit():
            return "La cédula solo debe contener números."
        if len(cedula) < 5:
            return "La cédula debe tener al menos 5 caracteres."
        return None

    def validar_nombre(self, nombre):
        """Validar que el nombre solo contenga letras y tenga al menos 5 caracteres"""
        if len(nombre) < 5:
            return "El nombre debe tener al menos 5 caracteres."
        if not nombre.isalpha():
            return "El nombre solo debe contener letras."
        return None

    def validar_apellido(self, apellido):
        """Validar que el apellido solo contenga letras"""
        if not apellido.isalpha():
            return "El apellido solo debe contener letras."
        return None

    def validar_telefono(self, telefono):
        """Validar que el teléfono solo contenga números"""
        if not telefono.isdigit():
            return "El teléfono solo debe contener números."
        return None

    def validar_email(self, email):
        """Validar formato del correo electrónico"""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            return "El correo electrónico no es válido."
        return None

    def registrar_usuario(self, event=None):
        cedula = self.txtCedula.get()
        nombre = self.txtNombre.get()
        apellido = self.txtApellido.get()
        telefono = self.txtTelefono.get()
        email = self.txtEmail.get()

        # Verificar si algún campo está vacío
        if not cedula or not nombre or not apellido or not telefono or not email:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        # Validaciones de los campos
        mensaje_error = self.validar_cedula(cedula)
        if not mensaje_error:
            mensaje_error = self.validar_nombre(nombre)
        if not mensaje_error:
            mensaje_error = self.validar_apellido(apellido)
        if not mensaje_error:
            mensaje_error = self.validar_telefono(telefono)
        if not mensaje_error:
            mensaje_error = self.validar_email(email)

        if mensaje_error:
            messagebox.showwarning("Advertencia", mensaje_error)
            return

        # Si todas las validaciones pasan, se crea una instancia de Usuario y se registra
        usuario = Usuario()
        rol = "Registrador"  # Rol por defecto

        # Registrar el usuario en la base de datos
        resultado = usuario.registrar_usuario(cedula, nombre, apellido, telefono, email, rol)

        # Mostrar el resultado
        if resultado:
            messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
            self.volver_a_login()  # Volver al login
