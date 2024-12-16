from Model.ConexionDB import ConexionDB
import tkinter as tk
from tkinter import messagebox as mb

class Chef():
    def __init__(self):
        pass

    def agregar_plato(self, id_plato, nombre, precio, cantidad, descripcion):
        """Método para agregar un plato a la base de datos"""
        # Crear conexión a la base de datos
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        
        try:
            cursor = con.cursor()
            
            # Verificar si el ID ya existe
            cursor.execute("SELECT COUNT(*) FROM platos WHERE idPlato = %s", (id_plato,))
            resultado = cursor.fetchone()
            
            if resultado[0] > 0:  # Si ya existe un registro con ese ID
                mb.showwarning("Advertencia", f"El ID {id_plato} ya existe. No se puede agregar el plato.")
                return
            
            # Insertar el nuevo plato si el ID no existe
            query = """
            INSERT INTO platos (idPlato, Nombre, Precio, CantidadDisponible, Descripcion)
            VALUES (%s, %s, %s, %s, %s)
            """
            params = (id_plato, nombre, precio, cantidad, descripcion)
            cursor.execute(query, params)
            con.commit()  # Confirmar los cambios

            mb.showinfo("Éxito", "Plato agregado exitosamente.")
        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al agregar el plato: {e}")
        finally:
            cursor.close()
            con.close()

    def obtener_platos(self):
        """Método para obtener todos los platos de la base de datos"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()
            query = "SELECT * FROM platos"
            cursor.execute(query)
            platos = cursor.fetchall()
            return platos
        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al obtener los platos: {e}")
            return []
        finally:
            cursor.close()
            con.close()


    def buscar_plato(self, id_plato):
        """Buscar un plato por ID en la base de datos."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        
        try:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM platos WHERE idPlato = %s", (id_plato,))
            plato = cursor.fetchone()
            return plato
        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al buscar el plato: {e}")
            return None
        finally:
            cursor.close()
            con.close()

    def eliminar_plato(self, id_plato):
        """Eliminar un plato por ID de la base de datos."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        
        try:
            cursor = con.cursor()
            cursor.execute("DELETE FROM platos WHERE idPlato = %s", (id_plato,))
            con.commit()
            return cursor.rowcount > 0  # True si se eliminó algún registro
        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al eliminar el plato: {e}")
            return False
        finally:
            cursor.close()
            con.close()

    def servir_comanda(self, id_comanda):
        """Cambiar el estado de una comanda a 'Servida', solo si está en estado 'En preparación'."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar si la comanda existe y su estado actual
            query_verificar_comanda = "SELECT Estado FROM Comandas WHERE IdComanda = %s"
            cursor.execute(query_verificar_comanda, (id_comanda,))
            resultado_comanda = cursor.fetchone()

            if resultado_comanda is None:
                mb.showerror("Error", f"La comanda con el ID {id_comanda} no existe.")
                return False

            if resultado_comanda[0] != "En preparacion":
                mb.showerror("Error", "La comanda no está en estado 'En preparación'. No se puede cambiar a 'Servida'.")
                return False

            # Actualizar el estado de la comanda a 'Servida'
            query_actualizar_estado = "UPDATE Comandas SET Estado = 'Servida' WHERE IdComanda = %s"
            cursor.execute(query_actualizar_estado, (id_comanda,))
            con.commit()

            mb.showinfo("Éxito", "La comanda ha sido marcada como 'Servida' correctamente.")
            return True

        except Exception as e:
            print(f"Error al servir la comanda: {e}")
            mb.showerror("Error", "Ocurrió un error al intentar servir la comanda.")
            return False

        finally:
            cursor.close()
            con.close()
