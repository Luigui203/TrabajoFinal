import tkinter as tk
from tkinter import messagebox
from Controller.Registrador import Registrador

class EliminarMesa:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        self.master.withdraw()  # Ocultar la ventana principal de cajero

        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Eliminar Mesero")
        self.nueva_ventana.geometry("400x300")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Evento para mostrar la ventana principal al cerrar
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        titulo = tk.Label(self.nueva_ventana, text="Eliminar Mesa", font=("Helvetica", 16))
        titulo.pack(pady=10)

        frame_form = tk.Frame(self.nueva_ventana)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="IdMesa*").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_IdMesa = tk.Entry(frame_form)
        self.entry_IdMesa.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="CantidadComensales*").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_CantidadComensales = tk.Entry(frame_form, state="disabled")
        self.entry_CantidadComensales.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Estado*").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_Estado = tk.Entry(frame_form, state="disabled")
        self.entry_Estado.grid(row=2, column=1, padx=5, pady=5)
        self.entry_Estado.insert(0, "libre")
        self.entry_Estado.config(state="disabled")


        frame_buttons = tk.Frame(self.nueva_ventana)
        frame_buttons.pack(pady=10)

        # Botón Buscar
        btn_buscar = tk.Button(frame_buttons, text="Buscar", command=self.buscar_Mesa)
        btn_buscar.grid(row=0, column=0, padx=10)

        # Botón Eliminar
        btn_eliminar = tk.Button(frame_buttons, text="Eliminar", command=self.eliminar_Mesa)
        btn_eliminar.grid(row=0, column=1, padx=10)

        # Botón Salir
        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.on_close)
        btn_salir.grid(row=0, column=2, padx=10)

        self.cajero = Registrador()  # Instancia de Mesero

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual

    def buscar_Mesa(self):
        """Buscar un Mesa por cédula"""
        IdMesa = self.entry_IdMesa.get()

        if not IdMesa:
            messagebox.showwarning("Advertencia", "Por favor ingrese una cédula.")
            return

        mesa = self.cajero.buscar_Mesa(IdMesa)

        if mesa:
            IdMesa, CantidadComensales, Estado = mesa
            self.entry_IdMesa.config(state="normal")
            self.entry_CantidadComensales.config(state="normal")
            self.entry_Estado.config(state="normal")

            self.entry_IdMesa.delete(0, tk.END)
            self.entry_CantidadComensales.delete(0, tk.END)
            self.entry_Estado.delete(0, tk.END)

            self.entry_IdMesa.insert(0, IdMesa)
            self.entry_CantidadComensales.insert(0, CantidadComensales)
            self.entry_Estado.insert(0, Estado)
            
        else:
            messagebox.showerror("Error", "Mesa no encontrado.")

    def eliminar_Mesa(self):
       """Eliminar Mesa de la base de datos solo si su estado es 'libre'."""
       IdMesa = self.entry_IdMesa.get()
       estado_mesa = self.entry_Estado.get()

       if not IdMesa:
           messagebox.showwarning("Advertencia", "Por favor ingrese el ID de la mesa para eliminar.")
           return

       if estado_mesa.lower() != "libre":
            messagebox.showerror("Error", "Solo se pueden eliminar mesas cuyo estado sea 'libre'.")
            return

       if self.cajero.eliminar_Mesa(IdMesa):
            messagebox.showinfo("Éxito", "Mesa eliminada correctamente.")
        # Limpiar campos después de la eliminación
            self.entry_IdMesa.delete(0, tk.END)
            self.entry_CantidadComensales.config(state="disabled")
            self.entry_CantidadComensales.delete(0, tk.END)
            self.entry_Estado.config(state="normal")
            self.entry_Estado.delete(0, tk.END)
            self.entry_Estado.insert(0, "libre")
            self.entry_Estado.config(state="disabled")
       else:
             messagebox.showerror("Error", "No se pudo eliminar la mesa.")
