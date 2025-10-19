
from dominio.ubicacion import Ubicacion


class Dispositivo:
    """
    Representa un dispositivo del sistema SmartHome.
    Aplica encapsulamiento al atributo 'estado'.
    """

    def __init__(self, id_dispositivo: int, nombre: str, estado_inicial: str,
                 esencial: bool, ubicacion: Ubicacion):
        if estado_inicial not in ("encendido", "apagado"):
            raise ValueError("El estado inicial debe ser 'encendido' o 'apagado'.")

        self.__id_dispositivo = id_dispositivo
        self.__nombre = nombre
        self.__estado = estado_inicial
        self.__esencial = esencial
        self.__ubicacion = ubicacion

   
    @property
    def id_dispositivo(self) -> int:
        return self.__id_dispositivo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre.strip():
            raise ValueError("El nombre del dispositivo no puede estar vacío.")
        self.__nombre = nuevo_nombre

    @property
    def estado(self) -> str:
        """Devuelve el estado actual del dispositivo."""
        return self.__estado

    @property
    def esencial(self) -> bool:
        return self.__esencial

    @property
    def ubicacion(self) -> Ubicacion:
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion: Ubicacion) -> None:
        """Actualiza la ubicación del dispositivo."""
        self.__ubicacion = nueva_ubicacion

    
    def encender(self) -> None:
        """Cambia el estado del dispositivo a 'encendido'."""
        if self.__estado != "encendido":
            self.__estado = "encendido"
            print(f"{self.__nombre} está encendido.")

    def apagar(self) -> None:
        """Cambia el estado del dispositivo a 'apagado'."""
        if self.__estado != "apagado":
            self.__estado = "apagado"
            print(f"{self.__nombre} está apagado.")

    def cambiar_estado(self) -> None:
        """Alterna entre encendido y apagado."""
        if self.__estado == "apagado":
            self.encender()
        else:
            self.apagar()

    def __str__(self) -> str:
        """Devuelve una representación legible del dispositivo."""
        return (
            f"[{self.__id_dispositivo}] {self.__nombre} - "
            f"Estado: {self.__estado} - "
            f"Esencial: {'Sí' if self.__esencial else 'No'} - "
            f"Ubicación: {self.__ubicacion.nombre}"
        )
