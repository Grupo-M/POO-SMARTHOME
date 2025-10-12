
import sys
import os
from typing import List, Optional
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dominio.usuario import Usuario
from dominio.rol import Rol
from conn.db_conn import insert_query, execute_query, update_query, delete_query
from dao.rol_dao import obtener_rol_por_id



class UsuarioDAO:
    def guardar(self, usuario: Usuario) -> None:
        # Guarda un nuevo usuario en la base de datos
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password, id_rol)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (
            usuario.nombre,
            usuario.apellido,
            usuario.email,
            usuario.password,
            usuario.rol.id_rol
        )
        insert_query(query, valores)

    def obtener_por_email(self, email: str) -> Optional[Usuario]:
        # Busca un usuario por su email
        query = """
            SELECT nombre, apellido, email, password, id_rol
            FROM usuarios
            WHERE email = %s
        """
        resultados = execute_query(query, (email,))

        if resultados and len(resultados) > 0:
            nombre, apellido, email, password, id_rol = resultados[0]
            rol = Rol(id_rol, "usuario", "Permisos básicos")
            return Usuario(nombre, apellido, email, password, rol) # type: ignore
        return None

    def listar_todos(self) -> List[Usuario]:
        # Devuelve una lista de todos los usuarios registrados
        query = """
            SELECT nombre, apellido, email, password, id_rol
            FROM usuarios
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
        # Modifica los datos de un usuario existente
        query = """
            UPDATE usuarios
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
        # Borra un usuario usando su email
        query = "DELETE FROM usuarios WHERE email = %s"
        valores = (email,)
        delete_query(query, valores)

        