# 📘 Cómo ejecutar los scripts SQL de nuestro proyecto en un DBMS online  

Este proyecto incluye **scripts SQL** para crear la estructura de una base de datos, cargar datos de prueba y ejecutar consultas de verificación.  
Podés usarlos fácilmente en **plataformas online**, sin necesidad de instalar software en tu computadora.  

---

## 📂 Archivos del proyecto
- `estructura.sql` → Crea las tablas, claves primarias y relaciones.  
- `datos.sql` → Inserta registros de ejemplo en cada tabla. 

---

## 🌐 Plataformas recomendadas
Algunas opciones donde podés ejecutar los scripts:  
- **OneCompiler (MySQL):** https://onecompiler.com/mysql  
- **SQL Fiddle (MySQL / PostgreSQL):** http://sqlfiddle.com/  
- **DB Fiddle (MySQL / PostgreSQL / SQLite):** https://db-fiddle.com/  
- **Replit (MySQL con configuración):** https://replit.com/  

---

## 🚀 Pasos para ejecutar los scripts  

1. Abrí el editor SQL en la plataforma que elijas.  
   👉 Ejemplo: [OneCompiler](https://onecompiler.com/mysql)  

2. Pegá el contenido de **`estructura.sql`**  
   - Este script define la base de datos y sus tablas.  
   - ⚠️ Si la plataforma no permite `CREATE DATABASE`, borrá esa línea y asegurate de estar dentro de una base activa.  

3. Ejecutá el script (Run / Execute o el botón equivalente).  

4. Pegá el contenido de **`datos.sql`** para cargar los registros de prueba.  

5. Ejecutá nuevamente y verificá que no haya errores.  

6. *(Opcional)* Probá consultas de verificación, por ejemplo:  
   ```sql
   SELECT * FROM nombre_tabla;
   SELECT COUNT(*) FROM otra_tabla;
