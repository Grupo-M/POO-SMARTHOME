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

def listar_roles() -> List[Rol]:
    """Devuelve una lista de todos los roles registrados."""
    query = "SELECT id_rol, nombre, descripcion FROM roles"
    resultados = execute_query(query)
    roles = []
    if resultados:
        for fila in resultados:
            id_rol, nombre, descripcion = fila
            roles.append(Rol(id_rol, nombre, descripcion))
    return roles


def actualizar_rol(rol: Rol) -> bool:
    """Actualiza los datos de un rol existente."""
    query = """
        UPDATE roles
        SET nombre = %s, descripcion = %s
        WHERE id_rol = %s
    """
    params = (rol.nombre, rol.descripcion, rol.id_rol)
    return update_query(query, params)


def eliminar_rol(id_rol: int) -> bool:
    """Elimina un rol de la base de datos según su ID."""
    query = "DELETE FROM roles WHERE id_rol = %s"
    params = (id_rol,)

    return delete_query(query,params)
