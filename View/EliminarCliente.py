import tkinter as tk
from tkinter import messagebox
from Controller.Mesero import Mesero

class EliminarCliente:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        self.master.withdraw()  # Ocultar la ventana principal de Mesero

        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Eliminar Cliente")
        self.nueva_ventana.geometry("400x300")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Evento para mostrar la ventana principal al cerrar
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        titulo = tk.Label(self.nueva_ventana, text="Eliminar Cliente", font=("Helvetica", 16))
        titulo.pack(pady=10)

        frame_form = tk.Frame(self.nueva_ventana)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Cédula*").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_cedula = tk.Entry(frame_form)
        self.entry_cedula.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Nombre*").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame_form, state="disabled")
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Apellido*").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_apellido = tk.Entry(frame_form, state="disabled")
        self.entry_apellido.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Teléfono*").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_telefono = tk.Entry(frame_form, state="disabled")
        self.entry_telefono.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Email*").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = tk.Entry(frame_form, state="disabled")
        self.entry_email.grid(row=4, column=1, padx=5, pady=5)

        frame_buttons = tk.Frame(self.nueva_ventana)
        frame_buttons.pack(pady=10)

        # Botón Buscar
        btn_buscar = tk.Button(frame_buttons, text="Buscar", command=self.buscar_cliente)
        btn_buscar.grid(row=0, column=0, padx=10)

        # Botón Eliminar
        btn_eliminar = tk.Button(frame_buttons, text="Eliminar", command=self.eliminar_cliente)
        btn_eliminar.grid(row=0, column=1, padx=10)

        # Botón Salir
        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.volver_a_menu_mesero)
        btn_salir.grid(row=0, column=2, padx=10)

        self.mesero = Mesero()  # Instancia de Mesero

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual

    def buscar_cliente(self):
        """Buscar un cliente por cédula"""
        cedula = self.entry_cedula.get()

        if not cedula:
            messagebox.showwarning("Advertencia", "Por favor ingrese una cédula.")
            return

        cliente = self.mesero.buscar_cliente(cedula)

        if cliente:
            nombre, apellido, telefono, email = cliente
            self.entry_nombre.config(state="normal")
            self.entry_apellido.config(state="normal")
            self.entry_telefono.config(state="normal")
            self.entry_email.config(state="normal")

            self.entry_nombre.delete(0, tk.END)
            self.entry_apellido.delete(0, tk.END)
            self.entry_telefono.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)

            self.entry_nombre.insert(0, nombre)
            self.entry_apellido.insert(0, apellido)
            self.entry_telefono.insert(0, telefono)
            self.entry_email.insert(0, email)
        else:
            messagebox.showerror("Error", "Cliente no encontrado.")

    def eliminar_cliente(self):
        """Eliminar cliente de la base de datos"""
        cedula = self.entry_cedula.get()

        if not cedula:
            messagebox.showwarning("Advertencia", "Por favor ingrese una cédula para eliminar.")
            return

        if self.mesero.eliminar_cliente(cedula):
            messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
            self.volver_a_menu_mesero()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el cliente.")

    def volver_a_menu_mesero(self):
        """Vuelve al menú principal de Mesero"""
        # Destruir la ventana actual de eliminar cliente
        self.nueva_ventana.destroy()
        
        # Mostrar la ventana principal de Mesero
        self.master.deiconify()

