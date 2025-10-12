
from dominio.ubicacion import Ubicacion

class Dispositivo:
    """
    Representa un dispositivo del sistema SmartHome.
    """

    def __init__(self, id_dispositivo: int, nombre: str, estado: str, esencial: bool, ubicacion: Ubicacion):
        self.id_dispositivo = id_dispositivo
        self.nombre = nombre
        self.estado = estado
        self.esencial = esencial
        self.__ubicacion = ubicacion

    @property
    def ubicacion(self) -> Ubicacion:
        """Devuelve la ubicación del dispositivo."""
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion: Ubicacion):
        """Actualiza la ubicación del dispositivo."""
        self.__ubicacion = nueva_ubicacion

    def encender(self):
        """Cambia el estado del dispositivo a encendido."""
        self.estado = "encendido"
        print(f"{self.nombre} está encendido.")

    def apagar(self):
        """Cambia el estado del dispositivo a apagado."""
        self.estado = "apagado"
        print(f"{self.nombre} está apagado.")

    def cambiar_estado(self):
        """Alterna entre encendido y apagado."""
        if self.estado == "apagado":
            self.encender()
        else:
            self.apagar()

    def __str__(self):
        """Devuelve una representación legible del dispositivo."""
        return f"[{self.id_dispositivo}] {self.nombre} - Estado: {self.estado} - Esencial: {'Sí' if self.esencial else 'No'} - Ubicación: {self.ubicacion.nombre}"
