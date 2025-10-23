from conn.db_conn import create_connection
from conn.db_crud import execute_query
import logging

logger = logging.getLogger("mysql.connector")

def crear_base_si_no_existe(nombre_db):
    """Crear base si no existe"""
    logger.debug("Verificando existencia de la base de datos: %s", nombre_db)
    conn = create_connection(with_db=False)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_db}")
            logger.info("Base verificada/creada: %s", nombre_db)
    finally:
        conn.close()

def ejecutar_script_sql(ruta_archivo):
    """Ejecutar script SQL completo"""
    logger.debug("Ejecutando script: %s", ruta_archivo)
    conn = create_connection()
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            script = f.read()
        with conn.cursor() as cursor:
            for statement in script.split(';'):
                if statement.strip():
                    cursor.execute(statement)
            conn.commit()
            logger.info("Script ejecutado: %s", ruta_archivo)
    finally:
        conn.close()

def verificar_tablas(tablas):
    print("\nVerificación de carga:")
    for tabla in tablas:
        resultado = execute_query(f"SELECT COUNT(*) FROM {tabla}")
        if resultado:
            print(f" - {tabla}: {resultado[0][0]} registros")
        else:
            print(f" - {tabla}: error al consultar")

