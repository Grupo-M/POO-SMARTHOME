import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelos.rol import Rol

def test_creacion_rol():
    rol = Rol(1, "Administrador", "Acceso total al sistema")
    assert rol.id_rol == 1
    assert rol.nombre == "Administrador"
    assert rol.descripcion == "Acceso total al sistema"

def test_tipos_de_datos():
    rol = Rol(2, "Usuario", "Acceso limitado")
    assert isinstance(rol.id_rol, int)
    assert isinstance(rol.nombre, str)
    assert isinstance(rol.descripcion, str)
