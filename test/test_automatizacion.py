from dominio.automatizacion import Automatizacion
from dominio.dispositivo import Dispositivo
from dominio.casa import Casa
from dominio.ubicacion import Ubicacion


def test_activar_modo_ahorro_apaga_dispositivos():
    casa = Casa(1, "Principal")
    ubicacion = Ubicacion(1, "Sala", casa)

    d1 = Dispositivo(1, "Luz", "encendido", False, ubicacion)
    d2 = Dispositivo(2, "Ventilador", "encendido", False, ubicacion)
    dispositivos = [d1, d2]

    auto = Automatizacion("Modo Ahorro")
    auto.activar_modo_ahorro(dispositivos)

    assert d1.estado == "apagado"
    assert d2.estado == "apagado"


def test_automatizacion_nombre_valido():
    auto = Automatizacion("Modo Eco")
    assert auto.nombre == "Modo Eco"



