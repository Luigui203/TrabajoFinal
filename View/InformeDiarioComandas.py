import tkinter as tk
from tkinter import messagebox
from datetime import datetime  # Importación necesaria para obtener la fecha actual
from Controller.Registrador import Registrador

class InformeDiario:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        self.master.withdraw()

        # Crear una nueva ventana
        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Informe Diario de Comandas")
        self.nueva_ventana.geometry("600x400")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")  # Ruta al ícono de la ventana

        # Evento para mostrar la ventana principal al cerrar
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Centrar el título "Informe Diario de Comandas"
        titulo = tk.Label(self.nueva_ventana, text="Informe Diario de Comandas", font=("Helvetica", 16))
        titulo.pack(pady=10)

        # Crear un frame para el formulario
        frame_form = tk.Frame(self.nueva_ventana)
        frame_form.pack(pady=10)

        # Crear y colocar los widgets del formulario en una cuadrícula
        tk.Label(frame_form, text="Fecha").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.label_fecha = tk.Label(frame_form, text="")
        self.label_fecha.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Cantidad Comandas").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.label_cantidad_comandas = tk.Label(frame_form, text="")
        self.label_cantidad_comandas.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Total Ganancias Día").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.label_total_ganancias = tk.Label(frame_form, text="")
        self.label_total_ganancias.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Promedio Ganancias Día").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.label_promedio_ganancias = tk.Label(frame_form, text="")
        self.label_promedio_ganancias.grid(row=3, column=1, padx=5, pady=5)

        # Crear un frame para los botones
        frame_buttons = tk.Frame(self.nueva_ventana)
        frame_buttons.pack(pady=10)

        # Botón Salir
        btn_salir = tk.Button(frame_buttons, text="Salir", command=self.on_close)
        btn_salir.grid(row=0, column=1, padx=10)

        # Botón para guardar el informe
        btn_guardar = tk.Button(frame_buttons, text="Guardar Informe", command=self.guardar_informe)
        btn_guardar.grid(row=0, column=0, padx=10)

        # Cargar el informe
        self.cargar_informe()

    def cargar_informe(self):
        """Carga los datos del informe desde la base de datos."""
        registrador = Registrador()
        informe = registrador.obtener_informe_diario()

        if informe:
            # Mostrar los datos del informe
            self.label_fecha.config(text=datetime.now().strftime('%Y-%m-%d'))  # Fecha actual
            self.label_cantidad_comandas.config(text=informe["cantidad_comandas"])
            self.label_total_ganancias.config(text=informe["total_ganancias"])
            self.label_promedio_ganancias.config(text=informe["promedio_ganancias"])
        else:
            messagebox.showerror("Error", "No se pudo obtener el informe.")

    def guardar_informe(self):
        """Guarda el informe en la base de datos."""
        fecha = datetime.now().strftime('%Y-%m-%d')
        cantidad_comandas = self.label_cantidad_comandas.cget("text")
        total_ganancias = self.label_total_ganancias.cget("text")
        promedio_ganancias = self.label_promedio_ganancias.cget("text")

        # Verifica que los valores sean válidos antes de guardar
        if cantidad_comandas and total_ganancias and promedio_ganancias:
            registrador = Registrador()
            resultado = registrador.guardar_informe_diario(fecha, cantidad_comandas, total_ganancias, promedio_ganancias)
            if resultado:
                messagebox.showinfo("Éxito", "Informe guardado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el informe.")
        else:
            messagebox.showerror("Error", "No hay datos válidos para guardar el informe.")

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual
