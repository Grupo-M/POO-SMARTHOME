import pytest
from dominio.rol import Rol


def test_cambiar_nombre_valido():
    rol = Rol(1, "Admin", "Control total")
    rol.nombre = "Súper Admin"
    assert rol.nombre == "Súper Admin"


def test_nombre_invalido():
    rol = Rol(1, "Admin", "Control")
    with pytest.raises(ValueError):
        rol.nombre = "   "
