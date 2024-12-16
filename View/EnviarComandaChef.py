import tkinter as tk
from tkinter import messagebox as mb
from Controller.Mesero import Mesero

class EnviarComandaChef:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        # Ocultar la ventana principal
        self.master.withdraw()

        # Crear la nueva ventana
        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Enviar Comanda al Chef")
        self.nueva_ventana.geometry("400x200")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Restaurar la ventana principal al cerrar esta
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Configurar diseño con un Frame principal
        frame = tk.Frame(self.nueva_ventana, padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        # Título
        titulo = tk.Label(frame, text="Enviar Comanda", font=("Helvetica", 16))
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Etiqueta y entrada para ID de la Comanda
        self.label_id_comanda = tk.Label(frame, text="ID Comanda:")
        self.label_id_comanda.grid(row=1, column=0, sticky="e", padx=5, pady=5)

        self.entry_id_comanda = tk.Entry(frame, width=30)
        self.entry_id_comanda.grid(row=1, column=1, padx=5, pady=5)

        # Botón para enviar la comanda
        self.btn_enviar = tk.Button(frame, text="Enviar Comanda", command=self.enviar_comanda)
        self.btn_enviar.grid(row=2, column=0, columnspan=2, pady=15)

        # Instancia del controlador Mesero
        self.mesero = Mesero()

    def on_close(self):
        """Restaurar la ventana principal al cerrar esta ventana."""
        if self.master:
            self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual

    def enviar_comanda(self):
        """Cambiar el estado de una comanda a 'En preparación'."""
        id_comanda = self.entry_id_comanda.get().strip()

        # Validar campo obligatorio
        if not id_comanda:
            mb.showwarning("Advertencia", "Por favor, ingrese el ID de la comanda.")
            return

        # Verificar que el ID sea un número válido
        if not id_comanda.isdigit():
            mb.showwarning("Advertencia", "El ID de la comanda debe ser un número válido.")
            return

        # Llamar al método del mesero para cambiar el estado de la comanda
        try:
            resultado = self.mesero.enviar_comanda_chef(id_comanda)
            if resultado:
                mb.showinfo("Éxito", "La comanda se ha enviado al chef correctamente.")
                self.on_close()  # Cerrar la ventana
        except Exception as e:
            mb.showerror("Error crítico", f"Ha ocurrido un error: {e}")
