"""
rol_dao.py
Clase DAO para la entidad Rol del sistema SmartHome.
"""
from typing import Optional, List
from dominio.rol import Rol
from conn.db_conn import execute_query, insert_query, update_query, delete_query
from interfaces.irol_dao import IRolDAO

class RolDAO(IRolDAO):
    

    def insertar(self, rol: Rol) -> bool:
        """Inserta un nuevo rol en la base de datos."""
        query = """
            INSERT INTO rol (nombre, descripcion)
            VALUES (%s, %s)
        """
        params = (rol.nombre, rol.descripcion)
        return insert_query(query, params)

    def obtener_por_id(self, id_rol: int) -> Optional[Rol]:
        """Devuelve un objeto Rol según su ID."""
        query = "SELECT id_rol, nombre, descripcion FROM rol WHERE id_rol = %s"
        resultados = execute_query(query, (id_rol,))

        if resultados:
            id_rol, nombre, descripcion = resultados[0]  # type: ignore
            return Rol(id_rol, nombre, descripcion)      # type: ignore
        return None

    def listar_todos(self) -> List[Rol]:
        """Devuelve una lista de todos los roles registrados."""
        query = "SELECT id_rol, nombre, descripcion FROM rol"
        resultados = execute_query(query)
        roles = []
        if resultados:
            for fila in resultados:
                id_rol, nombre, descripcion = fila
                roles.append(Rol(id_rol, nombre, descripcion))  # type: ignore
        return roles

    def actualizar(self, rol: Rol) -> bool:
        """Actualiza los datos de un rol existente."""
        query = """
            UPDATE rol
            SET nombre = %s, descripcion = %s
            WHERE id_rol = %s
        """
        params = (rol.nombre, rol.descripcion, rol.id_rol)
        return update_query(query, params)

    def eliminar(self, id_rol: int) -> bool:
        """Elimina un rol de la base de datos según su ID."""
        query = "DELETE FROM rol WHERE id_rol = %s"
        params = (id_rol,)
        return delete_query(query, params)

