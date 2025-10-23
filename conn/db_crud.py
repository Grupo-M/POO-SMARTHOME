from conn.db_conn import create_connection
import logging

logger = logging.getLogger("mysql.connector")

def execute_query(query, params=None):
    """SELECT"""
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
            logger.debug("Consulta ejecutada correctamente, %d registros obtenidos.", len(result))
            return result
    except Exception as e:
        logger.error("Error en SELECT: %s", e)
        return None
    finally:
        conn.close()

def insert_query(query, params):
    """INSERT"""
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            logger.debug("INSERT ejecutado correctamente.")
            return True
    except Exception as e:
        logger.error("Error en INSERT: %s", e)
        return False
    finally:
        conn.close()

def update_query(query, params):
    """UPDATE"""
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            logger.debug("UPDATE ejecutado correctamente.")
            return True
    except Exception as e:
        logger.error("Error en UPDATE: %s", e)
        return False
    finally:
        conn.close()

def delete_query(query, params):
    """DELETE"""
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            logger.debug("DELETE ejecutado correctamente.")
            return True
    except Exception as e:
        logger.error("Error en DELETE: %s", e)
        return False
    finally:
        conn.close()

