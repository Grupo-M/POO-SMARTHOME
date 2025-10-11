"""
usuario.py
Clase que representa un usuario del sistema SmartHome.
"""

from typing import Optional
from modelos.rol import Rol

ROL_POR_DEFECTO = Rol(1, "usuario", "Permisos básicos")


class Usuario:
    """
    Clase que representa un usuario del sistema SmartHome.
    Aplica encapsulamiento usando atributos privados y propiedades.
    """

    def __init__(self, nombre: str, apellido: str, email: str,
                 password: str, rol: Optional[Rol] = None) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self.__password = password
        self.__rol = rol if rol else ROL_POR_DEFECTO

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del usuario."""
        return self._nombre

    @property
    def apellido(self) -> str:
        """Devuelve el apellido del usuario."""
        return self._apellido

    @property
    def email(self) -> str:
        """Devuelve el email del usuario."""
        return self._email

    @property
    def rol(self) -> Rol:
        """Devuelve el rol del usuario."""
        return self.__rol

    @rol.setter
    def rol(self, nuevo_rol: Rol) -> None:
        """Modifica el rol del usuario."""
        self.__rol = nuevo_rol

    @property
    def password(self) -> str:
        """Devuelve la contraseña del usuario."""
        return self.__password

    @password.setter
    def password(self, nueva_password: str) -> None:
        """Modifica la contraseña del usuario con validación mínima."""
        if len(nueva_password) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres.")
        self.__password = nueva_password

    def validar_credenciales(self, email: str, password: str) -> bool:
        """
        Verifica si las credenciales coinciden con las del usuario.
        """
        return self._email == email and self.__password == password

