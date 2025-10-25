from dominio.dispositivo import Dispositivo
from dominio.casa import Casa
from dominio.ubicacion import Ubicacion


def crear_dispositivo():
    casa = Casa(1, "Casa")
    ubic = Ubicacion(1, "Living", casa)
    return Dispositivo(1, "Lámpara", "apagado", False, ubic)


def test_encender_dispositivo():
    d = crear_dispositivo()
    d.encender()
    assert d.estado == "encendido"


def test_apagar_dispositivo():
    d = crear_dispositivo()
    d.encender()
    d.apagar()
    assert d.estado == "apagado"


def test_cambiar_estado():
    d = crear_dispositivo()
    d.cambiar_estado()
    assert d.estado == "encendido"

