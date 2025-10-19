-- Archivo: consultas.sql
-- Proyecto: SmartHome - Evidencia 6
-- Descripción: Consultas SQL para verificación, análisis multitabla y subconsultas
-- Requiere que la base de datos 'smarthome_db' esté creada y poblada previamente

USE smarthome_db;

--  CONSULTAS SIMPLES: Verificación de datos cargados
SELECT * FROM rol;
SELECT * FROM casa;
SELECT * FROM usuario;
SELECT * FROM ubicacion;
SELECT * FROM dispositivo;
SELECT * FROM automatizacion;
SELECT * FROM automatizacion_dispositivo;

--  CONSULTAS MULTITABLA

-- 1. Usuarios y sus roles
-- Muestra el rol asignado a cada usuario, útil para verificar permisos y responsabilidades dentro del sistema.
SELECT u.nombre, u.apellido, u.email, r.nombre AS rol
FROM usuario u
JOIN rol r ON u.id_rol = r.id_rol;



-- 2. Dispositivos y su ubicación
-- Permite visualizar el estado de cada dispositivo según su ubicación física dentro de la casa. Útil para mantenimiento y control por zonas.
SELECT d.nombre AS dispositivo, d.estado, u.nombre AS ubicacion
FROM dispositivo d
JOIN ubicacion u ON d.id_ubicacion = u.id_ubicacion;

-- 3. Ubicaciones con mayor cantidad de dispositivos
-- Consulta para identificar qué zonas de las casas tienen más carga tecnológica, útil para planificación de infraestructura y mantenimiento.
SELECT u.nombre AS ubicacion, COUNT(d.id_dispositivo) AS cantidad_dispositivos
FROM ubicacion u
JOIN dispositivo d ON u.id_ubicacion = d.id_ubicacion
GROUP BY u.nombre
ORDER BY cantidad_dispositivos DESC;

-- 4. Dispositivos con su ubicación y casa asociada
-- Muestra cada dispositivo junto con su ubicación específica y la casa a la que pertenece. Útil para visualizar el contexto físico completo de cada dispositivo.
SELECT d.nombre AS dispositivo, d.estado, u.nombre AS ubicacion, c.nombre AS casa
FROM dispositivo d
JOIN ubicacion u ON d.id_ubicacion = u.id_ubicacion
JOIN casa c ON u.id_casa = c.id_casa;


--  SUBCONSULTAS

-- 1. Dispositivos esenciales
-- Muestra los dispositivos marcados como esenciales, clave para asegurar continuidad operativa y priorizar mantenimiento.
SELECT nombre, estado
FROM dispositivo
WHERE esencial = true;

-- 2. Dispositivos apagados en ubicaciones críticas
-- Consulta para detectar dispositivos apagados en zonas clave del hogar, útil para mantenimiento y prevención de fallos.
SELECT nombre
FROM dispositivo
WHERE estado = 'apagado'
AND id_ubicacion IN (
    SELECT id_ubicacion
    FROM ubicacion
    WHERE nombre IN ('Garage', 'Baño', 'Cocina')
);
