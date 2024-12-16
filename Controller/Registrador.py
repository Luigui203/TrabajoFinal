from Model.ConexionDB import ConexionDB
import tkinter as tk
from tkinter import messagebox as mb

class Registrador():
    def __init__(self):
        pass


    def AgregarChef(self, cedula, nombre, apellido, telefono, email):
        """Agrega un Chef a la base de datos"""
        # Crear conexión a la base de datos
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar si el correo electrónico contiene mayúsculas
            if not email.islower():
                mb.showerror("Error", "El correo electrónico debe estar en minúsculas.")
                return False

            # Verificar si la cédula ya existe en la tabla Usuarios
            query_verificar_cedula = "SELECT COUNT(*) FROM Usuarios WHERE NumCedula = %s"
            cursor.execute(query_verificar_cedula, (cedula,))
            resultado_cedula = cursor.fetchone()

            if resultado_cedula[0] > 0:
                mb.showerror("Error", f"La cédula {cedula} ya está registrada.")
                return False

            # Verificar si el teléfono ya existe en la tabla Usuarios
            query_verificar_telefono = "SELECT COUNT(*) FROM Usuarios WHERE Telefono = %s"
            cursor.execute(query_verificar_telefono, (telefono,))
            resultado_telefono = cursor.fetchone()

            if resultado_telefono[0] > 0:
                mb.showerror("Error", f"El teléfono {telefono} ya está registrado.")
                return False

            # Verificar si el email ya existe en la tabla Usuarios
            query_verificar_email = "SELECT COUNT(*) FROM Usuarios WHERE Email = %s"
            cursor.execute(query_verificar_email, (email,))
            resultado_email = cursor.fetchone()

            if resultado_email[0] > 0:
                mb.showerror("Error", f"El correo electrónico {email} ya está registrado.")
                return False

            # Insertar el nuevo Chef con rol "Chef"
            query_insertar = """
                INSERT INTO Usuarios (NumCedula, Nombre, Apellido, Telefono, Email, Rol)
                VALUES (%s, %s, %s, %s, %s, 'Chef')
            """
            parametros = (cedula, nombre, apellido, telefono, email)
            cursor.execute(query_insertar, parametros)
            con.commit()

            # Mostrar mensaje de éxito
            mb.showinfo("Éxito", f"El Chef con cédula {cedula} fue agregado exitosamente.")


            return True

        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al agregar el Chef: {e}")
            return False

        finally:
            cursor.close()
            con.close()


    def buscar_chef(self, cedula):
        """Busca un Chef en la base de datos por cédula"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar si la cédula existe en la base de datos
            query_buscar = "SELECT Nombre, Apellido, Telefono, Email FROM Usuarios WHERE NumCedula = %s AND Rol = 'Chef'"
            cursor.execute(query_buscar, (cedula,))
            resultado = cursor.fetchone()

            if resultado:
                return resultado  # Devuelve un tuple (nombre, apellido, telefono, email)
            else:
                return None  # Mesero no encontrado

        except Exception as e:
            print(f"Error al buscar Chef: {e}")
            return None

        finally:
            cursor.close()
            con.close()

    def eliminar_chef(self, cedula):
        """Elimina un Chef de la base de datos"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Eliminar al Mesero con la cédula especificada
            query_eliminar = "DELETE FROM Usuarios WHERE NumCedula = %s AND Rol = 'Chef'"
            cursor.execute(query_eliminar, (cedula,))
            con.commit()

            return True

        except Exception as e:
            print(f"Error al eliminar el Chef: {e}")
            return False

        finally:
            cursor.close()
            con.close()

            
    def AgregarMesero(self, cedula, nombre, apellido, telefono, email):
        """Agrega un Mesero a la base de datos"""
        # Crear conexión a la base de datos
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar si el correo electrónico contiene mayúsculas
            if not email.islower():
                mb.showerror("Error", "El correo electrónico debe estar en minúsculas.")
                return False

            # Verificar si la cédula ya existe en la tabla Usuarios
            query_verificar_cedula = "SELECT COUNT(*) FROM Usuarios WHERE NumCedula = %s"
            cursor.execute(query_verificar_cedula, (cedula,))
            resultado_cedula = cursor.fetchone()

            if resultado_cedula[0] > 0:
                mb.showerror("Error", f"La cédula {cedula} ya está registrada.")
                return False

            # Verificar si el teléfono ya existe en la tabla Usuarios
            query_verificar_telefono = "SELECT COUNT(*) FROM Usuarios WHERE Telefono = %s"
            cursor.execute(query_verificar_telefono, (telefono,))
            resultado_telefono = cursor.fetchone()

            if resultado_telefono[0] > 0:
                mb.showerror("Error", f"El teléfono {telefono} ya está registrado.")
                return False

            # Verificar si el email ya existe en la tabla Usuarios
            query_verificar_email = "SELECT COUNT(*) FROM Usuarios WHERE Email = %s"
            cursor.execute(query_verificar_email, (email,))
            resultado_email = cursor.fetchone()

            if resultado_email[0] > 0:
                mb.showerror("Error", f"El correo electrónico {email} ya está registrado.")
                return False

            # Insertar el nuevo Mesero con rol "Mesero"
            query_insertar = """
                INSERT INTO Usuarios (NumCedula, Nombre, Apellido, Telefono, Email, Rol)
                VALUES (%s, %s, %s, %s, %s, 'Mesero')
            """
            parametros = (cedula, nombre, apellido, telefono, email)
            cursor.execute(query_insertar, parametros)
            con.commit()

            # Mostrar mensaje de éxito
            mb.showinfo("Éxito", f"El Mesero con cédula {cedula} fue agregado exitosamente.")

            # Aquí puedes agregar código para actualizar la interfaz, si es necesario.
            # Por ejemplo, puedes llamar a un método que recargue la lista de Meseros.

            return True

        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al agregar el Mesero: {e}")
            return False

        finally:
            cursor.close()
            con.close()



    def buscar_Mesero(self, cedula):
        """Busca un Mesero en la base de datos por cédula"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar si la cédula existe en la base de datos
            query_buscar = "SELECT Nombre, Apellido, Telefono, Email FROM Usuarios WHERE NumCedula = %s AND Rol = 'Mesero'"
            cursor.execute(query_buscar, (cedula,))
            resultado = cursor.fetchone()

            if resultado:
                return resultado  # Devuelve un tuple (nombre, apellido, telefono, email)
            else:
                return None  # Mesero no encontrado

        except Exception as e:
            print(f"Error al buscar Mesero: {e}")
            return None

        finally:
            cursor.close()
            con.close()

    def eliminar_Mesero(self, cedula):
        """Elimina un Mesero de la base de datos"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Eliminar al Mesero con la cédula especificada
            query_eliminar = "DELETE FROM Usuarios WHERE NumCedula = %s AND Rol = 'Mesero'"
            cursor.execute(query_eliminar, (cedula,))
            con.commit()

            return True

        except Exception as e:
            print(f"Error al eliminar Mesero: {e}")
            return False

        finally:
            cursor.close()
            con.close()

    def AgregarMesa(self, IdMesa, CantidadComensales, Estado):
        """Agrega una Mesa a la base de datos"""
        # Crear conexión a la base de datos
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar si el id ya existe en la tabla Mesas
            query_verificar = "SELECT COUNT(*) FROM Mesas WHERE IdMesa = %s"
            cursor.execute(query_verificar, (IdMesa,))
            resultado = cursor.fetchone()

            if resultado[0] > 0:
                mb.showerror("Error", f"El id {IdMesa} ya está registrado.")
                return False

            # Insertar la nueva Mesa con rol "libre" por defecto para el Estado
            query_insertar = """
                INSERT INTO Mesas (IdMesa, CantidadComensales, Estado)
                VALUES (%s, %s, %s)
            """
            parametros = (IdMesa, CantidadComensales, Estado)  # Usar el parámetro Estado en vez de "libre"
            cursor.execute(query_insertar, parametros)
            con.commit()

            # Mostrar mensaje de éxito
            mb.showinfo("Éxito", f"La Mesa con id {IdMesa} fue agregada exitosamente.")

            return True

        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al agregar la Mesa: {e}")
            return False

        finally:
            cursor.close()
            con.close()

    def buscar_Mesa(self, IdMesa):
        """Busca una Mesa en la base de datos por el id"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar si la cédula existe en la base de datos
            query_buscar = "SELECT IdMesa, CantidadComensales, Estado FROM Mesas WHERE IdMesa = %s"
            cursor.execute(query_buscar, (IdMesa,))
            resultado = cursor.fetchone()

            if resultado:
                return resultado  # Devuelve un tuple (nIdMesa, CantidadComensales, Estado)
            else:
                return None  # Mesero no encontrado

        except Exception as e:
            print(f"Error al buscar Mesa: {e}")
            return None

        finally:
            cursor.close()
            con.close()

    def eliminar_Mesa(self, IdMesa):
        """Elimina una mesa de la base de datos"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Eliminar al Mesero con la cédula especificada
            query_eliminar = "DELETE FROM Mesas WHERE IdMesa = %s "
            cursor.execute(query_eliminar, (IdMesa,))
            con.commit()

            return True

        except Exception as e:
            print(f"Error al eliminar Mesa: {e}")
            return False

        finally:
            cursor.close()
            con.close()        

    def calcular_precio_total(self, id_comanda):
        """Calcular el precio total de la comanda, solo si su estado es 'Servida'."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar el estado de la comanda
            query_estado = "SELECT Estado FROM Comandas WHERE IdComanda = %s"
            cursor.execute(query_estado, (id_comanda,))
            resultado_estado = cursor.fetchone()

            if resultado_estado is None:
                print(f"Error: La comanda con ID {id_comanda} no existe.")
                return None  # Comanda no encontrada

            if resultado_estado[0] != "Servida":
                print(f"Error: La comanda no está en estado 'Servida'.")
                return None  # Comanda no servida

            # Si el estado es 'Servida', calcular el precio total
            query_precio = """
                SELECT SUM(p.Precio * d.Cantidad) AS PrecioTotal
                FROM DetalleComanda d
                JOIN Platos p ON d.IdPlato = p.IdPlato
                WHERE d.IdComanda = %s
                GROUP BY d.IdComanda
            """
            cursor.execute(query_precio, (id_comanda,))
            resultado_precio = cursor.fetchone()

            if resultado_precio is None or resultado_precio[0] is None:
                print(f"Error: La comanda no tiene platos asociados.")
                return None  # No tiene platos asociados

            return resultado_precio[0]  # Precio total de la comanda

        except Exception as e:
            print(f"Error al calcular el precio total de la comanda: {e}")
            return None

        finally:
            cursor.close()
            con.close()


    def obtener_informe_diario(self):
        """Obtiene el informe diario de la base de datos."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()
            query = """
                SELECT COUNT(*) AS CantidadComandas, SUM(PrecioTotal) AS TotalGanancias
                FROM Comandas
                WHERE Estado = 'Servida'
            """
            cursor.execute(query)
            resultado = cursor.fetchone()

            if resultado:
                cantidad_comandas = resultado[0]
                total_ganancias = resultado[1]
                promedio_ganancias = total_ganancias / cantidad_comandas if cantidad_comandas else 0

                return {
                    "cantidad_comandas": cantidad_comandas,
                    "total_ganancias": total_ganancias,
                    "promedio_ganancias": promedio_ganancias
                }
            else:
                return None
        except Exception as e:
            print(f"Error al obtener el informe diario: {e}")
            return None
        finally:
            cursor.close()
            con.close()

    def guardar_informe_diario(self, fecha, cantidad_comandas, total_ganancias, promedio_ganancias):
        """Guarda el informe en la base de datos."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()
            query = """
                INSERT INTO Informes (FechaInforme, CantidadComandas, TotalGananciasDia, PromedioGananciasDia)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (fecha, cantidad_comandas, total_ganancias, promedio_ganancias))
            con.commit()
            return True
        except Exception as e:
            print(f"Error al guardar el informe: {e}")
            return False
        finally:
            cursor.close()
            con.close()