from Model.ConexionDB import ConexionDB
import tkinter as tk
from tkinter import messagebox as mb

class Usuario():
    def __init__(self):
        self.cedula = None
        self.nombre = None
        self.apellido = None
        self.telefono = None
        self.email = None
        self.rol = None

    def iniciarSesion(self, nombreUsuario, password, loggin):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()

        try:
            cursor.execute("SELECT * FROM Usuarios WHERE nombre = %s AND NumCedula = %s", (nombreUsuario, password))
            usuario = cursor.fetchone()

            if usuario:
                self.nombre = usuario[1]
                self.correo = usuario[2]
                self.rol = usuario[5]  # Suponiendo que el rol está en la sexta columna
                mb.showinfo("Información", "¡Acceso concedido!")
                return self.rol  # Devolver el rol para redireccionar
            
        except Exception as e:
            mb.showerror("Error", f"Error al iniciar sesión: {e}")
            return None
        finally:
            cursor.close()
            con.close()

    

    def verificar_cedula_repetida(self, cedula):
        """Verificar si la cédula ya está registrada en la base de datos"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        try:
            query = "SELECT COUNT(*) FROM Usuarios WHERE NumCedula = %s"
            cursor.execute(query, (cedula,))
            resultado = cursor.fetchone()

            if resultado[0] > 0:
                mb.showerror("Error", f"La cédula {cedula} ya está registrada.")
                return True
            return False
        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al verificar la cédula: {e}")
            return True
        finally:
            cursor.close()
            con.close()


    def verificar_email_repetido(self, email):
        """Verificar si el correo ya está registrado en la base de datos"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        try:
            query = "SELECT COUNT(*) FROM Usuarios WHERE Email = %s"
            cursor.execute(query, (email,))
            resultado = cursor.fetchone()

            if resultado[0] > 0:
                mb.showerror("Error", f"El correo {email} ya está registrado.")
                return True
            return False
        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al verificar el correo: {e}")
            return True
        finally:
            cursor.close()
            con.close()


    def verificar_telefono_repetido(self, telefono):
        """Verificar si el teléfono ya está registrado en la base de datos"""
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        try:
            query = "SELECT COUNT(*) FROM Usuarios WHERE Telefono = %s"
            cursor.execute(query, (telefono,))
            resultado = cursor.fetchone()

            if resultado[0] > 0:
                mb.showerror("Error", f"El teléfono {telefono} ya está registrado.")
                return True
            return False
        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al verificar el teléfono: {e}")
            return True
        finally:
            cursor.close()
            con.close()


    def registrar_usuario(self, cedula, nombre, apellido, telefono, email, rol):
        """Registrar un usuario en la base de datos"""
        # Verificar si la cédula, el correo o el teléfono ya están registrados
        if self.verificar_cedula_repetida(cedula) or self.verificar_email_repetido(email) or self.verificar_telefono_repetido(telefono):
            return False  # Si alguno está repetido, no se registra el usuario

        # Crear conexión a la base de datos solo cuando sea necesario
        miConexion = ConexionDB()
        miConexion.crearConexion()
        con = miConexion.getConection()
        cursor = con.cursor()
        try:
            query = """
                INSERT INTO Usuarios (NumCedula, Nombre, Apellido, Telefono, Email, Rol)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            parametros = (cedula, nombre, apellido, telefono, email, rol)
            cursor.execute(query, parametros)
            con.commit()  # Confirmar la transacción
            return True
        except Exception as e:
            mb.showerror("Error", f"Ocurrió un error al registrar el usuario: {e}")
            return False
        finally:
            cursor.close()
            con.close()
