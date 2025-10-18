class Rol:
    def __init__(self, id_rol: int, nombre: str, descripcion: str):
        self.__id_rol = id_rol
        self.__nombre = nombre
        self.__descripcion = descripcion

    @property
    def id_rol(self) -> int:
        return self.__id_rol
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre.strip():  
            raise ValueError("El nombre del rol no puede estar vacío.")
        self.__nombre = nuevo_nombre


    @property
    def descripcion(self) -> str:
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, nueva_descripcion: str) -> None:
        if not nueva_descripcion.strip():
            raise ValueError("La descripción del rol no puede estar vacía.")
        self.__descripcion = nueva_descripcion


    def __str__(self) -> str:
        return f"Rol {self.__nombre} (ID: {self.__id_rol}): {self.__descripcion}"
