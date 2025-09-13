"""
Test para la clase Usuario.
Verifica creación, validación de credenciales y modificación de rol.
"""

# pylint: disable=import-error, missing-function-docstring, invalid-name
from modelos.usuario import Usuario, ROL_POR_DEFECTO
from modelos.rol import Rol


def test_crear_usuario():
    usuario = Usuario("Carolina", "Lanfranco", "caro123@gmail.com", "Oreo4")

    # Verificar que los atributos públicos existan
    assert hasattr(usuario, "nombre")
    assert hasattr(usuario, "apellido")
    assert hasattr(usuario, "email")
    
    # Verificar que el rol por defecto esté asignado
    assert usuario.rol == ROL_POR_DEFECTO


def test_validar_credenciales():
    usuario = Usuario("Caro", "Lanfranco", "caro123@gmail.com", "Oreo4")

    # Comprobar credenciales correctas
    assert usuario.validar_credenciales("caro123@gmail.com", "Oreo4") is True
    # Comprobar credenciales incorrectas
    assert usuario.validar_credenciales("caro123@gmail.com", "wrong") is False
    assert usuario.validar_credenciales("wrong@gmail.com", "Oreo4") is False


def test_modificar_rol():
    usuario = Usuario("Caro", "Lanfranco", "caro123@gmail.com", "Oreo4")
    
    # Creamos un rol de administrador
    rol_admin = Rol(2, "administrador", "Acceso completo")
    
    # Modificamos el rol
    usuario.modificar_rol(rol_admin)

    # Verificar que el rol se haya actualizado correctamente
    assert usuario.rol.nombre == "administrador"
    assert usuario.rol.descripcion == "Acceso completo"
