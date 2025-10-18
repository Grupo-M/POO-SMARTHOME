class Casa:
    """
    Representa una casa dentro del sistema SmartHome.
    """

    def __init__(self, id_casa: int, nombre: str):
        if id_casa <= 0:
            raise ValueError("El ID de la casa debe ser un número positivo.")
        if not nombre.strip():
            raise ValueError("El nombre de la casa no puede estar vacío.")

        self.__id_casa = id_casa
        self.__nombre = nombre

    @property
    def id_casa(self) -> int:
        """Devuelve el ID de la casa."""
        return self.__id_casa

    @property
    def nombre(self) -> str:
        """Devuelve el nombre de la casa."""
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        """Permite modificar el nombre de la casa."""
        if not nuevo_nombre.strip():
            raise ValueError("El nombre de la casa no puede estar vacío.")
        self.__nombre = nuevo_nombre

    def __str__(self) -> str:
        """Devuelve una representación legible de la casa."""
        return f"Casa {self.__nombre} (ID: {self.__id_casa})"


   
