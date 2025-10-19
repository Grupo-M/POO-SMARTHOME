
-- Proyecto: SmartHome
-- Creación de tablas y datos iniciales coherentes con los DAOs de Python

USE smarthome_db;

-- Tabla de roles
CREATE TABLE IF NOT EXISTS rol (
    id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100)
);


INSERT INTO rol (id_rol, nombre, descripcion) VALUES
    (1, 'Admin', 'Permisos totales'),
    (2, 'Usuario', 'Permisos básicos');

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    id_rol INT NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES rol(id_rol)
);

-- Tabla de casas
CREATE TABLE IF NOT EXISTS casa (
    id_casa INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(100)
);

-- Tabla de ubicaciones
CREATE TABLE IF NOT EXISTS ubicacion (
    id_ubicacion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    id_casa INT NOT NULL,
    FOREIGN KEY (id_casa) REFERENCES casa(id_casa)
);

-- Tabla de dispositivos
CREATE TABLE IF NOT EXISTS dispositivo (
    id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    estado VARCHAR(20) DEFAULT 'apagado',
    esencial BOOLEAN NOT NULL,
    id_ubicacion INT NOT NULL,
    FOREIGN KEY (id_ubicacion) REFERENCES ubicacion(id_ubicacion)
);

-- Tabla de automatizaciones
CREATE TABLE IF NOT EXISTS automatizacion (
    id_automatizacion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Tabla de relación automatizacion <-> dispositivo
CREATE TABLE IF NOT EXISTS automatizacion_dispositivo (
    id_automatizacion INT NOT NULL,
    id_dispositivo INT NOT NULL,
    PRIMARY KEY (id_automatizacion, id_dispositivo),
    FOREIGN KEY (id_automatizacion) REFERENCES automatizacion(id_automatizacion),
    FOREIGN KEY (id_dispositivo) REFERENCES dispositivo(id_dispositivo)
);
