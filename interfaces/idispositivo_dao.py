
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

class IDispositivoDAO(ABC):
    """
    Interfaz que define los métodos que debe implementar cualquier clase DAO
    encargada de gestionar los dispositivos en la base de datos.
    """

    @abstractmethod
    def insertar_objeto(self, nombre: str, estado: str, esencial: int, id_ubicacion: int) -> bool:
        """Inserta un nuevo dispositivo en la base de datos."""
        pass


    @abstractmethod
    def obtener_todos_objetos(self) -> Optional[List[Tuple]]:
        """Obtiene todos los dispositivos registrados en la base de datos."""
        pass


    @abstractmethod
    def actualizar_estado(self, id_dispositivo: int, nuevo_estado: str) -> bool:
        """Actualiza el estado (por ejemplo: encendido/apagado) de un dispositivo."""
        pass

    @abstractmethod
    def modificar(self, id_dispositivo: int, nombre: str, estado: str, esencial: int, id_ubicacion: int) -> bool:
        """Modifica los datos de un dispositivo existente."""
        pass

    @abstractmethod
    def eliminar(self, id_dispositivo: int) -> bool:
        """Elimina un dispositivo por su identificador."""
        pass

