# BD-Evidencia-6

Este repositorio contiene los archivos correspondientes a la Evidencia 6 del proyecto SmartHome.

##  Archivos incluidos

- `estructura.sql`: creación de tablas del sistema SmartHome.
- `datos_iniciales.sql`: inserción de datos iniciales (roles, usuarios, casas, ubicaciones, dispositivos, automatizaciones).
- `consultas.sql`: incluye consultas simples, multitabla y subconsultas, todas justificadas y relevantes para el sistema.

##  Cómo ejecutar los scripts

1. Ingresar a [OneCompiler](https://onecompiler.com/mysql).
2. Seleccionar el motor de base de datos **MySQL**.
3. Ejecutar los archivos en el siguiente orden:
   - Primero: `estructura.sql`
   - Segundo: `datos_iniciales.sql`
   - Tercero: `consultas.sql`
4. Verificar los resultados en la consola de salida.

> ⚠️ Este script está diseñado para el motor **MySQL**. Si se utiliza otro motor como PostgreSQL o SQL Server, pueden surgir diferencias en sintaxis o comportamiento.

##  Recomendaciones

- Si se vuelve a ejecutar el script, se recomienda limpiar las tablas con `TRUNCATE` para evitar errores por datos duplicados.
- Las consultas están comentadas y justificadas según las necesidades del sistema SmartHome.
