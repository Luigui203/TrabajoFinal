import tkinter as tk
from tkinter import messagebox
from View.AgregarPlato import AgregarPlato
from View.EliminarPlato import EliminarPlato
from View.ServirComanda import ServirComanda

class MenuChef:


    def AgregarPlato(self):
        agregar = AgregarPlato(self.ventana,self.usuario)

    def EliminarPlato(self):
        eliminar = EliminarPlato(self.ventana,self.usuario)

    def ServirComanda(self):
        servir = ServirComanda(self.ventana,self.usuario)

    def volver_a_login(self):
        """Cierra la ventana actual y abre el inicio de sesión."""
        self.ventana.destroy()  # Cerrar la ventana actual
        from View.Loggin import Loggin  # Mover la importación aquí
        Loggin()  # Abrir la ventana de inicio de sesión

    def __init__(self, usuario):
        self.ventana = tk.Tk()
        self.ventana.geometry("300x250")
        self.ventana.title("Menu Chef")
        self.ventana.resizable(0, 0)
        self.ventana.focus_set()
        self.ventana.iconbitmap(r"iconos\valle.ico")

        self.usuario = usuario

        self.lblTitulo = tk.Label(self.ventana, text=f"Bienvenido Chef {usuario}")
        self.lblTitulo.pack()

        self.menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu)

        # Menú Gestionar Platos
        gestionar_platos_menu = tk.Menu(self.menu, tearoff=0)
        gestionar_platos_menu.add_command(label="Agregar Plato", command=self.AgregarPlato)
        gestionar_platos_menu.add_command(label="Eliminar Plato", command=self.EliminarPlato)
        self.menu.add_cascade(label="Gestionar Platos", menu=gestionar_platos_menu)

        # Menú Gestionar Comandas
        gestionar_comandas_menu = tk.Menu(self.menu, tearoff=0)
        gestionar_comandas_menu.add_command(label="Servir Comanda", command=self.ServirComanda)
        self.menu.add_cascade(label="Gestionar Comandas", menu=gestionar_comandas_menu)

        volver_login = tk.Menu(self.menu, tearoff=0)
        volver_login.add_command(label="Volver al loggin", command=self.volver_a_login)
        self.menu.add_cascade(label="Salir", menu=volver_login)




        self.ventana.mainloop()

