import logging
import mysql.connector
from mysql.connector import errorcode
from conn.config import DB_CONFIG

# Logger para depuración
logger = logging.getLogger("mysql.connector")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def create_connection(with_db=True):
    """Crea y devuelve la conexión a MySQL. with_db=False ignora DB_CONFIG['database']"""
    config = DB_CONFIG.copy()
    if not with_db:
        config.pop("database", None)
    try:
        conn = mysql.connector.connect(**config)
        logger.debug("Conexión exitosa a la base de datos.")
        return conn
    except mysql.connector.Error as err:
        logger.error("Error al conectar: %s", err)
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            raise ConnectionError("Usuario o contraseña no válidos.") from err
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            raise ConnectionError("La base de datos no existe.") from err
        raise ConnectionError("Error al conectar con la base de datos.") from err

