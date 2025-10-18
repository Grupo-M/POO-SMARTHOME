from typing import List
from dominio.dispositivo import Dispositivo
from dominio.casa import Casa

class Ubicacion:
    def __init__(self, id_ubicacion: int, nombre: str, casa: Casa):
        self.__id_ubicacion = id_ubicacion
        self.__nombre = nombre
        self.__casa = casa
        self.__dispositivos: List[Dispositivo] = []

    @property
    def id_ubicacion(self) -> int:
        return self.__id_ubicacion

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre  

    @property
    def casa(self) -> Casa:
        return self.__casa

    @property
    def dispositivos(self) -> List[Dispositivo]:
        
        return self.__dispositivos.copy()

    def agregar_dispositivo(self, dispositivo: Dispositivo) -> None:
        if dispositivo not in self.__dispositivos:
            self.__dispositivos.append(dispositivo)

    def eliminar_dispositivo(self, dispositivo: Dispositivo) -> None:
        if dispositivo in self.__dispositivos:
            self.__dispositivos.remove(dispositivo)

    def listar_dispositivos(self) -> List[str]:
        return [d.nombre for d in self.__dispositivos]

    def encender(self) -> None:
        for dispositivo in self.__dispositivos:
            dispositivo.encender()

    def apagar(self) -> None:
        for dispositivo in self.__dispositivos:
            dispositivo.apagar()

    def __str__(self) -> str:
        return f"Ubicación {self.__nombre} (ID: {self.__id_ubicacion}, Casa ID: {self.__casa.id_casa})"


