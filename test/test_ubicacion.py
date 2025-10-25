from dominio.casa import Casa
from dominio.ubicacion import Ubicacion


def test_ubicacion_getters():
    casa = Casa(1, "Mi Casa")
    ubicacion = Ubicacion(20, "Cocina", casa)

    assert ubicacion.id_ubicacion == 20
    assert ubicacion.nombre == "Cocina"
    assert ubicacion.casa == casa

