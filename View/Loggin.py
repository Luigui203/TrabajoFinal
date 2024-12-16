import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Controller.Usuario import Usuario
from View.MenuChef import MenuChef
from View.MenuMesero import MenuMesero
from View.MenuRegistrador import MenuRegistrador
from View.RegistrarUsuario import RegistrarUsuario
from Tooltip import Tooltip
import mariadb

class Loggin():
    def validarCampos(self, event):
        if len(self.txtUsuario.get()) >= 5 and len(self.txtPassword.get()) >= 5:
            if len(self.txtUsuario.get()) <= 25 and len(self.txtPassword.get()) <= 25:
                self.btnIngresar.config(state="normal")
            elif len(self.txtUsuario.get()) <= 25 and len(self.txtPassword.get()) >= 25:
                self.txtPassword.delete(len(self.txtPassword.get()) - 1, END)
            elif len(self.txtUsuario.get()) >= 25 and len(self.txtPassword.get()) <= 25:
                self.txtUsuario.delete(len(self.txtUsuario.get()) - 1, END)
        else:
            self.btnIngresar.config(state="disabled")

    def validarUsuario(self, event):
        caracter = event.keysym
        if caracter.isalpha() or caracter == '.' or caracter == "BackSpace":
            self.txtUsuario.config(bg="#ffffff", fg="#000000")
        
    def verCaracteres(self, event):
        if self.bandera == True:
            self.txtPassword.config(show='*')
            self.btnVer.config(text="Ver")
            self.bandera = False
        else:
            self.txtPassword.config(show='')
            self.btnVer.config(text="Ocu")
            self.bandera = True

    def ingresar(self, event):
        try:
            miUsuario = Usuario()
            usuario = self.txtUsuario.get()
            rol = miUsuario.iniciarSesion(usuario, self.txtPassword.get(), self.ventana)

            if rol:
                # Destruir la ventana del login
                self.ventana.destroy()
                
                # Abrir la ventana correspondiente al rol
                if rol == 'Chef':
                    MenuChef(usuario)  # Crear ventana del Chef
                elif rol == 'Mesero':
                    MenuMesero(usuario)
                else:
                    MenuRegistrador(usuario)
            else:
                messagebox.showwarning("Advertencia", "Usuario o contraseña incorrectos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al intentar ingresar: {e}")



    def limpiarCampos(self):
        # Limpiar los campos de texto
        self.txtUsuario.delete(0, END)
        self.txtPassword.delete(0, END)

    def abrirVentanaRegistro(self):
        """Abre la ventana de registro de usuario"""
        self.ventana.withdraw()  # Oculta la ventana de inicio de sesión
        registrar_ventana = RegistrarUsuario(self.ventana)  # Crea la ventana de registro
        registrar_ventana.ventana.mainloop()


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0, 0)
        self.ventana.config(width=440, height=350)
        self.ventana.title("Inicio de Sesión")
        self.ventana.iconbitmap(r"iconos\valle.ico")
        self.inicio_exitoso = False  # Bandera para verificar inicio de sesión exitoso

        self.bandera = False
        self.caracteresUsuario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.']
        self.caracteresPassword = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Título
        self.lblTitulo = tk.Label(self.ventana, text="Inicio Sesión", font=("Helvetica", 16, "bold"))
        self.lblTitulo.place(relx=0.5, y=50, anchor="center")

        # Usuario
        self.lblUsuario = tk.Label(self.ventana, text="Usuario*: ")
        self.lblUsuario.place(x=100, y=125, width=70, height=25)

        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(x=190, y=125, width=150, height=25)
        self.txtUsuario.bind("<KeyRelease>", self.validarCampos)
        self.txtUsuario.bind("<Key>", self.validarUsuario)
        Tooltip(self.txtUsuario, "Ingrese su nombre de usuario (mínimo 5 caracteres).")

        # Contraseña
        self.lblPassword = tk.Label(self.ventana, text="Password*: ")
        self.lblPassword.place(x=100, y=200, width=70, height=25)

        self.txtPassword = tk.Entry(self.ventana, show="*")
        self.txtPassword.place(x=190, y=200, width=150, height=25)
        self.txtPassword.bind("<KeyRelease>", self.validarCampos)
        Tooltip(self.txtPassword, "Ingrese su contraseña (mínimo 5 caracteres).")

        # Botones
        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", state="disabled")
        self.btnIngresar.place(x=140, y=275, width=70, height=25)
        self.btnIngresar.bind("<Button-1>", self.ingresar)
        Tooltip(self.btnIngresar, "Inicia sesión con tu usuario y contraseña.")

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", command=self.limpiarCampos)
        self.btnLimpiar.place(x=230, y=275, width=70, height=25)
        Tooltip(self.btnLimpiar, "Limpia los campos de texto.")

        self.btnRegistrarse = tk.Button(self.ventana, text="Registrarse", command=self.abrirVentanaRegistro)
        self.btnRegistrarse.place(x=320, y=275, width=90, height=25)
        Tooltip(self.btnRegistrarse, "Regístrate como nuevo usuario.")

        self.btnVer = tk.Button(self.ventana, text="Ver")
        self.btnVer.place(x=360, y=200, width=30, height=25)
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)
    

        self.ventana.mainloop()


