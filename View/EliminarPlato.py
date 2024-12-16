import tkinter as tk
from tkinter import messagebox as mb
from Controller.Chef import Chef

class EliminarPlato:
    def __init__(self, master, usuario):
        self.master = master
        self.usuario = usuario

        self.master.withdraw()

        # Crear una nueva ventana
        self.nueva_ventana = tk.Toplevel(master)
        self.nueva_ventana.title("Eliminar Plato")
        self.nueva_ventana.geometry("400x300")
        self.nueva_ventana.resizable(0, 0)
        self.nueva_ventana.focus_set()
        self.nueva_ventana.configure(bg="#f0f0f0")
        self.nueva_ventana.iconbitmap(r"iconos\valle.ico")

        # Evento para restaurar la ventana principal
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.on_close)

        # Centrar el título "Eliminar Plato"
        titulo = tk.Label(self.nueva_ventana, text="Eliminar Plato", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
        titulo.pack(pady=20)

        # Crear un frame para el formulario
        frame_form = tk.Frame(self.nueva_ventana, bg="#f0f0f0")
        frame_form.pack(pady=10, padx=20, fill=tk.X)

        # Crear y colocar los widgets del formulario en una cuadrícula
        self.create_label_entry(frame_form, "ID*", 0)
        self.entry_id = self.create_entry(frame_form, 0)

        self.create_label_entry(frame_form, "Nombre*", 1)
        self.entry_nombre = self.create_entry(frame_form, 1, "disabled")

        self.create_label_entry(frame_form, "Precio*", 2)
        self.entry_precio = self.create_entry(frame_form, 2, "disabled")

        self.create_label_entry(frame_form, "Cantidad Disponible*", 3)
        self.entry_cantidad = self.create_entry(frame_form, 3, "disabled")

        self.create_label_entry(frame_form, "Descripción*", 4)
        self.entry_descripcion = self.create_entry(frame_form, 4, "disabled")

        # Crear un frame para los botones
        frame_buttons = tk.Frame(self.nueva_ventana, bg="#f0f0f0")
        frame_buttons.pack(pady=10)

        self.create_button(frame_buttons, "Buscar", self.buscar_plato, 0)
        self.create_button(frame_buttons, "Eliminar", self.eliminar_plato, 1)
        self.create_button(frame_buttons, "Salir", self.on_close, 2)

    def on_close(self):
        """Restaurar la ventana principal al cerrar la ventana actual."""
        self.master.deiconify()  # Mostrar la ventana principal
        self.nueva_ventana.destroy()  # Cerrar la ventana actual

    def create_label_entry(self, frame, text, row):
        label = tk.Label(frame, text=text, font=("Helvetica", 10), bg="#f0f0f0", fg="#333")
        label.grid(row=row, column=0, padx=5, pady=5, sticky="e")

    def create_entry(self, frame, row, state="normal"):
        entry = tk.Entry(frame, state=state)
        entry.grid(row=row, column=1, padx=5, pady=5, sticky="w")
        return entry

    def create_button(self, frame, text, command, column):
        button = tk.Button(frame, text=text, command=command, bg="#007BFF", fg="white", font=("Helvetica", 10, "bold"), bd=0, padx=10, pady=5)
        button.grid(row=0, column=column, padx=10)

    def buscar_plato(self):
        """Buscar un plato por ID y mostrar los detalles en los campos"""
        id_plato = self.entry_id.get()
        if not id_plato:
            mb.showerror("Error", "Por favor, ingresa el ID del plato.")
            return

        chef = Chef()
        plato = chef.buscar_plato(id_plato)

        if plato:
            self.entry_nombre.config(state="normal")
            self.entry_precio.config(state="normal")
            self.entry_cantidad.config(state="normal")
            self.entry_descripcion.config(state="normal")

            self.entry_nombre.delete(0, tk.END)
            self.entry_precio.delete(0, tk.END)
            self.entry_cantidad.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)

            self.entry_nombre.insert(0, plato[1])
            self.entry_precio.insert(0, plato[2])
            self.entry_cantidad.insert(0, plato[3])
            self.entry_descripcion.insert(0, plato[4])

            self.entry_nombre.config(state="disabled")
            self.entry_precio.config(state="disabled")
            self.entry_cantidad.config(state="disabled")
            self.entry_descripcion.config(state="disabled")
        else:
            mb.showerror("Error", f"No se encontró un plato con ID {id_plato}.")

    def eliminar_plato(self):
        """Eliminar un plato por ID"""
        id_plato = self.entry_id.get()
        if not id_plato:
            mb.showerror("Error", "Por favor, ingresa el ID del plato a eliminar.")
            return

        chef = Chef()
        resultado = chef.eliminar_plato(id_plato)

        if resultado:
            mb.showinfo("Éxito", f"El plato con ID {id_plato} fue eliminado exitosamente.")
            self.entry_id.delete(0, tk.END)
            self.entry_nombre.config(state="normal")
            self.entry_precio.config(state="normal")
            self.entry_cantidad.config(state="normal")
            self.entry_descripcion.config(state="normal")

            self.entry_nombre.delete(0, tk.END)
            self.entry_precio.delete(0, tk.END)
            self.entry_cantidad.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)

            self.entry_nombre.config(state="disabled")
            self.entry_precio.config(state="disabled")
            self.entry_cantidad.config(state="disabled")
            self.entry_descripcion.config(state="disabled")
        else:
            mb.showerror("Error", f"No se pudo eliminar el plato con ID {id_plato}.")
