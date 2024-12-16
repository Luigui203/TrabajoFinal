CREATE DATABASE Restaurante;

USE Restaurante;


-- Tabla Usuarios
CREATE TABLE Usuarios (
    NumCedula INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Telefono VARCHAR(15),
    Email VARCHAR(50),
    Rol ENUM('Registrador', 'Mesero', 'Chef', 'Cliente') -- Enumeración de roles
);

-- Tabla Mesas
CREATE TABLE Mesas (
    IdMesa INT PRIMARY KEY,
    CantidadComensales INT,
    Estado ENUM('libre', 'ocupada') DEFAULT 'libre' -- Enumeración de estados con valor por defecto 'libre'
);

-- Tabla Platos
CREATE TABLE Platos (
    IdPlato INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Precio DECIMAL(10, 2),
    CantidadDisponible INT,
    Descripcion VARCHAR(100)
);

-- Tabla Comandas
CREATE TABLE Comandas (
    IdComanda INT PRIMARY KEY,
    NumCedulaCliente INT,
    IdMesa INT,
    PrecioTotal DECIMAL(10, 2),
    Estado ENUM('Pendiente','En preparación','Servida'),
    FOREIGN KEY (NumCedulaCliente) REFERENCES Usuarios(NumCedula),
    FOREIGN KEY (IdMesa) REFERENCES Mesas(IdMesa)
);

-- Tabla DetalleComanda (relación entre Comandas y Platos)
CREATE TABLE DetalleComanda (
    IdDetalle INT PRIMARY KEY AUTO_INCREMENT,
    IdComanda INT,
    IdPlato INT,
    Cantidad INT,
    FOREIGN KEY (IdComanda) REFERENCES Comandas(IdComanda),
    FOREIGN KEY (IdPlato) REFERENCES Platos(IdPlato)
);

-- Tabla Informes
CREATE TABLE Informes (
    IdInforme INT PRIMARY KEY AUTO_INCREMENT,
    FechaInforme DATE,
    CantidadComandas INT,
    TotalGananciasDia DECIMAL(10, 2),
    PromedioGananciasDia DECIMAL(10, 2)
);


