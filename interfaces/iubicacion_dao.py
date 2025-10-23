from abc import ABC, abstractmethod
from typing import List
from dominio.ubicacion import Ubicacion


class IUbicacionDAO(ABC):
    """Interfaz para el acceso a datos de la entidad Ubicación."""

    @abstractmethod
    def obtener_todas(self) -> List[Ubicacion]:
        """Devuelve una lista con todas las ubicaciones registradas."""
        pass

