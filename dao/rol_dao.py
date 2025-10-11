#rol_dao

from dominio.rol import Rol
from conn.db_conn import execute_query, insert_query, update_query, delete_query
from typing import Optional, List


def insertar_rol(rol: Rol) -> bool:
    """Inserta un nuevo rol en la base de datos."""
    query = """
        INSERT INTO roles (id_rol, nombre, descripcion)
        VALUES (%s, %s, %s)
    """
    params = (rol.id_rol, rol.nombre, rol.descripcion)
    return insert_query(query, params)


def obtener_rol_por_id(id_rol: int) -> Optional[Rol]:
    """Devuelve un objeto Rol según su ID."""
    query = "SELECT id_rol, nombre, descripcion FROM roles WHERE id_rol = %s"
    resultados = execute_query(query % id_rol)  # O adaptar execute_query para usar parámetros
    if resultados:
        id_rol, nombre, descripcion = resultados[0]
        return Rol(id_rol, nombre, descripcion)
    return None


