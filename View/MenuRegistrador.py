import tkinter as tk
from tkinter import messagebox
from View.AgregarChef import AgregarChef  
from View.EliminarChef import EliminarChef  
from View.AgregarMesero import AgregarMesero
from View.EliminarMesero import EliminarMesero
from View.AgregarMesa import AgregarMesa
from View.EliminarMesa import EliminarMesa
from View.CalcularPrecioTotal import CalcularPrecioTotal
from View.InformeDiarioComandas import InformeDiario

class MenuRegistrador:
    def AgregarChef(self):
        agregar = AgregarChef(self.ventana, self.usuario)

    def EliminarChef(self):
        eliminar = EliminarChef(self.ventana, self.usuario)

    def AgregarMesero(self):
        agregar = AgregarMesero(self.ventana, self.usuario)

    def EliminarMesero(self):
        eliminar = EliminarMesero(self.ventana, self.usuario)

    def AgregarMesa(self):
        agregar = AgregarMesa(self.ventana, self.usuario)

    def EliminarMesa(self):
        eliminar = EliminarMesa(self.ventana, self.usuario)

    def CalcularPrecioTotal(self):
        calcular = CalcularPrecioTotal(self.ventana, self.usuario)

    def InformeDiarioComandas(self):
        """Abre la ventana de informe diario de comandas."""
        informe = InformeDiario(self.ventana, self.usuario)

    def volver_al_loggin(self):
        """Cierra la ventana actual y abre el inicio de sesión."""
        self.ventana.destroy()  # Cerrar la ventana actual
        from View.Loggin import Loggin  # Mover la importación aquí
        Loggin()  # Abrir la ventana de inicio de sesión

    
    
    def __init__(self, usuario):
        self.ventana = tk.Tk()
        self.ventana.geometry("500x350")
        self.ventana.title("Menú Registrador")
        self.ventana.resizable(0, 0)
        self.ventana.focus_set()
        self.ventana.iconbitmap(r"iconos\valle.ico")

        self.usuario = usuario

        self.lblTitulo = tk.Label(self.ventana, text=f"Bienvenido Registrador {usuario}")
        self.lblTitulo.pack()

        self.menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu)

        # Menú Gestionar Chefs
        gestionar_chefs_menu = tk.Menu(self.menu, tearoff=0)
        gestionar_chefs_menu.add_command(label="Agregar Chef", command=self.AgregarChef)
        gestionar_chefs_menu.add_command(label="Eliminar Chef", command=self.EliminarChef)
        self.menu.add_cascade(label="Gestionar Chefs", menu=gestionar_chefs_menu)

        # Menú Gestionar Meseros
        gestionar_chefs_menu = tk.Menu(self.menu, tearoff=0)
        gestionar_chefs_menu.add_command(label="Agregar Mesero", command=self.AgregarMesero)
        gestionar_chefs_menu.add_command(label="Eliminar Mesero", command=self.EliminarMesero)
        self.menu.add_cascade(label="Gestionar Meseros", menu=gestionar_chefs_menu)

        # Menú Gestionar Mesas
        gestionar_chefs_menu = tk.Menu(self.menu, tearoff=0)
        gestionar_chefs_menu.add_command(label="Agregar Mesa", command=self.AgregarMesa)
        gestionar_chefs_menu.add_command(label="Eliminar Mesa", command=self.EliminarMesa)
        self.menu.add_cascade(label="Gestionar Mesas", menu=gestionar_chefs_menu)

        # Menú Gestionar Comanda
        gestionar_comanda_menu = tk.Menu(self.menu, tearoff=0)
        gestionar_comanda_menu.add_command(label="Calcular precio total", command=self.CalcularPrecioTotal)
        gestionar_comanda_menu.add_command(label="Generar informe diario", command=self.InformeDiarioComandas)
        self.menu.add_cascade(label="Gestionar Comanda", menu=gestionar_comanda_menu)

        # Menú Salir
        salir_menu = tk.Menu(self.menu, tearoff=0)
        salir_menu.add_command(label="Salir", command=self.volver_al_loggin)
        self.menu.add_cascade(label="Salir", menu=salir_menu)

        self.ventana.mainloop()
