from dominio.casa import Casa

class Ubicacion:
    def __init__(self, id_ubicacion: int, nombre: str, casa: Casa):
        self.__id_ubicacion = id_ubicacion
        self.__nombre = nombre
        self.__casa = casa

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

    def __str__(self) -> str:
        return f"Ubicación {self.__nombre} (ID: {self.__id_ubicacion}, Casa ID: {self.__casa.id_casa})"


