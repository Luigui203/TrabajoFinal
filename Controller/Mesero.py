from Model.ConexionDB import ConexionDB
import tkinter as tk
from tkinter import messagebox as mb

class Mesero:
    def __init__(self):
        pass

    def AgregarCliente(self, cedula, nombre, apellido, telefono, email):
        """Agrega un cliente a la base de datos"""
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

            # Insertar el nuevo cliente con rol "Cliente"
            query_insertar = """
                INSERT INTO Usuarios (NumCedula, Nombre, Apellido, Telefono, Email, Rol)
                VALUES (%s, %s, %s, %s, %s, 'Cliente')
            """
            parametros = (cedula, nombre, apellido, telefono, email)
            cursor.execute(query_insertar, parametros)
            con.commit()

            # Mostrar mensaje de éxito
            mb.showinfo("Éxito", f"El cliente con cédula {cedula} fue agregado exitosamente.")


            return True

        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al agregar el cliente: {e}")
            return False

        finally:
            cursor.close()
            con.close()

    def buscar_cliente(self, cedula):
        """Busca un cliente en la base de datos por cédula"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar si la cédula existe en la base de datos
            query_buscar = "SELECT Nombre, Apellido, Telefono, Email FROM Usuarios WHERE NumCedula = %s AND Rol = 'Cliente'"
            cursor.execute(query_buscar, (cedula,))
            resultado = cursor.fetchone()

            if resultado:
                return resultado  # Devuelve un tuple (nombre, apellido, telefono, email)
            else:
                return None  # Cliente no encontrado

        except Exception as e:
            print(f"Error al buscar cliente: {e}")
            return None

        finally:
            cursor.close()
            con.close()

    def eliminar_cliente(self, cedula):
        """Elimina un cliente de la base de datos"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Eliminar al cliente con la cédula especificada
            query_eliminar = "DELETE FROM Usuarios WHERE NumCedula = %s AND Rol = 'Cliente'"
            cursor.execute(query_eliminar, (cedula,))
            con.commit()

            return True

        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False

        finally:
            cursor.close()
            con.close()

    def buscar_mesa(self, id_mesa):
        """Consulta una mesa en la base de datos por su ID."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()
            query = """
                SELECT CantidadComensales, Estado
                FROM Mesas
                WHERE IdMesa = %s
            """
            cursor.execute(query, (id_mesa,))
            mesa = cursor.fetchone()
            return mesa  # Devuelve una tupla (CantidadComensales, Estado) o None si no se encuentra
        except Exception as e:
            print(f"Error al buscar la mesa: {e}")
            return None
        finally:
            cursor.close()
            con.close()

    def ocupar_mesa(self, id_mesa):
        """Actualizar el estado de la mesa a 'ocupada'."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()
            query = "UPDATE Mesas SET Estado = 'ocupada' WHERE IdMesa = %s AND Estado = 'libre'"
            cursor.execute(query, (id_mesa,))
            con.commit()

            return cursor.rowcount > 0  # Verifica si se actualizó alguna fila

        except Exception as e:
            print(f"Error al ocupar mesa: {e}")
            return False

        finally:
            cursor.close()
            con.close()


    def liberar_mesa(self, id_mesa):
        """Actualizar el estado de la mesa a 'liberada'."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()
            query = "UPDATE Mesas SET Estado = 'libre' WHERE IdMesa = %s AND Estado = 'ocupada'"
            cursor.execute(query, (id_mesa,))
            con.commit()

            return cursor.rowcount > 0  # Verifica si se actualizó alguna fila

        except Exception as e:
            print(f"Error al liberar la mesa: {e}")
            return False

        finally:
            cursor.close()
            con.close()

    def guardar_comanda(self, id_comanda, id_cliente, num_mesa, precio_total, estado):
        """Guardar una nueva comanda en la base de datos."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar si el ID de la comanda ya existe
            query_verificar_comanda = "SELECT IdComanda FROM Comandas WHERE IdComanda = %s"
            cursor.execute(query_verificar_comanda, (id_comanda,))
            resultado_comanda = cursor.fetchone()

            if resultado_comanda is not None:
                mb.showerror("Error", f"El ID de la comanda {id_comanda} ya existe.")
                return False

            # Verificar si la mesa existe y está ocupada
            query_verificar_mesa = "SELECT Estado FROM Mesas WHERE IdMesa = %s"
            cursor.execute(query_verificar_mesa, (num_mesa,))
            resultado_mesa = cursor.fetchone()

            if resultado_mesa is None:
                mb.showerror("Error", f"La mesa con el número {num_mesa} no existe.")
                return False
            elif resultado_mesa[0] != "ocupada":
                mb.showerror("Error", f"La mesa {num_mesa} no está ocupada.")
                return False

            # Verificar si el cliente existe
            query_verificar_cliente = "SELECT NumCedula FROM Usuarios WHERE NumCedula = %s AND Rol = 'Cliente'"
            cursor.execute(query_verificar_cliente, (id_cliente,))
            resultado_cliente = cursor.fetchone()

            if resultado_cliente is None:
                mb.showerror("Error", "El cliente no existe o no tiene el rol de 'Cliente'.")
                return False

            # Insertar la comanda con estado 'Pendiente' y precio inicial 0.0
            query_insert_comanda = """
                INSERT INTO Comandas (IdComanda, NumCedulaCliente, IdMesa, PrecioTotal, Estado)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query_insert_comanda, (id_comanda, id_cliente, num_mesa, precio_total, estado))
            con.commit()

            return True

        except Exception as e:
            print(f"Error al guardar la comanda: {e}")
            return False

        finally:
            cursor.close()
            con.close()

    def agregar_plato_comanda(self, id_comanda, id_plato, cantidad):
        """Agregar un plato a la comanda, solo si está en estado 'Pendiente' y actualizar el precio total de la comanda."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar si la comanda está en estado 'Pendiente'
            query_verificar_comanda = "SELECT Estado, PrecioTotal FROM Comandas WHERE IdComanda = %s"
            cursor.execute(query_verificar_comanda, (id_comanda,))
            resultado_comanda = cursor.fetchone()

            if resultado_comanda is None:
                mb.showerror("Error", f"La comanda con el ID {id_comanda} no existe.")
                return False

            if resultado_comanda[0] != "Pendiente":
                mb.showerror("Error", "La comanda no está en estado 'Pendiente'. No se pueden agregar más platos.")
                return False

            # Convertir cantidad a entero
            try:
                cantidad = int(cantidad)
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser mayor que cero.")
            except ValueError:
                mb.showerror("Error", "La cantidad debe ser un número entero positivo.")
                return False

            # Verificar si el plato existe y obtener el precio
            query_verificar_plato = "SELECT Precio, CantidadDisponible FROM Platos WHERE IdPlato = %s"
            cursor.execute(query_verificar_plato, (id_plato,))
            resultado_plato = cursor.fetchone()

            if resultado_plato is None:
                mb.showerror("Error", f"El plato con el ID {id_plato} no existe.")
                return False

            precio_plato = resultado_plato[0]
            stock_disponible = resultado_plato[1]

            # Verificar que la cantidad disponible sea suficiente
            if stock_disponible < cantidad:
                mb.showerror("Error", f"No hay suficiente stock disponible para este plato. Solo hay {stock_disponible} disponibles.")
                return False

            # Verificar si el plato ya existe en la comanda (DetalleComanda)
            query_verificar_detalle = "SELECT IdDetalle, Cantidad FROM DetalleComanda WHERE IdComanda = %s AND IdPlato = %s"
            cursor.execute(query_verificar_detalle, (id_comanda, id_plato))
            resultado_detalle = cursor.fetchone()

            if resultado_detalle:
                # Si el plato ya está en la comanda, actualizar la cantidad
                nueva_cantidad = resultado_detalle[1] + cantidad
                query_actualizar_detalle = """
                    UPDATE DetalleComanda
                    SET Cantidad = %s
                    WHERE IdDetalle = %s
                """
                cursor.execute(query_actualizar_detalle, (nueva_cantidad, resultado_detalle[0]))
            else:
                # Si el plato no está en la comanda, insertar un nuevo detalle
                query_insert_detalle = """
                    INSERT INTO DetalleComanda (IdComanda, IdPlato, Cantidad)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(query_insert_detalle, (id_comanda, id_plato, cantidad))

            # Actualizar el precio total de la comanda
            precio_total_nuevo = resultado_comanda[1] + (precio_plato * cantidad)
            query_actualizar_precio = """
                UPDATE Comandas
                SET PrecioTotal = %s
                WHERE IdComanda = %s
            """
            cursor.execute(query_actualizar_precio, (precio_total_nuevo, id_comanda))

            # Actualizar el stock disponible del plato
            nuevo_stock = stock_disponible - cantidad
            query_actualizar_stock = """
                UPDATE Platos
                SET CantidadDisponible = %s
                WHERE IdPlato = %s
            """
            cursor.execute(query_actualizar_stock, (nuevo_stock, id_plato))
            con.commit()

            return True

        except Exception as e:
            print(f"Error al agregar plato a la comanda: {e}")
            return False

        finally:
            cursor.close()
            con.close()


    def eliminar_plato_comanda(self, id_comanda, id_plato, cantidad):
        """Eliminar un plato de la comanda, solo si está en estado 'Pendiente' y ajustar el precio de la comanda y el stock del plato."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar si la comanda está en estado 'Pendiente'
            query_verificar_comanda = "SELECT Estado, PrecioTotal FROM Comandas WHERE IdComanda = %s"
            cursor.execute(query_verificar_comanda, (id_comanda,))
            resultado_comanda = cursor.fetchone()

            if resultado_comanda is None:
                mb.showerror("Error", f"La comanda con el ID {id_comanda} no existe.")
                return False

            if resultado_comanda[0] != "Pendiente":
                mb.showerror("Error", "La comanda no está en estado 'Pendiente'. No se puede eliminar platos.")
                return False

            # Verificar si el plato está asociado a la comanda
            query_verificar_plato_comanda = """
                SELECT IdPlato, Cantidad FROM DetalleComanda WHERE IdComanda = %s AND IdPlato = %s
            """
            cursor.execute(query_verificar_plato_comanda, (id_comanda, id_plato))
            resultado_plato_comanda = cursor.fetchone()

            if resultado_plato_comanda is None:
                mb.showerror("Error", "El plato no está asociado a la comanda.")
                return False

            # Verificar si la cantidad es válida
            if int(cantidad) > resultado_plato_comanda[1]:
                mb.showerror("Error", f"La cantidad a eliminar supera la cantidad del plato en la comanda.")
                return False

            # Obtener el precio del plato
            query_obtener_precio_plato = "SELECT Precio, CantidadDisponible FROM Platos WHERE IdPlato = %s"
            cursor.execute(query_obtener_precio_plato, (id_plato,))
            resultado_plato = cursor.fetchone()

            if resultado_plato is None:
                mb.showerror("Error", "El plato con el ID proporcionado no existe en la base de datos.")
                return False

            precio_plato = resultado_plato[0]
            stock_disponible = resultado_plato[1]

            # Actualizar el stock del plato
            nuevo_stock = stock_disponible + int(cantidad)
            query_actualizar_stock = """
                UPDATE Platos
                SET CantidadDisponible = %s
                WHERE IdPlato = %s
            """
            cursor.execute(query_actualizar_stock, (nuevo_stock, id_plato))

            # Si la cantidad es mayor que 1, reducir la cantidad
            if int(cantidad) < resultado_plato_comanda[1]:
                query_actualizar_cantidad = """
                    UPDATE DetalleComanda SET Cantidad = Cantidad - %s WHERE IdComanda = %s AND IdPlato = %s
                """
                cursor.execute(query_actualizar_cantidad, (cantidad, id_comanda, id_plato))
            else:
                # Si la cantidad es igual a la cantidad en detallecomanda, eliminar el plato
                query_eliminar_plato = """
                    DELETE FROM DetalleComanda WHERE IdComanda = %s AND IdPlato = %s
                """
                cursor.execute(query_eliminar_plato, (id_comanda, id_plato))

            # Actualizar el precio total de la comanda
            nuevo_precio_total = resultado_comanda[1] - (precio_plato * int(cantidad))
            query_actualizar_precio = """
                UPDATE Comandas
                SET PrecioTotal = %s
                WHERE IdComanda = %s
            """
            cursor.execute(query_actualizar_precio, (nuevo_precio_total, id_comanda))

            con.commit()

            return True

        except Exception as e:
            print(f"Error al eliminar plato de la comanda: {e}")
            return False

        finally:
            cursor.close()
            con.close()


    def enviar_comanda_chef(self, id_comanda):
        """Cambiar el estado de una comanda a 'En preparación', solo si está en estado 'Pendiente' y tiene platos asociados."""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()

        try:
            cursor = con.cursor()

            # Verificar el estado actual de la comanda
            query_verificar_estado = "SELECT Estado FROM Comandas WHERE IdComanda = %s"
            cursor.execute(query_verificar_estado, (id_comanda,))
            resultado_comanda = cursor.fetchone()

            if resultado_comanda is None:
                mb.showerror("Error", f"La comanda con ID {id_comanda} no existe.")
                return False

            if resultado_comanda[0] != "Pendiente":
                mb.showerror("Error", f"La comanda no está en estado 'Pendiente'.")
                return False

            # Verificar si la comanda tiene al menos un plato asociado
            query_verificar_detalle = "SELECT COUNT(*) FROM DetalleComanda WHERE IdComanda = %s"
            cursor.execute(query_verificar_detalle, (id_comanda,))
            resultado_detalle = cursor.fetchone()

            if resultado_detalle[0] == 0:
                mb.showerror("Error", "La comanda no tiene platos asociados y no se puede enviar al chef.")
                return False

            # Cambiar el estado de la comanda a 'En preparación'
            query_actualizar_estado = "UPDATE Comandas SET Estado = 'En preparacion' WHERE IdComanda = %s"
            cursor.execute(query_actualizar_estado, (id_comanda,))
            con.commit()

            return True

        except Exception as e:
            print(f"Error al enviar la comanda al chef: {e}")
            return False

        finally:
            cursor.close()
            con.close()

        