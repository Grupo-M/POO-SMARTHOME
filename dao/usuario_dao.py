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
            SELECT nombre, apellido, email, password, id_rol
            FROM usuario
            WHERE email = %s
        """
        resultados = execute_query(query, (email,))
        if resultados and len(resultados) > 0:
            nombre, apellido, email, password, id_rol = resultados[0]
            rol = Rol(id_rol, "usuario", "Permisos básicos")
            return Usuario(nombre, apellido, email, password, rol) # type: ignore
        return None

    def listar_todos(self) -> List[Usuario]:
        query = """
            SELECT nombre, apellido, email, password, id_rol
            FROM usuario
        """
        resultados = execute_query(query)
        usuarios = []
        if resultados:
            for fila in resultados:
                nombre, apellido, email, password, id_rol = fila
                rol = Rol(id_rol, "usuario", "Permisos básicos") # type: ignore
                usuario = Usuario(nombre, apellido, email, password, rol) # type: ignore
                usuarios.append(usuario)
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

    def eliminar_por_email(self, email: str) -> None:
        query = "DELETE FROM usuario WHERE email = %s"
        valores = (email,)
        delete_query(query, valores)

        