import tkinter as tk
from tkinter import messagebox as mb
from Controller.Mesero import Mesero

class EliminarPlatoComanda:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        self.master.withdraw()  # Ocultar la ventana principal

        # Crear una nueva ventana
        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Eliminar Plato de Comanda")
        self.nueva_ventana.geometry("400x400")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Evento para restaurar la ventana principal
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Centrar el título "Eliminar Plato de Comanda"
        titulo = tk.Label(self.nueva_ventana, text="Eliminar Plato de Comanda", font=("Helvetica", 16))
        titulo.pack(pady=10)

        # Crear un frame para el formulario
        frame_form = tk.Frame(self.nueva_ventana)
        frame_form.pack(pady=10)

        # Crear y colocar los widgets del formulario
        tk.Label(frame_form, text="ID Comanda*").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_comanda = tk.Entry(frame_form)
        self.entry_id_comanda.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="ID Plato*").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_plato = tk.Entry(frame_form)
        self.entry_id_plato.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Cantidad*").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_cantidad = tk.Entry(frame_form)
        self.entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

        # Crear un frame para los botones
        frame_buttons = tk.Frame(self.nueva_ventana)
        frame_buttons.pack(pady=10)

        # Botón Eliminar Plato
        btn_eliminar_plato = tk.Button(frame_buttons, text="Eliminar Plato", command=self.eliminar_plato)
        btn_eliminar_plato.grid(row=0, column=0, padx=10)

        # Botón Salir
        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.on_close)
        btn_salir.grid(row=0, column=1, padx=10)

        self.mesero = Mesero()

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual

    def eliminar_plato(self):
        """Eliminar un plato de la comanda."""
        id_comanda = self.entry_id_comanda.get()
        id_plato = self.entry_id_plato.get()
        cantidad = self.entry_cantidad.get()

        # Validar campos obligatorios
        if not id_comanda or not id_plato or not cantidad:
            mb.showwarning("Advertencia", "Por favor complete todos los campos obligatorios marcados con *.")
            return

        # Llamar al método del mesero para eliminar el plato
        resultado = self.mesero.eliminar_plato_comanda(id_comanda, id_plato, cantidad)

        if resultado:
            # Si la eliminación fue exitosa
            mb.showinfo("Éxito", "Plato eliminado de la comanda correctamente.")
            self.on_close()  # Cerrar la ventana
    
