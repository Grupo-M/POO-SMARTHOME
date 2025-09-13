from typing import List
from dispositivo import Dispositivo


class Ubicacion:

    # Clase Ubicacion: representa un espacio físico dentro de la Casa
    # donde se asocian dispositivos inteligentes.
    # Relación: Composición con Dispositivo (los dispositivos dependen de la ubicación)

    def __init__(self, id_ubicacion: int, nombre: str):
        self.__id_ubicacion = id_ubicacion      
        self.__nombre = nombre                  
        self.__dispositivos: List[Dispositivo] = []  

    def id_ubicacion(self) -> int:
        return self.__id_ubicacion

    def nombre(self) -> str:
        return self.__nombre

    def nombre(self, nuevo_nombre: str):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre de la ubicación no puede estar vacío")
        self.__nombre = nuevo_nombre

    def agregar_dispositivo(self, dispositivo: Dispositivo) -> None:
        
        # Agrega un dispositivo a la ubicacion si no esta ya presente

       if dispositivo not in self.__dispositivos:
            self.__dispositivos.append(dispositivo)

    def eliminar_dispositivo(self, dispositivo: Dispositivo) -> None:
        
        # Elimina un dispositivo de la ubicacion si esta presente

        if dispositivo in self.__dispositivos:
            self.__dispositivos.remove(dispositivo)

    def listar_dispositivos(self) -> List[str]:
        
        # Devuelve una lista con los nombres de los dispositivos de la ubicación.

        return [d.nombre for d in self.__dispositivos]

    def encender(self) -> None:
        
        # Enciende todos los dispositivos de la ubicación.
        
        for dispositivo in self.__dispositivos:
            dispositivo.encender()

    def apagar(self) -> None:
        
        # Apaga todos los dispositivos de la ubicación.
        
        for dispositivo in self.__dispositivos:
            dispositivo.apagar()

    def __str__(self) -> str:
        return f"Ubicación {self.__nombre} (ID: {self.__id_ubicacion})"
