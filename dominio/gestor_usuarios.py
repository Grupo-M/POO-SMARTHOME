
from typing import Optional, List
from dominio.usuario import Usuario
from dominio.rol import Rol
from conn.db_conn import execute_query, update_query, insert_query

class GestorUsuarios:
   

    def __init__(self, admin_usuario: Usuario):
        """
        admin_usuario: Usuario que está realizando las operaciones.
        Solo los administradores pueden cambiar roles de otros usuarios.
        """
        if admin_usuario.rol.id_rol != 1:  
            raise PermissionError("Solo administradores pueden usar GestorUsuarios.")
        self.admin_usuario = admin_usuario

    def cambiar_rol(self, usuario_id: int, nuevo_rol: Rol) -> bool:
        """
        Cambia el rol de un usuario en la base de datos.
        """
        query = "UPDATE usuario SET id_rol = %s WHERE id_usuario = %s"
        params = (nuevo_rol.id_rol, usuario_id)
        exito = update_query(query, params)
        return exito

    def agregar_usuario(self, usuario: Usuario) -> bool:
        """
        Agrega un usuario nuevo a la base de datos.
        """
        query = """
            INSERT INTO usuario (nombre, apellido, email, password, id_rol)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (
            usuario.nombre,
            usuario.apellido,
            usuario.email,
            usuario.password,
            usuario.rol.id_rol
        )
        return insert_query(query, params)

    def listar_usuarios(self) -> Optional[List[tuple]]:
        """
        Devuelve todos los usuarios de la base de datos.
        """
        query = "SELECT id_usuario, nombre, apellido, email, id_rol FROM usuario"
        return execute_query(query)

