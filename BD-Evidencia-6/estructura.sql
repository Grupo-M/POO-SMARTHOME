-- Archivo: estructura.sql
-- Proyecto: SmartHome - Evidencia 6
-- Descripción: Creación de tablas para el sistema de gestión de casas inteligentes
-- Requiere que la base de datos 'smarthome_db' exista previamente


USE smarthome_db;

CREATE TABLE IF NOT EXISTS rol (
    id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(100) NOT NULL,
    id_rol INT NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES rol(id_rol)
);

CREATE TABLE IF NOT EXISTS casa (
    id_casa INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS ubicacion (
    id_ubicacion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    id_casa INT NOT NULL,
    FOREIGN KEY (id_casa) REFERENCES casa(id_casa)
);

CREATE TABLE IF NOT EXISTS dispositivo (
    id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    estado VARCHAR(20) DEFAULT 'apagado',
    esencial BOOLEAN NOT NULL,
    id_ubicacion INT NOT NULL,
    FOREIGN KEY (id_ubicacion) REFERENCES ubicacion(id_ubicacion)
);

CREATE TABLE IF NOT EXISTS automatizacion (
    id_automatizacion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS automatizacion_dispositivo (
    id_automatizacion INT NOT NULL,
    id_dispositivo INT NOT NULL,
    PRIMARY KEY (id_automatizacion, id_dispositivo),
    FOREIGN KEY (id_automatizacion) REFERENCES automatizacion(id_automatizacion),
    FOREIGN KEY (id_dispositivo) REFERENCES dispositivo(id_dispositivo)
);

