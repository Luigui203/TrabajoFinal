import tkinter as tk
from tkinter import messagebox
from View.AgregarCliente import AgregarCliente
from View.EliminarCliente import EliminarCliente
from View.ConsultarMesa import ConsultarMesa
from View.OcuparMesa import OcuparMesa
from View.LiberarMesa import LiberarMesa
from View.TomarComanda import TomarComanda
from View.AgregarPlatoComanda import AgregarPlatoComanda
from View.EliminarPlatoComanda import EliminarPlatoComanda
from View.EnviarComandaChef import EnviarComandaChef

class MenuMesero:

    def AgregarCliente(self):
        agregar = AgregarCliente(self.ventana, self.usuario)
    
    def EliminarCliente(self):
        eliminar = EliminarCliente(self.ventana, self.usuario)

    def ConsultarMesa(self):
        consultar = ConsultarMesa(self.ventana,self.usuario)

    def OcuparMesa(self):
        ocupar = OcuparMesa(self.ventana, self.usuario)

    def LiberarMesa(self):
        liberar = LiberarMesa(self.ventana, self.usuario)

    def TomarComanda(self):
        Tomar = TomarComanda(self.ventana, self.usuario)

    def AgregarPlatoComanda(self):
        agregar = AgregarPlatoComanda(self.ventana, self.usuario)

    def EliminarPlatoComanda(self):
        eliminar = EliminarPlatoComanda(self.ventana, self.usuario)

    def EnviarComandaChef(self):
        enviar = EnviarComandaChef(self.ventana, self.usuario)

    def volver_al_loggin(self):
        """Cierra la ventana actual y abre el inicio de sesión."""
        self.ventana.destroy()  # Cerrar la ventana actual
        from View.Loggin import Loggin  # Mover la importación aquí
        Loggin()  # Abrir la ventana de inicio de sesión

    def __init__(self,usuario):
        self.ventana = tk.Tk()
        self.ventana.geometry("400x450")
        self.ventana.title(f"Menú Mesero - {usuario}")
        self.ventana.resizable(0, 0)
        self.ventana.focus_set()
        self.ventana.iconbitmap(r"iconos\valle.ico")

        self.usuario = usuario

        self.lblTitulo = tk.Label(self.ventana, text=f"Bienvenido Mesero {usuario}")
        self.lblTitulo.pack()

        self.menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu)

        # Menú Gestionar Clientes
        gestionar_clientes_menu = tk.Menu(self.menu, tearoff=0)
        gestionar_clientes_menu.add_command(label="Agregar Cliente", command=self.AgregarCliente)
        gestionar_clientes_menu.add_command(label="Eliminar Cliente", command=self.EliminarCliente)
        self.menu.add_cascade(label="Gestionar Clientes", menu=gestionar_clientes_menu)

        # Menú Gestionar Mesas
        gestionar_mesas_menu = tk.Menu(self.menu, tearoff=0)
        gestionar_mesas_menu.add_command(label="Consultar Mesa", command=self.ConsultarMesa)
        gestionar_mesas_menu.add_command(label="Ocupar Mesa", command=self.OcuparMesa)
        gestionar_mesas_menu.add_command(label="Liberar Mesa", command=self.LiberarMesa)
        self.menu.add_cascade(label="Gestionar Mesas", menu=gestionar_mesas_menu)

        # Menú Gestionar Comandas
        gestionar_comandas_menu = tk.Menu(self.menu, tearoff=0)
        gestionar_comandas_menu.add_command(label="Tomar Comanda", command=self.TomarComanda)
        gestionar_comandas_menu.add_command(label="Agregar Plato Comanda", command=self.AgregarPlatoComanda)
        gestionar_comandas_menu.add_command(label="Eliminar Plato Comanda", command=self.EliminarPlatoComanda)
        gestionar_comandas_menu.add_command(label="Enviar Comanda", command=self.EnviarComandaChef)
        self.menu.add_cascade(label="Gestionar Comandas", menu=gestionar_comandas_menu)

        # Menú Salir
        salir_menu = tk.Menu(self.menu, tearoff=0)
        salir_menu.add_command(label="Salir", command=self.volver_al_loggin)
        self.menu.add_cascade(label="Salir", menu=salir_menu)

        self.ventana.mainloop()


    def salirApp(self):
        respuesta = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
        if respuesta == "yes":
            self.ventana.destroy()


