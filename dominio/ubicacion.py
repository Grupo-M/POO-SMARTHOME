from typing import List
from dominio.dispositivo import Dispositivo


class Ubicacion:
    # Clase Ubicacion: Representa un espacio físico dentro de la Casa (ejemplo: cocina, dormitorio).

    def __init__(self, id_ubicacion: int, nombre: str, id_casa: int):
        
        self.id_ubicacion: int = id_ubicacion    
        self.nombre: str = nombre
        self.id_casa: int = id_casa               
        self.dispositivos: List[Dispositivo] = [] # Lista de dispositivos en esta ubicación

    def agregar_dispositivo(self, dispositivo: Dispositivo) -> None:
        # Agrega un dispositivo a la ubicación si no está ya presente
        if dispositivo not in self.dispositivos:
            self.dispositivos.append(dispositivo)

    def eliminar_dispositivo(self, dispositivo: Dispositivo) -> None:
        # Elimina un dispositivo de la ubicación si está presente
        if dispositivo in self.dispositivos:
            self.dispositivos.remove(dispositivo)

    def listar_dispositivos(self) -> List[str]:
        # Devuelve una lista con los nombres de los dispositivos de la ubicación
        return [d.nombre for d in self.dispositivos]

    def encender(self) -> None:
        # Enciende todos los dispositivos de la ubicación
        for dispositivo in self.dispositivos:
            dispositivo.encender()

    def apagar(self) -> None:
        # Apaga todos los dispositivos de la ubicación
        for dispositivo in self.dispositivos:
            dispositivo.apagar()

    def __str__(self) -> str:
        return f"Ubicación {self.nombre} (ID: {self.id_ubicacion}, Casa ID: {self.id_casa})"
