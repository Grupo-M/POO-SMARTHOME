DROP DATABASE IF EXISTS `POO-SmartHome`;
CREATE DATABASE `POO-SmartHome`;
USE `POO-SmartHome`;

CREATE TABLE rol (
  id_rol INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(100)
);

CREATE TABLE usuario (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nombre_completo VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  contrasena VARCHAR(100) NOT NULL,
  id_rol INT,
  FOREIGN KEY (id_rol) REFERENCES rol(id_rol)
);

CREATE TABLE casa (
  id_casa INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  direccion VARCHAR(100)
);

CREATE TABLE ubicacion (
  id_ubicacion INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  id_casa INT,
  FOREIGN KEY (id_casa) REFERENCES casa(id_casa)
);

CREATE TABLE dispositivo (
  id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  estado VARCHAR(20) DEFAULT 'apagado',
  esencial BOOLEAN NOT NULL,
  id_ubicacion INT,
  FOREIGN KEY (id_ubicacion) REFERENCES ubicacion(id_ubicacion)
);

CREATE TABLE automatizacion (
  id_automatizacion INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL
);

CREATE TABLE automatizacion_dispositivo (
  id_automatizacion INT NOT NULL,
  id_dispositivo INT NOT NULL,
  PRIMARY KEY (id_automatizacion, id_dispositivo),
  FOREIGN KEY (id_automatizacion) REFERENCES automatizacion(id_automatizacion),
  FOREIGN KEY (id_dispositivo) REFERENCES dispositivo(id_dispositivo)
);