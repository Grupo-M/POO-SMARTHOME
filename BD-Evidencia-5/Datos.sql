USE `POO-SmartHome`;

INSERT INTO rol (nombre, descripcion) VALUES
('Administrador', 'Acceso total al sistema'),
('Usuario', 'Acceso limitado a sus dispositivos');

INSERT INTO casa (nombre, direccion) VALUES
('Casa Principal', 'Av. Siempre Viva 123'),
('Casa de Verano', 'Ruta Provincial S/N');

INSERT INTO ubicacion (nombre, id_casa) VALUES
('Cocina', 1),
('Dormitorio 1', 1),
('Living', 1),
('Terraza', 2),
('Garage', 2);

INSERT INTO dispositivo (nombre, estado, esencial, id_ubicacion) VALUES
('Luz cocina', 'apagado', TRUE, 1),
('Televisor', 'encendido', FALSE, 3),
('Aire acondicionado', 'apagado', TRUE, 2),
('Cámara seguridad', 'encendido', TRUE, 5),
('Ventilador', 'apagado', FALSE, 2),
('Microondas', 'encendido', FALSE, 1),
('Router WiFi', 'encendido', TRUE, 3),
('Sensor de movimiento', 'apagado', TRUE, 4);

INSERT INTO automatizacion (nombre) VALUES
('Modo Ahorro de Energía'),
('Modo Seguridad'),
('Modo Noche'),
('Modo Vacaciones'),
('Modo Emergencia');

INSERT INTO usuario (nombre_completo, email, contrasena, id_rol) VALUES
('Juan Pérez', 'juan@example.com', '1234', 1),
('Ana Gómez', 'ana@example.com', 'abcd', 2),
('Carlos Ruiz', 'carlos@example.com', 'pass1', 2),
('Lucía Fernández', 'lucia@example.com', 'pass2', 2),
('Pedro Martínez', 'pedro@example.com', 'pass3', 1),
('Sofía López', 'sofia@example.com', 'pass4', 2),
('Diego Torres', 'diego@example.com', 'pass5', 2),
('Valentina Castro', 'valentina@example.com', 'pass6', 2),
('Martín Rivas', 'martin@example.com', 'pass7', 1),
('Camila Herrera', 'camila@example.com', 'pass8', 2);

INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES
(1, 1),
(2, 2),
(1, 3),
(2, 4),
(3, 5),
(4, 6),
(5, 7),
(3, 8);

SELECT * FROM rol;
SELECT * FROM usuario;
SELECT * FROM casa;
SELECT * FROM ubicacion;
SELECT * FROM dispositivo;
SELECT * FROM automatizacion;
SELECT * FROM automatizacion_dispositivo;