-- Usar la base de datos existente
USE smarthome_db;

CREATE TABLE IF NOT EXISTS rol (
  id_rol INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  descripcion VARCHAR(100)
);

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    email VARCHAR(100),
    contrasena VARCHAR(100),
    id_rol INT,
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
  id_casa INT,
  FOREIGN KEY (id_casa) REFERENCES casa(id_casa)
);

CREATE TABLE IF NOT EXISTS dispositivo (
  id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  estado VARCHAR(20) DEFAULT 'apagado',
  esencial BOOLEAN NOT NULL,
  id_ubicacion INT,
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

