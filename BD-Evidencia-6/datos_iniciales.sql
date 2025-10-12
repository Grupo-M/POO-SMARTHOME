
-- Tabla: rol
INSERT INTO rol (nombre, descripcion) VALUES
('usuario', 'Permisos básicos para controlar dispositivos'),
('administrador', 'Acceso completo al sistema'),
('técnico', 'Gestión técnica de dispositivos'),
('invitado', 'Acceso limitado a ciertas funciones'),
('seguridad', 'Monitoreo de sensores y alarmas'),
('mantenimiento', 'Control de dispositivos esenciales'),
('automatizador', 'Diseño de reglas de automatización'),
('auditor', 'Revisión de actividad del sistema'),
('propietario', 'Dueño de la casa inteligente'),
('desarrollador', 'Acceso a funciones avanzadas y pruebas');

-- Tabla: casa
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

-- Tabla: usuario
INSERT INTO usuario (nombre_completo, email, contrasena, id_rol) VALUES
('Carolina Lanfranco', 'caro14@gmail.com', 'Oreo4', 1),
('Julia Lanfranco', 'julia2@gmail.com', 'cooni123', 2),
('Martín Paez ', 'martin_Paez@gmail.com', 'Polar123', 3),
('Micaela Lopez', 'micalopez@gmail.com', 'Luna456', 4),
('Solange Martinez ', 'Solange@gmail.com', 'Estrella7', 5),
('Catalina arnosio', 'Cataarno@gmail.com', 'Hups82', 6),
('Matias Rodriguez', 'MatiRo@gmail.com', 'nose69', 7),
('Rocio Altamirano', 'Rochi@gmail.com', 'jaja2', 8),
('Facundo Rodriguez', 'facu.r@gmail.com', 'Luchi5', 9),
('Diego Cordoba', 'DiegoCord@gmail.com', 'Ave78', 10);

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

INSERT INTO dispositivo (nombre, estado, esencial, id_ubicacion) VALUES
('Lámpara LED', 'encendido', true, 1),
('persiana automatica', 'apagado', true, 2),
('Aire acondicionado', 'apagado', false, 3),
('Extractor de aire', 'encendido', true, 4),
('Cámara de seguridad', 'encendido', true, 5),
('Termotanque', 'encendido', true, 6),
('Router WiFi', 'encendido', false, 7),
('Luz inteligente exterior', 'encendido', true, 8),
('Smart TV', 'apagado', false, 9),
('Persiana automática', 'encendido', false, 10);

-- Tabla: automatizacion
INSERT INTO automatizacion (nombre) VALUES
('Encender luces al anochecer'),
('Apagar luces al amanecer'),
('Activar cámara de seguridad al salir'),
('Encender aire acondicionado si hace calor'),
('Apagar termotanque por la noche'),
('Encender extractor al detectar humedad'),
('Reiniciar router cada madrugada'),
('Bajar persianas al atardecer'),
('Activar persiana automática en cocina'),
('Encender Smart TV para modo cine');

-- Dispositivos adicionales en Garage
INSERT INTO dispositivo (nombre, estado, esencial, id_ubicacion) VALUES
('Sensor de movimiento', 'encendido', true, 5),
('Alarma sonora', 'apagado', true, 5);

-- Dispositivos adicionales en Living
INSERT INTO dispositivo (nombre, estado, esencial, id_ubicacion) VALUES
('Parlante inteligente', 'encendido', false, 1),
('Control de cortinas', 'apagado', false, 1);




-- Automatización 1: Encender luces al anochecer → Lámpara LED (Living)
INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES (1, 1);

-- Automatización 2: Apagar luces al amanecer → Luz inteligente exterior (Patio)
INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES (2, 8);

-- Automatización 3: Activar cámara de seguridad al salir → Cámara de seguridad (Garage)
INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES (3, 5);

-- Automatización 4: Encender aire acondicionado si hace calor → Aire acondicionado (Dormitorio)
INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES (4, 3);

-- Automatización 5: Apagar termotanque por la noche → Termotanque (Lavadero)
INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES (5, 6);

-- Automatización 6: Encender extractor al detectar humedad → Extractor de aire (Baño)
INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES (6, 4);

-- Automatización 7: Reiniciar router cada madrugada → Router WiFi (Oficina)
INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES (7, 7);

-- Automatización 8: Bajar persianas al atardecer → Persiana automática (Quincho)
INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES (8, 10);

-- Automatización 9: Activar persiana automática en cocina → Persiana automática (Cocina)
INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES (9, 2);

-- Automatización 10: Encender Smart TV para modo cine → Smart TV (Comedor)
INSERT INTO automatizacion_dispositivo (id_automatizacion, id_dispositivo) VALUES (10, 9);



