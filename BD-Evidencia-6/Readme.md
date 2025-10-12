# BD-Evidencia-6

Este repositorio contiene los archivos correspondientes a la Evidencia 6 del proyecto SmartHome, desarrollada en SQL para el motor MySQL.

##  Archivos incluidos

- `estructura.sql`: contiene la creación de las tablas del sistema SmartHome.
- `datos_iniciales.sql`: incluye los datos iniciales (INSERT) para poblar las tablas con roles, usuarios, casas, ubicaciones, dispositivos y automatizaciones.
- `consultas.sql`: contiene consultas simples, multitabla y subconsultas, todas comentadas y justificadas según las necesidades del sistema.

##  Cómo ejecutar los scripts

1. Ingresar a [OneCompiler MySQL](https://onecompiler.com/mysql).
2. Verificar que el lenguaje seleccionado sea **MySQL**.
3. Ejecutar los archivos en el siguiente orden:
   - Primero: `estructura.sql` (creación de tablas)
   - Segundo: `datos_iniciales.sql` (inserción de datos)
   - Tercero: `consultas.sql` (ejecución de consultas)
4. Verificar los resultados en la consola de salida.

> ⚠️ Importante: No se debe incluir `USE smarthome_db;` en los scripts, ya que OneCompiler no permite cambiar de base de datos.

---

##  Explicación de las consultas

###  Consultas simples

Estas consultas permiten verificar que los datos fueron cargados correctamente en cada tabla:

- `SELECT * FROM rol;`
- `SELECT * FROM casa;`
- `SELECT * FROM usuario;`
- `SELECT * FROM ubicacion;`
- `SELECT * FROM dispositivo;`
- `SELECT * FROM automatizacion;`
- `SELECT * FROM automatizacion_dispositivo;`

---

###  Consultas multitabla

Estas consultas combinan información de varias tablas para obtener datos relevantes del sistema:

1. **Usuarios y sus roles**  
   Muestra el rol asignado a cada usuario, útil para verificar permisos y responsabilidades.

2. **Dispositivos y su ubicación**  
   Permite visualizar el estado de cada dispositivo según su ubicación física dentro de la casa.

3. **Ubicaciones con mayor cantidad de dispositivos**  
   Identifica qué zonas del hogar tienen más carga tecnológica, útil para planificación y mantenimiento.

4. **Automatizaciones y dispositivos vinculados**  
   Muestra qué dispositivos están automatizados y cómo, útil para monitoreo y revisión de reglas activas.

---

###  Subconsultas

Estas consultas permiten obtener información más específica usando subqueries:

1. **Dispositivos esenciales**  
   Muestra los dispositivos marcados como esenciales, clave para asegurar continuidad operativa.

2. **Dispositivos apagados en ubicaciones críticas**  
   Detecta dispositivos apagados en zonas clave del hogar (Garage, Baño, Cocina), útil para mantenimiento y prevención de fallos.

---

##  Recomendaciones

- Si se vuelve a ejecutar el script, se recomienda limpiar las tablas con `TRUNCATE` para evitar errores por datos duplicados.
- Las consultas están comentadas y justificadas para facilitar su comprensión y evaluación.


