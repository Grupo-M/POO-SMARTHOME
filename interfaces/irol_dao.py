
from abc import ABC, abstractmethod
from typing import Optional, List
from dominio.rol import Rol


class IRolDAO(ABC):
    """
    Interfaz que define el contrato para las operaciones de acceso a datos
    relacionadas con la entidad Rol.
    Cualquier clase que implemente esta interfaz debe cumplir estos métodos.
    """

    @abstractmethod
    def insertar(self, rol: Rol) -> bool:
        """Inserta un nuevo rol en la base de datos."""
        pass

    @abstractmethod
    def obtener_por_id(self, id_rol: int) -> Optional[Rol]:
        """Devuelve un objeto Rol según su ID, o None si no existe."""
        pass

    @abstractmethod
    def listar_todos(self) -> List[Rol]:
        """Devuelve una lista de todos los roles registrados en la base de datos."""
        pass

    @abstractmethod
    def actualizar(self, rol: Rol) -> bool:
        """Actualiza los datos de un rol existente."""
        pass

    @abstractmethod
    def eliminar(self, id_rol: int) -> bool:
        """Elimina un rol por su ID."""
        pass


