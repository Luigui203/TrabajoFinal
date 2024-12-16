import mariadb as sql

class ConexionDB():
    def __init__(self, host="127.0.0.1", user="root", password="", port=3306, database="restaurante"):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port
        self.__database = database
        self.__conection = None

    def crearConexion(self):
        try:
            self.__conection = sql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                port=self.__port,
                database=self.__database
            )
        except sql.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            self.__conection = None

    def cerrarConexion(self):
        if self.__conection:
            self.__conection.close()
            self.__conection = None

    def getConection(self):
        return self.__conection

    def probarConexion(self):
        try:
            with sql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                port=self.__port,
                database=self.__database
            ) as conn:
                print("Conexión exitosa.")
        except sql.Error as e:
            print(f"Error al probar la conexión: {e}")

    # Métodos para obtener atributos si es necesario
    def getHost(self):
        return self.__host

    def getUser(self):
        return self.__user

    def getDatabase(self):
        return self.__database
