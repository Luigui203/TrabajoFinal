import tkinter as tk
from tkinter import messagebox
from Controller.Mesero import Mesero


class TomarComanda:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        self.master.withdraw()

        # Crear una nueva ventana
        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Tomar Comanda")
        self.nueva_ventana.geometry("400x400")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Evento para mostrar la ventana principal al cerrar
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)


        # Centrar el título "Tomar Comanda"
        titulo = tk.Label(self.nueva_ventana, text="Tomar Comanda", font=("Helvetica", 16))
        titulo.pack(pady=10)

        # Crear un frame para el formulario
        frame_form = tk.Frame(self.nueva_ventana)
        frame_form.pack(pady=10)

        # Crear y colocar los widgets del formulario en una cuadrícula
        tk.Label(frame_form, text="ID Comanda*").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_comanda = tk.Entry(frame_form)
        self.entry_id_comanda.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="ID Cliente*").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_cliente = tk.Entry(frame_form)
        self.entry_id_cliente.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="N° Mesa*").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_num_mesa = tk.Entry(frame_form)
        self.entry_num_mesa.grid(row=2, column=1, padx=5, pady=5)


        tk.Label(frame_form, text="Precio Total").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_precio_total = tk.Entry(frame_form)
        self.entry_precio_total.grid(row=4, column=1, padx=5, pady=5)
        self.entry_precio_total.insert(0, "0.0")  # Valor por defecto
        self.entry_precio_total.config(state="disabled")  # Deshabilitar después de configurar valor por defecto

        tk.Label(frame_form, text="Estado").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_estado = tk.Entry(frame_form)
        self.entry_estado.grid(row=5, column=1, padx=5, pady=5)
        self.entry_estado.insert(0, "Pendiente")
        self.entry_estado.config(state="disabled") 

        # Crear un frame para los botones
        frame_buttons = tk.Frame(self.nueva_ventana)
        frame_buttons.pack(pady=10)

        # Botón Guardar Comanda
        btn_guardar_comanda = tk.Button(frame_buttons, text="Guardar Comanda", command=self.guardar_comanda)
        btn_guardar_comanda.grid(row=0, column=0, padx=10)

        # Botón Salir
        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.on_close)
        btn_salir.grid(row=0, column=1, padx=10)

        self.mesero = Mesero()


    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual

    def guardar_comanda(self):
        """Guardar la comanda en la base de datos."""
        # Obtener datos de los campos del formulario
        id_comanda = self.entry_id_comanda.get()
        id_cliente = self.entry_id_cliente.get()
        num_mesa = self.entry_num_mesa.get()
        estado = "Pendiente"  # Estado por defecto
        precio_total = 0.0    # Precio inicial por defecto

        # Validar campos obligatorios
        if not id_comanda or not id_cliente or not num_mesa:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos obligatorios marcados con *.")
            return

        # Llamar al método del mesero para guardar la comanda
        resultado = self.mesero.guardar_comanda(id_comanda, id_cliente, num_mesa, precio_total, estado)

        if resultado:
            messagebox.showinfo("Éxito", "Comanda guardada correctamente.")
            self.on_close()  # Cierra la ventana de "Tomar Comanda"
        