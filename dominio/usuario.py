
from typing import Optional
from dominio.rol import Rol

ROL_POR_DEFECTO = Rol(1, "usuario", "Permisos básicos")

class Usuario:
    """
    Clase que representa un usuario del sistema SmartHome.
    Aplica encapsulamiento usando atributos privados y propiedades.
    """

    def __init__(self, nombre: str, apellido: str, email: str, password: str, rol: Optional[Rol] = None):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self.__password = password          
        self.__rol = rol if rol else ROL_POR_DEFECTO  
    
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def apellido(self) -> str:
        return self._apellido

    @property
    def email(self) -> str:
        return self._email

    @property
    def rol(self) -> Rol:
        return self.__rol

    def validar_credenciales(self, email: str, password: str) -> bool:
        return self._email == email and self.__password == password

    def modificar_rol(self, nuevo_rol: Rol):
        self.__rol = nuevo_rol
