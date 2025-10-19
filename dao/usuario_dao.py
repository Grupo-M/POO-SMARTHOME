from dominio.usuario import Usuario
from dominio.rol import Rol
from typing import List, Optional
from conn.db_conn import insert_query, execute_query, update_query, delete_query

class UsuarioDAO:

    def guardar(self, usuario: Usuario) -> bool:
        query = """
            INSERT INTO usuario (nombre, apellido, email, password, id_rol)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (
            usuario.nombre,
            usuario.apellido,
            usuario.email,
            usuario.password,
            usuario.rol.id_rol
        )
        return insert_query(query, valores)

    def obtener_por_email(self, email: str) -> Optional[Usuario]:
        query = """
            SELECT u.id_usuario, u.nombre, u.apellido, u.email, u.password,
                   r.id_rol, r.nombre, r.descripcion
            FROM usuario u
            JOIN rol r ON u.id_rol = r.id_rol
            WHERE u.email = %s
        """
        resultados = execute_query(query, (email,))
        if resultados:
            fila = resultados[0]
            id_usuario, nombre, apellido, email, password, id_rol, rol_nombre, rol_descripcion = fila
            rol = Rol(id_rol, rol_nombre, rol_descripcion)
            return Usuario(nombre, apellido, email, password, rol, id_usuario=id_usuario)
        return None

    def obtener_por_id(self, id_usuario: int) -> Optional[Usuario]:
        query = """
            SELECT u.id_usuario, u.nombre, u.apellido, u.email, u.password,
                   r.id_rol, r.nombre, r.descripcion
            FROM usuario u
            JOIN rol r ON u.id_rol = r.id_rol
            WHERE u.id_usuario = %s
        """
        resultados = execute_query(query, (id_usuario,))
        if resultados:
            fila = resultados[0]
            id_usuario, nombre, apellido, email, password, id_rol, rol_nombre, rol_descripcion = fila
            rol = Rol(id_rol, rol_nombre, rol_descripcion)
            return Usuario(nombre, apellido, email, password, rol, id_usuario=id_usuario)
        return None

    def listar_todos(self) -> List[Usuario]:
        query = """
            SELECT u.id_usuario, u.nombre, u.apellido, u.email, u.password,
                   r.id_rol, r.nombre, r.descripcion
            FROM usuario u
            JOIN rol r ON u.id_rol = r.id_rol
        """
        resultados = execute_query(query)
        usuarios = []
        if resultados:
            for fila in resultados:
                id_usuario, nombre, apellido, email, password, id_rol, rol_nombre, rol_descripcion = fila
                rol = Rol(id_rol, rol_nombre, rol_descripcion)
                usuarios.append(Usuario(nombre, apellido, email, password, rol, id_usuario=id_usuario))
        return usuarios

    def modificar(self, usuario: Usuario) -> None:
        query = """
            UPDATE usuario
            SET nombre = %s, apellido = %s, password = %s, id_rol = %s
            WHERE email = %s
        """
        valores = (
            usuario.nombre,
            usuario.apellido,
            usuario.password,
            usuario.rol.id_rol,
            usuario.email
        )
        update_query(query, valores)

    def cambiar_rol(self, id_usuario: int, nuevo_rol: Rol) -> bool:
        query = "UPDATE usuario SET id_rol = %s WHERE id_usuario = %s"
        return update_query(query, (nuevo_rol.id_rol, id_usuario))

    def eliminar_por_email(self, email: str) -> None:
        query = "DELETE FROM usuario WHERE email = %s"
        delete_query(query, (email,))


