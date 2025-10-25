from dominio.usuario import Usuario
from dominio.rol import Rol


def test_validar_credenciales_correctas():
    rol = Rol(2, "Usuario", "Básico")
    usuario = Usuario("Caro", "Lanfranco", "caro@test.com", "1234", rol)
    assert usuario.validar_credenciales("caro@test.com", "1234")


def test_validar_credenciales_incorrectas():
    usuario = Usuario("Ana", "Test", "ana@test.com", "abcd")
    assert not usuario.validar_credenciales("mal@test.com", "abcd")
