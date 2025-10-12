import unittest
from dominio import Ubicacion
from dominio import Dispositivo


class TestUbicacion(unittest.TestCase):

    def setUp(self):
        # Creamos una Ubicacion con FK a la Casa (id_casa = 1)
        self.ubicacion = Ubicacion(1, "Cocina", id_casa=1)
        # Creamos un Dispositivo asignado a esta ubicacion
        self.dispositivo = Dispositivo(1, "Luz Cocina", "apagado", True, id_ubicacion=1)

    def test_agregar_y_listar_dispositivo(self):
        self.ubicacion.agregar_dispositivo(self.dispositivo)
        self.assertIn("Luz Cocina", self.ubicacion.listar_dispositivos())

    def test_evitar_dispositivo_duplicado(self):
        self.ubicacion.agregar_dispositivo(self.dispositivo)
        self.ubicacion.agregar_dispositivo(self.dispositivo)  # lo intenta dos veces
        self.assertEqual(len(self.ubicacion.dispositivos), 1)

    def test_eliminar_dispositivo(self):
        self.ubicacion.agregar_dispositivo(self.dispositivo)
        self.ubicacion.eliminar_dispositivo(self.dispositivo)
        self.assertNotIn(self.dispositivo, self.ubicacion.dispositivos)

    def test_encender_y_apagar_dispositivos(self):
        self.ubicacion.agregar_dispositivo(self.dispositivo)

        self.ubicacion.encender()
        self.assertEqual(self.dispositivo.estado, "encendido")

        self.ubicacion.apagar()
        self.assertEqual(self.dispositivo.estado, "apagado")

