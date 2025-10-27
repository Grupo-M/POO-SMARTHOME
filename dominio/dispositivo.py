from dominio.ubicacion import Ubicacion

class Dispositivo:
    """Representa un dispositivo del sistema SmartHome con encapsulamiento."""

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
        return self.__estado

    @estado.setter
    def estado(self, valor: str) -> None:
        if valor not in ("encendido", "apagado"):
            raise ValueError("Estado debe ser 'encendido' o 'apagado'")
        self.__estado = valor

    @property
    def esencial(self) -> bool:
        return self.__esencial

    @property
    def ubicacion(self) -> Ubicacion:
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion: Ubicacion) -> None:
        self.__ubicacion = nueva_ubicacion

    def encender(self) -> None:
        self.__estado = "encendido"

    def apagar(self) -> None:
        self.__estado = "apagado"

    def cambiar_estado(self) -> None:
        if self.__estado == "apagado":
            self.encender()
        else:
            self.apagar()

    def __str__(self) -> str:
        return (
            f"[{self.__id_dispositivo}] {self.__nombre} - "
            f"Estado: {self.__estado} - "
            f"Esencial: {'Sí' if self.__esencial else 'No'} - "
            f"Ubicación: {self.__ubicacion.nombre}"
        )
