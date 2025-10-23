from abc import ABC, abstractmethod
from typing import List, Optional
from dominio.usuario import Usuario
from dominio.rol import Rol


class IUsuarioDAO(ABC):
    """Interfaz para el acceso a datos de la entidad Usuario."""

    @abstractmethod
    def guardar(self, usuario: Usuario) -> bool:
        """Guarda un nuevo usuario en la base de datos."""
        pass

    @abstractmethod
    def obtener_por_email(self, email: str) -> Optional[Usuario]:
        """Obtiene un usuario a partir de su email."""
        pass

    @abstractmethod
    def obtener_por_id(self, id_usuario: int) -> Optional[Usuario]:
        """Obtiene un usuario según su ID."""
        pass

    @abstractmethod
    def listar_todos(self) -> List[Usuario]:
        """Devuelve una lista con todos los usuarios registrados."""
        pass

    @abstractmethod
    def modificar(self, usuario: Usuario) -> None:
        """Modifica los datos de un usuario existente."""
        pass

    @abstractmethod
    def cambiar_rol(self, id_usuario: int, nuevo_rol: Rol) -> bool:
        """Cambia el rol asignado a un usuario."""
        pass

    @abstractmethod
    def eliminar_por_email(self, email: str) -> None:
        """Elimina un usuario según su email."""
        pass
