"""
db_conn.py
Módulo para conexión y operaciones CRUD en la base de datos MySQL.

"""

import sys
import os
import logging
import mysql.connector
from mysql.connector import errorcode

# Ajuste del path para permitir importaciones desde la raíz del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Intento de importación de configuración privada
try:
    from conn.config import DB_CONFIG  # Configuración privada (gitignored)
except ImportError:
    from conn.config_gral import DB_CONFIG  # Configuración pública
    print("Crea tu conn/config.py con tus credenciales reales.")

# Configuración del logger
logger = logging.getLogger("mysql.connector")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def create_connection():
    """Crea y devuelve la conexión a la base de datos MySQL."""
    logger.debug("Intentando conectarse a la base de datos...")
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        logger.debug("Conexión exitosa a la base de datos.")
        return conn
    except mysql.connector.Error as err:
        logger.error("Error al conectar: %s", err)
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            raise ConnectionError("Usuario o contraseña no válidos.") from err
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            raise ConnectionError("La base de datos no existe.") from err
        raise ConnectionError("Error al conectar con la base de datos.") from err

def execute_query(query, params=None):
    """Ejecuta una consulta SELECT y devuelve los resultados."""
    logger.debug("Ejecutando SELECT: %s | Parámetros: %s", query, params)
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params) # type: ignore
            result = cursor.fetchall()
            logger.debug("Consulta ejecutada correctamente, %d registros obtenidos.", len(result))
            return result
    except mysql.connector.Error as err:
        logger.error("Error al ejecutar SELECT: %s", err)
        return None
    finally:
        conn.close()
        logger.debug("Conexión cerrada")


def insert_query(query, params):
    """Ejecuta una consulta INSERT con parámetros."""
    logger.debug("Ejecutando INSERT: %s | Parámetros: %s", query, params)
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            logger.debug("INSERT ejecutado correctamente.")
            return True
    except mysql.connector.Error as err:
        logger.error("Error al ejecutar INSERT: %s", err)
        return False
    finally:
        conn.close()
        logger.debug("Conexión cerrada")

def update_query(query, params):
    """Ejecuta una consulta UPDATE con parámetros."""
    logger.debug("Ejecutando UPDATE: %s | Parámetros: %s", query, params)
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            logger.debug("UPDATE ejecutado correctamente.")
            return True
    except mysql.connector.Error as err:
        logger.error("Error al ejecutar UPDATE: %s", err)
        return False
    finally:
        conn.close()
        logger.debug("Conexión cerrada")

def delete_query(query, params):
    """Ejecuta una consulta DELETE con parámetros."""
    logger.debug("Ejecutando DELETE: %s | Parámetros: %s", query, params)
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            logger.debug("DELETE ejecutado correctamente.")
            return True
    except mysql.connector.Error as err:
        logger.error("Error al ejecutar DELETE: %s", err)
        return False
    finally:
        conn.close()
        logger.debug("Conexión cerrada")

if __name__ == "__main__":
    resultados = execute_query("SHOW TABLES;")
    if resultados:
        print("Tablas en la base de datos:")
        for fila in resultados:
            print(f" - {fila[0]}") # type: ignore



