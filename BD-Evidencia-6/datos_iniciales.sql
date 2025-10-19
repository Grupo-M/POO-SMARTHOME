-- Roles
INSERT INTO rol (id_rol, nombre, descripcion) VALUES
(1, 'administrador', 'Acceso completo al sistema'),
(2, 'usuario', 'Permisos básicos para controlar dispositivos');

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


