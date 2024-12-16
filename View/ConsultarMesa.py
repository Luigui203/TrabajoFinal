import tkinter as tk
from tkinter import messagebox
from Controller.Mesero import Mesero

class ConsultarMesa:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        self.master.withdraw()

        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Consultar Mesa")
        self.nueva_ventana.geometry("400x300")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Evento para mostrar la ventana principal al cerrar
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Título de la ventana
        titulo = tk.Label(self.nueva_ventana, text="Consultar Mesa", font=("Helvetica", 16))
        titulo.pack(pady=10)

        # Frame para el formulario
        frame_form = tk.Frame(self.nueva_ventana)
        frame_form.pack(pady=10, padx=20)

        # Etiqueta y entrada para el ID de la mesa a buscar
        tk.Label(frame_form, text="ID de Mesa").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id = tk.Entry(frame_form)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Cantidad de comensales").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_comensales = tk.Entry(frame_form, state="disabled")
        self.entry_comensales.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Estado").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_estado = tk.Entry(frame_form, state="disabled")
        self.entry_estado.grid(row=2, column=1, padx=5, pady=5)

        # Botones de Buscar y Salir
        frame_buttons = tk.Frame(self.nueva_ventana)
        frame_buttons.pack(pady=10)

        btn_buscar = tk.Button(frame_buttons, text="Buscar", command=self.buscar_mesa)
        btn_buscar.pack(side=tk.LEFT, padx=10)

        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.salir)
        btn_salir.pack(side=tk.RIGHT, padx=10)

        # Instancia del controlador Mesero
        self.mesero = Mesero()

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual

    def buscar_mesa(self):
        """Buscar una mesa por su ID e ingresar la información en los campos correspondientes"""
        id_mesa = self.entry_id.get()

        if not id_mesa:
            messagebox.showwarning("Advertencia", "Por favor ingrese el ID de la mesa.")
            return

        mesa = self.mesero.buscar_mesa(id_mesa)

        if mesa:
            comensales, estado = mesa
            self.entry_comensales.config(state="normal")
            self.entry_estado.config(state="normal")

            self.entry_comensales.delete(0, tk.END)
            self.entry_estado.delete(0, tk.END)

            self.entry_comensales.insert(0, comensales)
            self.entry_estado.insert(0, estado)

            self.entry_comensales.config(state="disabled")
            self.entry_estado.config(state="disabled")
        else:
            messagebox.showerror("Error", "Mesa no encontrada.")

    def salir(self):
        """Cerrar la ventana actual y restaurar la ventana principal"""
        self.on_close()
