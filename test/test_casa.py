import unittest
from modelos import Casa  # ajusta la ruta según tu proyecto

class TestCasa(unittest.TestCase):
    def test_inicializacion(self):
        c = Casa(id_casa=1, nombre="Mi Casa")
        self.assertEqual(c.id_casa, 1)
        self.assertEqual(c.nombre, "Mi Casa")

if __name__ == "__main__":
    unittest.main()