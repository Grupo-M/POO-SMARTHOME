from typing import Optional
from dominio.rol import Rol

ROL_POR_DEFECTO = Rol(2, "Usuario", "Permisos básicos")

class Usuario:
    """Clase que representa un usuario del sistema SmartHome."""

    def __init__(self, nombre: str, apellido: str, email: str,
                 password: str, rol: Optional[Rol] = None, id_usuario: Optional[int] = None) -> None:

        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__password = password
        self.__rol = rol if rol else ROL_POR_DEFECTO

    @property
    def id_usuario(self) -> Optional[int]:
        return self.__id_usuario

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def apellido(self) -> str:
        return self.__apellido

    @property
    def email(self) -> str:
        return self.__email

    @property
    def rol(self) -> Rol:
        return self.__rol

    @rol.setter
    def rol(self, nuevo_rol: Rol) -> None:
        self.__rol = nuevo_rol

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, nueva_password: str) -> None:
        if len(nueva_password) < 4:
            raise ValueError("El password debe tener al menos 4 caracteres.")
        self.__password = nueva_password

    def validar_credenciales(self, email: str, password: str) -> bool:
        return self.__email == email and self.__password == password



