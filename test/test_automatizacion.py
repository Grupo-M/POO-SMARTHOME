import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dominio.automatizacion import Automatizacion

def test_activar_modo_ahorro():
    auto = Automatizacion("Modo Ahorro")
    dispositivos = [
        {"nombre": "Luz", "estado": "encendido"},
        {"nombre": "Ventilador", "estado": "encendido"}
    ]
    resultado = auto.activar_modo_ahorro(dispositivos)
    esperado = [
        {"nombre": "Luz", "estado": "apagado"},
        {"nombre": "Ventilador", "estado": "apagado"}
    ]
    assert resultado == esperado
