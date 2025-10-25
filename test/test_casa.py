import pytest
from dominio.casa import Casa


def test_casa_creacion_valida():
    casa = Casa(10, "Mi Hogar")
    assert casa.id_casa == 10
    assert casa.nombre == "Mi Hogar"


def test_cambiar_nombre_casa_valido():
    casa = Casa(2, "Antes")
    casa.nombre = "Después"
    assert casa.nombre == "Después"


def test_casa_nombre_invalido():
    with pytest.raises(ValueError):
        Casa(3, "   ")
