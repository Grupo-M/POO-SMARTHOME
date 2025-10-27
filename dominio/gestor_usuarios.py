
from typing import Optional, List
from dominio.usuario import Usuario
from dominio.rol import Rol
from dao.usuario_dao import UsuarioDAO  # Tu DAO concreto

class GestorUsuarios:

    def __init__(self, admin_usuario: Usuario, usuario_dao: UsuarioDAO):
        if admin_usuario.rol.id_rol != 1:
            raise PermissionError("Solo administradores pueden usar GestorUsuarios.")
        self.admin_usuario = admin_usuario
        self._usuario_dao = usuario_dao  # Encapsulamos el DAO

    def agregar_usuario(self, usuario: Usuario) -> bool:
        # Aquí podemos poner validaciones de negocio
        return self._usuario_dao.guardar(usuario)

    def listar_usuarios(self) -> Optional[List[Usuario]]:
        return self._usuario_dao.listar_todos()

    def cambiar_rol(self, usuario_id: int, nuevo_rol: Rol) -> bool:
        # Validaciones de negocio, por ejemplo que no cambie el rol del admin principal
        if usuario_id == self.admin_usuario.id_usuario:
            raise ValueError("No se puede cambiar el rol del usuario administrador actual.")
        return self._usuario_dao.cambiar_rol(usuario_id, nuevo_rol)
