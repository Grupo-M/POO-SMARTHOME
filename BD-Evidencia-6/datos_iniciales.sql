-- Crear base de datos
CREATE DATABASE IF NOT EXISTS smarthome_db;
USE smarthome_db;

-- --- Tablas ---
CREATE TABLE IF NOT EXISTS rol (
    id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
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
    id_usuario INT NULL,
    FOREIGN KEY (id_ubicacion) REFERENCES ubicacion(id_ubicacion),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
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

-- --- Datos iniciales ---

-- Roles
INSERT INTO rol (nombre, descripcion) VALUES
('administrador', 'Acceso completo al sistema'),
('usuario', 'Permisos básicos para controlar dispositivos');

-- Casas
INSERT INTO casa (nombre, direccion) VALUES
('Casa Carolina', 'Av. Córdoba 123, Almafuerte'),
('Casa Julia', 'Calle San Martín 456, Almafuerte'),
('Casa Martin', 'Parque Industrial 789, Río Tercero'),
('Casa Micaela', 'Ruta 5 km 12, Embalse'),
('Casa Solange', 'Calle Las Heras 321, Villa María'),
('Casa Catalina', 'Av. del Sol 999, San Luis'),
('Casa Matias', 'Calle Tucumán 88, Córdoba Capital'),
('Casa Rocio', 'Calle Belgrano 77, Alta Gracia'),
('Casa Facundo', 'Av. General Paz 1000, Córdoba'),
('Casa Diego', 'Av Libertadores 365, Córdoba');

-- Usuarios
-- Administrador inicial
INSERT INTO usuario (nombre, apellido, email, password, id_rol) VALUES
('Carolina', 'Lanfranco', 'caro14@gmail.com', 'Oreo4', 1);

-- Usuarios estándar
INSERT INTO usuario (nombre, apellido, email, password, id_rol) VALUES
('Julia', 'Lanfranco', 'julia2@gmail.com', 'cooni123', 2),
('Martín', 'Paez', 'martin_Paez@gmail.com', 'Polar123', 2),
('Micaela', 'Lopez', 'micalopez@gmail.com', 'Luna456', 2),
('Solange', 'Martinez', 'Solange@gmail.com', 'Estrella7', 2),
('Catalina', 'Arnosio', 'Cataarno@gmail.com', 'Hups82', 2),
('Matias', 'Rodriguez', 'MatiRo@gmail.com', 'nose69', 2),
('Rocio', 'Altamirano', 'Rochi@gmail.com', 'jaja2', 2),
('Facundo', 'Rodriguez', 'facu.r@gmail.com', 'Luchi5', 2),
('Diego', 'Cordoba', 'DiegoCord@gmail.com', 'Ave78', 2);

-- Ubicaciones
INSERT INTO ubicacion (nombre, id_casa) VALUES
('Living', 1),
('Cocina', 2),
('Dormitorio Principal', 3),
('Baño', 4),
('Garage', 5),
('Lavadero', 6),
('Oficina', 7),
('Patio', 8),
('Comedor', 9),
('Quincho', 10);

-- Dispositivos de ejemplo
INSERT INTO dispositivo (nombre, estado, esencial, id_ubicacion) VALUES
('Lámpara LED', 'encendido', true, 1),
('Persiana automática', 'apagado', true, 2),
('Aire acondicionado', 'apagado', false, 3),
('Extractor de aire', 'encendido', true, 4),
('Cámara de seguridad', 'encendido', true, 5),
('Termotanque', 'encendido', true, 6),
('Router WiFi', 'encendido', false, 7),
('Luz inteligente exterior', 'encendido', true, 8),
('Smart TV', 'apagado', false, 9),
('Persiana automática', 'encendido', false, 10);


