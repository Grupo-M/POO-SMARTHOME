import unittest
from ubicacion import Ubicacion
from dispositivo import Dispositivo


class TestUbicacion(unittest.TestCase):

    def test_agregar_y_listar_dispositivo(self):
        ubicacion = Ubicacion(1, "Cocina")
        dispositivo = Dispositivo(1, "Luz Cocina", "apagado", True, ubicacion)

        ubicacion.agregar_dispositivo(dispositivo)
        self.assertIn("Luz Cocina", ubicacion.listar_dispositivos())

    def test_encender_y_apagar_dispositivos(self):
        ubicacion = Ubicacion(2, "Dormitorio")
        dispositivo = Dispositivo(2, "Ventilador", "apagado", False, ubicacion)
        ubicacion.agregar_dispositivo(dispositivo)

        ubicacion.encender()
        self.assertEqual(dispositivo.estado, "encendido")

        ubicacion.apagar()
        self.assertEqual(dispositivo.estado, "apagado")

