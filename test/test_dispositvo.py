import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dominio.dispositivo import Dispositivo
from dominio.ubicacion import Ubicacion

def test_cambiar_estado_dispositivo():
    ubicacion = Ubicacion(1, "Cocina")

    dispositivo = Dispositivo(
        id_dispositivo=1,
        nombre="Luz cocina",
        esencial=True,
        ubicacion=ubicacion
    )

    assert dispositivo.estado == "apagado"

    dispositivo.cambiar_estado()
    assert dispositivo.estado == "encendido"

    dispositivo.cambiar_estado()
    assert dispositivo.estado == "apagado"
